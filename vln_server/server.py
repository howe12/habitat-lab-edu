"""
JanusVLN HTTP Inference Service for Spark-I Robot
"""
import sys
sys.path.insert(0, "/root/gpufree-data/JanusVLN/src")

import io, base64, torch, copy
import numpy as np
from PIL import Image
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from transformers import AutoProcessor
from qwen_vl_utils import extract_vision_info
from qwen_vl.model.modeling_qwen2_5_vl import Qwen2_5_VLForConditionalGenerationForJanusVLN
from qwen_vl.model.vggt.utils.load_fn import load_and_preprocess_images

MODEL_PATH = "/root/gpufree-data/JanusVLN_Base/misstl/JanusVLN_Base"

model = None
processor = None
device = None
patch_size = None
merge_size = None

def load_model():
    global model, processor, device, patch_size, merge_size
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = Qwen2_5_VLForConditionalGenerationForJanusVLN.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True)
    model.eval()
    patch_size = processor.image_processor.patch_size
    merge_size = processor.image_processor.merge_size

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield

app = FastAPI(title="JanusVLN", lifespan=lifespan)
sessions = {}

@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": model is not None}

class ResetReq(BaseModel):
    session_id: str = "default"
    instruction: str

class StepReq(BaseModel):
    session_id: str = "default"
    image_base64: str
    step_id: int = 0

@app.post("/reset")
async def reset(req: ResetReq):
    sessions[req.session_id] = {"instruction": req.instruction, "history": [], "step": 0}
    if model: model.past_key_values_vggt = None
    return {"ok": True}

@app.post("/step")
async def step(req: StepReq):
    if not model: raise HTTPException(503, "Model not loaded")
    s = sessions.get(req.session_id, {"instruction": "", "history": [], "step": 0})
    if not s["instruction"]: raise HTTPException(400, "Call /reset first")

    # Decode incoming image
    img_data = req.image_base64.split(",", 1)[-1] if "," in req.image_base64 else req.image_base64
    img = Image.open(io.BytesIO(base64.b64decode(img_data))).convert("RGB")
    all_imgs = s["history"] + [img]

    # Build message (matching evaluation.py pattern)
    context = (
        f"These images are your historical observations and your current observation.\n"
        f"Your task is to {s['instruction']}\n"
        f"You should take one of the following actions:\n"
        f"MOVE_FORWARD\nTURN_LEFT\nTURN_RIGHT\nSTOP."
    )
    system_msg = {"role": "system", "content": "You are a visual language navigation model, and your should go to the locations to complete the given task. Compare the observation and instruction to infer your current progress, and then select the correct direction from the candidates to go to the target location and finish the task."}

    # Build image content list
    img_content = []
    for v in all_imgs:
        img_content.append({"type": "image", "image": v})
    img_content.append({"type": "text", "text": context})
    user_msg = {"role": "user", "content": img_content}

    messages = [[system_msg, user_msg]]

    # Apply chat template
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # Build images_vggt (last frame only) and image_inputs (all frames)
    images_vggt = []
    image_inputs = []
    for message in messages:
        vision_info = extract_vision_info(message)
        cur_images_vggt = []
        for i, ele in enumerate(vision_info):
            if "image" in ele:
                image = ele["image"]
                if isinstance(image, str) and "base64," in image:
                    _, b64_data = image.split("base64,", 1)
                    data = base64.b64decode(b64_data)
                    with io.BytesIO(data) as bio:
                        image = copy.deepcopy(Image.open(bio))
            else:
                raise NotImplementedError("Unsupported vision info type")

            assert isinstance(image, Image.Image), f"Unsupported image type: {type(image)}"
            image = load_and_preprocess_images([image])[0]

            # Last image in the message goes to images_vggt
            if i == len(vision_info) - 1:
                cur_images_vggt.append(image)

            # Dimension correction for patch_size/merge_size alignment
            _, height, width = image.shape
            if (width // patch_size) % merge_size > 0:
                width = width - (width // patch_size) % merge_size * patch_size
            if (height // patch_size) % merge_size > 0:
                height = height - (height // patch_size) % merge_size * patch_size
            image = image[:, :height, :width]
            image_inputs.append(image)

        images_vggt.append(torch.stack(cur_images_vggt))

    # Process inputs
    inputs = processor(
        text=text,
        images=image_inputs,
        videos=None,
        padding=True,
        return_tensors="pt",
        do_rescale=False
    )
    inputs["images_vggt"] = [feat.to(device) for feat in images_vggt]
    inputs = {k: (v if k == "images_vggt" else v.to(device)) for k, v in inputs.items()}

    # Generate
    with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.bfloat16):
        gen = model.generate(**inputs, max_new_tokens=24, temperature=0, do_sample=False,
                             pad_token_id=processor.tokenizer.pad_token_id)

    out_ids = [o[len(i):] for i, o in zip(inputs["input_ids"], gen)]
    out = processor.batch_decode(out_ids, skip_special_tokens=True)[0].strip().lower()

    acts = {"forward": "MOVE_FORWARD", "left": "TURN_LEFT", "right": "TURN_RIGHT", "stop": "STOP"}
    action = "STOP"
    for k, v in acts.items():
        if k in out: action = v; break

    s["history"].append(img)
    if len(s["history"]) > 10: s["history"] = s["history"][-10:]
    s["step"] = req.step_id + 1

    return {"action": action, "step_id": req.step_id, "raw_output": out}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8443)
