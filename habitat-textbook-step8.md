# 第8章：真机部署 — Habitat 从零理解

> 视觉语言模型（VLM）直接接收 RGB 图像 + 自然语言指令 → 输出控制命令。 无需地图、无需 ROS 导航栈、无需预建环境模型——一个模型解决全部问题。

## 本章概览：从架构到微调的完整流程

将仿真训练的 VLN 模型部署到真实 Spark‑I 机器人：架构设计 → 模型选型 → 零样本直控 → 数据采集 → LoRA 微调。

两种真机方案：VLN→ROS Nav2（稳妥）和 VLM 端到端（前沿）。前置：[第7章 VLN](habitat-textbook-step7.html) 仿真训练。

| \#  | 案例                           | 你将学会                     | 难度   |
| --- | ---------------------------- | ------------------------ | ---- |
| 8-1 | [云-边-端 VLN 架构](#case8-1)     | Spark→L40 拓扑、SSH 隧道、推理链路 | ⭐⭐   |
| 8-2 | [理解 VLM 导航原理](#case8-2)      | VLM 为什么能做导航、核心论文思路       | ⭐⭐   |
| 8-3 | [模型选型与部署方案](#case8-3)        | JanusVLN 等模型对比、INT8 量化   | ⭐⭐⭐  |
| 8-4 | [云端直控真机 ★](#case8-4)         | JanusVLN 零样本部署、防打转、显示窗口  | ⭐⭐⭐⭐ |
| 8-5 | [仿真与真机测试计划](#case8-5)        | 评估指标、测试场景设计、安全守则         | ⭐⭐   |
| 8-6 | [真机采集与数据处理](#case8-6)        | rosbag录制、仿真采集、数据质量检查     | ⭐⭐⭐  |
| 8-7 | [LoRA 微调 JanusVLN](#case8-7) | 单卡微调、数据采集方法论             | ⭐⭐⭐⭐ |
| 8-8 | [两种方法全面对比](#case8-8)         | VLN+Nav2 vs JanusVLN 直控  | ⭐⭐⭐  |

## 方案一 · VLN → ROS Nav2

将第7章训练好的 VLN 模型部署到真实机器人：VLN 做高层决策 → 输出子目标位姿 → ROS Nav2 执行底层导航。

## 方案二 · VLM 端到端

不使用导航栈，视觉语言模型直接输出控制指令——无地图、端到端的 VLN 方案。

## 8-1 · 云-边-端 VLN 架构

<div>

**① 案例含义**

当模型大到 80 亿参数（JanusVLN），真机的 Jetson / 树莓派根本跑不动。 本案例介绍**云-边-端分离**方案（具体实现在 [8-4](#case8-4)）： 真机负责感知+执行，云端 GPU 负责推理。

</div>

### ② 系统架构

``` 
    复制
    # ═══════════ 真机 (Spark-I, Jetson Orin) ═══════════
#   算力有限，只做采集 + 执行

# ═══════════ 云端 (L40 GPU 服务器) ═══════════
#   JanusVLN 推理，~2 秒/步

# 数据流:
#
#  真机 📷 ──JPEG(50KB)──→ 云端
#  真机 🤖 ←──action──── 云端 (JanusVLN 推理)
#
#  循环: 拍照→上传→推理→回传→Nav2执行→拍照→...
```

</div>

| 模块        | 部署位置   | 硬件              | 职责                               |
| --------- | ------ | --------------- | -------------------------------- |
| 📷 图像采集    | 真机     | RealSense D435i | RGB 拍照 → JPEG 压缩                 |
| 📤 图像上传    | 真机     | WiFi/5G         | HTTP POST 到云端                    |
| 🧠 VLN 推理  | **云端** | **L40 GPU**     | JanusVLN: 图像+指令→动作               |
| 📥 动作回传    | 云端→真机  | WiFi/5G         | JSON {"action": "MOVE\_FORWARD"} |
| 🗺️ 动作映射   | 真机     | Jetson CPU      | FORWARD → Nav2 目标位姿              |
| 🚗 路径规划+控制 | 真机     | Jetson + 电机     | ROS Nav2 规划+执行                   |

### ③ 核心代码

**真机侧：image\_bridge\_node.py**

``` 
    复制
    import rclpy, cv2, requests, json
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class VLNCloudBridge(rclpy.node.Node):
    def __init__(self):
        super().__init__('vln_cloud_bridge')
        self.bridge = CvBridge()
        self.cloud_url = "http://L40_IP:8000/step"
        self.instruction = "Go to the kitchen"  # 可动态更新

        # 订阅相机
        self.sub = self.create_subscription(
            Image, '/camera/color/image_raw', self.on_image, 10)

        # 发布子目标给 Nav2
        self.goal_pub = self.create_publisher(
            PoseStamped, '/goal_pose', 10)

    def on_image(self, msg):
        # 1. ROS Image → JPEG bytes
        cv_img = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        _, jpg = cv2.imencode('.jpg', cv_img, [cv2.IMWRITE_JPEG_QUALITY, 80])

        # 2. 上传到云端
        resp = requests.post(self.cloud_url,
            files={'image': jpg.tobytes()},
            data={'instruction': self.instruction},
            timeout=5)

        # 3. 解析动作
        action = resp.json()['action']  # "MOVE_FORWARD"
        self.get_logger().info(f'Action: {action}')

        # 4. 映射为 Nav2 目标并发布
        if action == 'STOP':
            self.cancel_nav()
        else:
            goal = self.action_to_goal(action)
            self.goal_pub.publish(goal)
```

**云端：inference\_server.py**

``` 
    复制
    from fastapi import FastAPI, File, Form
from PIL import Image
import io

app = FastAPI()
model = load_janusvln()  # 启动时加载模型

@app.post("/step")
async def step(image: bytes = File(...), instruction: str = Form(...)):
    # 1. JPEG → PIL Image
    pil_img = Image.open(io.BytesIO(image)).convert('RGB')

    # 2. VLN 推理
    action = model.predict(pil_img, instruction)  # ~2 秒

    return {"action": action}  # "MOVE_FORWARD" | "TURN_LEFT" | "STOP"

# 启动: uvicorn inference_server:app --host 0.0.0.0 --port 8000
```

### ④ 每步延迟预算

| 阶段              | 耗时            | 占比      | 优化空间            |
| --------------- | ------------- | ------- | --------------- |
| 拍照 + 压缩         | \~0.05s       | 2%      | 已足够             |
| 网络上传 (50KB)     | \~0.02s       | 1%      | WiFi 6 / 5G 无压力 |
| **JanusVLN 推理** | **\~2.0s**    | **80%** | 模型量化 / TensorRT |
| 网络回传            | \~0.01s       | 0%      | 可忽略             |
| Nav2 规划         | \~0.1s        | 4%      | 已足够             |
| 机器人移动 (0.25m)   | \~0.3s        | 13%     | 取决于速度           |
| **合计**          | **\~2.5 秒/步** |         |                 |

> ⚠️
> 
> <div class="warn-title">
> 
> ⚠️ 推理速度是瓶颈——但不是死结
> 
> 2 秒/步听起来慢，但 VLN 导航通常 10-30 步到达目标 → **总耗时 25-75 秒**，实际可用。 如果接受不了，可以：模型量化到 INT8（速度 2x）、换小模型（Qwen2.5-VL-3B）、 或等下一代 GPU（RTX 5090 推理 \<0.5s）。
> 
> <div id="case8-2" class="section">
> 
> <div class="container">
> 
> ## 8-2 · 理解 VLM 导航原理
> 
> <div>
> 
> **① 案例含义 — VLM 导航与传统 VLN 有什么不同？**
> 
> 传统 VLN（如 [第7章](habitat-textbook-step7.html) 训练的模型）是一个**任务专用的小模型**：CNN 编码图像 + LSTM 编码指令 → 输出离散动作。 VLM 导航则使用一个**通用的大模型**（数亿到数十亿参数），已在海量图文数据上预训练过， 具备对场景、物体、空间关系的广泛理解。  
>   
> **核心区别：**VLN 需要针对导航任务专门训练；VLM 已经"知道"什么是厨房、走廊、门口， 导航只是它推理能力的延伸。
> 
> </div>
> 
> ### ② 核心论文思路拆解
> 
> <div class="dual-panel">
> 
> <div class="panel">
> 
> #### 📄 NaVid-4D (CVPR 2025)
> 
> **核心思路：**将导航形式化为视频预测任务。  
> 输入：**历史视频帧**（多帧 RGB）+ 指令文本  
> 输出：**未来轨迹**（一系列 waypoint 坐标）  
> 特点：不显式建图，利用视频中的时序信息隐式编码空间结构。  
> 模型：基于 Video Diffusion 架构，在 Habitat 仿真中训练。  
> **与我们的关系：**可以复用 [第7章](habitat-textbook-step7.html) 训练出的模型作为特征提取器。
> 
> </div>
> 
> <div class="panel">
> 
> #### 📄 NaVILA (CoRL 2024)
> 
> **核心思路：**结合 VLM 的语义理解 + 传统导航策略。  
> 输入：RGB 图像 + 指令  
> 输出：**子目标**（不是最终动作，而是中间目标点）  
> 定位：介于方法一和方法二之间——VLM 做高层规划，但还需要底层控制器。  
> **与我们的关系：**可视为方法一的升级版：将 VLN 模型替换为大 VLM。
> 
> <div class="arch-diagram">
> 
> <div style="font-size:0.85rem;color:#f9a8d4;font-weight:700;margin-bottom:18px;">
> 
> VLM 端到端导航 — 极简架构
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#3b82f620;border:2px solid #3b82f6;min-width:180px;">
> 
> 📷 RGB 相机  
> <span class="small">单帧或历史帧 stack</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#8b5cf620;border:2px solid #8b5cf6;min-width:200px;">
> 
> 📝 自然语言指令  
> <span class="small">"走到厨房水池前"</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   输入   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#ec489920;border:2px solid #ec4899;min-width:500px;">
> 
> **VLM (Vision-Language Model)**  
> <span class="small">Qwen2-VL / LLaVA / GPT-4V / NaVid / NaVILA</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   输出   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⬆️ 前进  
> <span class="small">FORWARD 0.5m</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⬅️ 左转  
> <span class="small">LEFT 30°</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ➡️ 右转  
> <span class="small">RIGHT 30°</span>
> 
> </div>
> 
> <div class="arch-layer" style="background:#f59e0b20;border:2px solid #f59e0b;min-width:160px;">
> 
> ⏹️ 停止  
> <span class="small">STOP</span>
> 
> <div class="arch-arrow-center">
> 
> ↓   直接映射   ↓
> 
> </div>
> 
> <div class="arch-row">
> 
> <div class="arch-layer" style="background:#10b98120;border:2px solid #10b981;min-width:300px;">
> 
> /cmd\_vel (Twist)  
> <span class="small">驱动底盘电机</span>
> 
> </div>
> 
> <div class="highlight-box">
> 
> #### 🔑 关键洞察：VLM 导航的本质是 "视觉问答 + 行动"
> 
> 你可以把 VLM 导航理解为：  
>   
> **Q（指令）：**"走到厨房水池前面"  
> **VLM 看当前图像：**识别到 "我在客厅，前方是走廊，左边是厨房门"  
> **VLM 推理：**"我应该往前走，到厨房门口再左转"  
> **A（动作）：**FORWARD  
>   
> 每一步都是一个新的视觉问答循环。VLM 不维护地图——它依赖**实时视觉 + 常识推理**来做决策。 这最接近人类导航的方式：你不需要心里有精确的 2D 栅格地图，你只需要"看到前方是什么"就能决定下一步。
> 
> <div id="case8-3" class="section">
> 
> <div class="container">
> 
> ## 8-3 · 模型选型与部署方案
> 
> <div>
> 
> **① 案例含义**
> 
> 开源和商业 VLM 模型各有优劣。选型取决于你的**硬件算力**（Spark-I 的 i5-1240P 无独显 vs 是否有远程 GPU 服务器）、 **延迟要求**（实时导航需要 \<500ms 推理）和**费用预算**。
> 
> </div>
> 
> ### ② 模型对比
> 
> | 模型                      | 类型      | 参数量  | 推理速度 (CPU)               | 导航能力             | 硬件需求                          |
> | ----------------------- | ------- | ---- | ------------------------ | ---------------- | ----------------------------- |
> | **JanusVLN-7B** ⭐       | 开源      | \~8B | \~2s (GPU) / \~6s (INT8) | 双记忆导航，SOTA       | 10GB VRAM (INT8)，L40 单卡       |
> | **Qwen2-VL-2B**         | 开源      | 2B   | \~300ms (量化)             | 基础理解，可 fine-tune | 4GB RAM，CPU 可行                |
> | **LLaVA-1.6-7B**        | 开源      | 7B   | \~2s (CPU)               | 较强推理，需量化         | 8GB VRAM (GPU)，14GB RAM (CPU) |
> | **NaVid-4D**            | 研究 (复现) | \~1B | \~200ms (GPU)            | 专为导航优化           | 4GB VRAM                      |
> | **GPT-4V (API)**        | 商业 API  | 未公开  | \~500ms–2s (网络)          | 极强常识推理           | 仅需网络连接                        |
> | **Claude Vision (API)** | 商业 API  | 未公开  | \~300ms–1s (网络)          | 极强空间推理           | 仅需网络连接                        |
> | **Qwen2-VL-72B (API)**  | 商业/开源   | 72B  | \~2–5s (API)             | 最强综合能力           | 仅需网络连接                        |
> 

> <div class="dual-panel">
> 
> <div class="panel">
> 
> #### 🖥️ 方案 A：本地推理（Spark-I 离线运行）
> 
> **选型：**Qwen2-VL-2B 量化版 (INT8/INT4)  
> **优点：**无网络依赖、低延迟、数据不出设备  
> **缺点：**导航能力弱于大模型，可能在复杂场景出错  
> **适配：**使用 ONNX Runtime 或 llama.cpp 在 i5-1240P 上运行  
> **调优：**可以用 R2R 数据做少量 fine-tune 提升导航表现
> 
> </div>
> 
> <div class="panel">
> 
> #### ☁️ 方案 B：云端 API（机器人连 WiFi）
> 
> **选型：**GPT-4V 或 Claude Vision API  
> **优点：**最强推理能力，几乎不需要 fine-tune  
> **缺点：**依赖网络、有延迟波动、API 调用费用  
> **适配：**ROS 节点通过 HTTP/gRPC 调用 API  
> **适用场景：**研究原型验证、Demo、非实时任务
> 
> > 💡
> > 
> > <div class="tip-title">
> > 
> > 💡 推荐策略：本地 + 云端混合
> > 
> > 先用**方案 B（云端 API）快速验证** VLM 导航的可行性——用最聪明的模型看看你的场景是否能靠纯视觉+语言解决。 确认可行后，再考虑**方案 A 部署本地模型**以获得更低的延迟和更稳定的表现。  
> >   
> > Spark-I 的 i5-1240P 虽然无独显，但 16GB RAM + Intel Iris Xe 集成显卡可以跑 ONNX 量化模型。 Leo 如果有更强算力（或外接 GPU），选择余地更大。
> > 
> > <div id="case8-4" class="section">
> > 
> > <div class="container">
> > 
> > ## 8-4 · JanusVLN 云端直控真机 ★
> > 
> > <div>
> > 
> > **① 案例含义**
> > 
> > 7-6 在仿真里评估了 JanusVLN（SR=46.7%），但仿真不是现实。8-4 把同一个模型**部署到真实的 Spark-I 机器人上**， 用中文自然语言指令驱动它在办公室里导航——"去打印机前""去有显示器的桌子"。
> > 
> > **核心创新：**机器人本地没 GPU，通过 SSH 隧道把摄像头画面实时发给云端 L40， JanusVLN 推理后返回动作指令，形成一个 **"云端大脑 + 本地身体"** 的异构架构。
> > 
> > **前置条件：**Spark-I 机器人（ROS2 Humble）+ L40 云端 GPU（\>= 24GB 显存）+ 稳定网络。 需要安装 `bitsandbytes` 做 INT8 量化。
> > 
> > </div>
> > 
> > #### 云-边 VLN 推理架构
> > 
> > <div class="flow-box">
> > 
> > <div class="flow-step" style="border-top:3px solid #64748b;">
> > 
> > **① Spark-I 本地**
> > 
> > D435 摄像头拍照  
> > ROS2 vln\_client 节点
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #3b82f6;">
> > 
> > **② SSH 隧道**
> > 
> > 384px JPEG 编码  
> > localhost:18001→L40:8443
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #8b5cf6;">
> > 
> > **③ L40 推理**
> > 
> > JanusVLN INT8  
> > \~6-8s/步推理
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #f59e0b;">
> > 
> > **④ 返回动作**
> > 
> > MOVE\_FORWARD/TURN/STOP  
> > JSON HTTP 200
> > 
> > </div>
> > 
> > <div class="flow-arrow">
> > 
> > →
> > 
> > </div>
> > 
> > <div class="flow-step" style="border-top:3px solid #10b981;">
> > 
> > **⑤ 执行动作**
> > 
> > ROS2 Twist→底盘  
> > 连续运动不顿挫
> > 
> > ### ② L40 端：推理服务 (server.py)
> > 
> > <div>
> > 
> > **📦 模型加载 — 关键参数**
> > 
> > 直接加载 JanusVLN（\~10B 参数，BF16 精度）需要 **43GB 显存**，L40 总共 44GB。 加上推理时的 KV cache 和激活值——**第 8 步必然 OOM**。
> > 
> > </div>
> > 
> > #### 🔑 解决方案：INT8 量化
> > 
> > ``` 
> >     加载时加一行 load_in_8bit=True
> >     # BF16 — 43GB, 第8步OOM
> > model = Qwen2_5_VLForConditionalGenerationForJanusVLN.from_pretrained(
> >     MODEL_PATH,
> >     torch_dtype=torch.bfloat16,
> >     device_map="auto",
> > )
> > 
> > # INT8 — 10.6GB, 永不OOM
> > model = Qwen2_5_VLForConditionalGenerationForJanusVLN.from_pretrained(
> >     MODEL_PATH,
> >     load_in_8bit=True,
> >     device_map="auto",
> > )
> >   
> > ```
> > 
> > > 💡
> > > 
> > > <div class="tip-title">
> > > 
> > > 📊 实测对比
> > > 
> > > BF16：43GB / 第8步OOM / \~2-5s/步 · INT8：**10.6GB** / **永远不崩** / \~6-8s/步
> > > 
> > > </div>
> > > 
> > > #### 推理端点设计
> > > 
> > > ``` 
> > >     # POST /reset — 新任务开始
> > > {"session_id": "spark_001", "instruction": "去打印机前"}
> > > 
> > > # POST /step — 每步推理
> > > {"session_id": "spark_001", "image_base64": "...", "step_id": 5}
> > > 
> > > # 响应
> > > {"action": "MOVE_FORWARD", "step_id": 5, "raw_output": "move_forward"}
> > >   
> > > ```
> > > 
> > > > ⚠️
> > > > 
> > > > <div class="warn-title">
> > > > 
> > > > ⚠️ 两处防 OOM 的关键代码
> > > > 
> > > > **1. 限制历史帧数**：保持最近 10 帧历史图像，超出丢弃  
> > > > **2. 每步清理 KV cache**：推理后重置 past\_key\_values 并调用 torch.cuda.empty\_cache()  
> > > >   
> > > > 历史帧越多 → KV cache 越大 → 推理越慢 + 显存越紧。10 帧是平衡点。
> > > > 
> > > > </div>
> > > > 
> > > > ### ② Spark 端：客户端节点 (vln\_client.py)
> > > > 
> > > > | 模块         | 作用                     | 关键技术点                              |
> > > > | ---------- | ---------------------- | ---------------------------------- |
> > > > | **SSH 隧道** | 连接 L40 推理服务            | localhost:18001→L40:8443 端口映射      |
> > > > | **摄像头订阅**  | 接收 D435 彩色图像           | cv\_bridge 转 OpenCV，缩放至 384px 节省带宽 |
> > > > | **推理循环**   | 每步：拍照→HTTP POST→等回复→执行 | INT8 推理慢，http\_timeout 设 15s       |
> > > > | **防打转**    | 连续3次同向转弯→强制直行          | 零样本方向感弱时的兜底策略                      |
> > > > | **显示窗口**   | Spark 屏幕实时画面           | cv2.imshow + 动作叠加，DISPLAY=:0       |
> > > > 

> > > > #### 防打转逻辑
> > > > 
> > > > ``` 
> > > >     # JanusVLN 零样本方向感弱，容易连续输出转弯
> > > > # 兜底策略：检查连续同向转弯次数，>=3 则强制直行
> > > > if action in ("TURN_LEFT", "TURN_RIGHT"):
> > > >     if action == self._last_turn_dir:
> > > >         self._turn_count += 1
> > > >     else:
> > > >         self._turn_count = 1
> > > >     self._last_turn_dir = action
> > > >     if self._turn_count >= 3:
> > > >         action = "MOVE_FORWARD"      # 强制打破打转
> > > >         self._turn_count = 0
> > > >   
> > > > ```
> > > > 
> > > > ### ③ 启动命令
> > > > 
> > > > ``` 
> > > >     L40 端 — 启动推理服务
> > > > ```
> > > > 
> > > >     # 1. 安装 bitsandbytes（一次性）
> > > >     $ pip install bitsandbytes
> > > >     
> > > >     # 2. 修改 server.py：torch_dtype → load_in_8bit=True
> > > >     # 3. 后台启动
> > > >     $ nohup python server.py /tmp/srv.log 2>&1 &
> > > >     
> > > >     # 4. 验证
> > > >     $ curl http://localhost:8443/health
> > > >     {"status": "ok", "model_loaded": true}
> > > > 
> > > > ``` 
> > > >     Spark 端 — 启动导航
> > > > ```
> > > > 
> > > >     # 1. 清理僵尸进程（重要！否则 D435 断连）
> > > >     $ pkill -9 -f spark_base; pkill -9 -f realsense2_camera; pkill -9 -f vln_client
> > > >     
> > > >     # 2. 一键启动底盘+摄像头+VLN
> > > >     $ ros2 launch spark_vln vln_bringup.launch.py
> > > >     
> > > >     # 3. 设置指令（ROS2 param，支持中文）
> > > >     $ ros2 param set /vln_client instruction "去打印机前"
> > > >     
> > > >     # 4. 启动导航
> > > >     $ ros2 service call /vln/start std_srvs/srv/Trigger
> > > > 
> > > > ### ④ 实测数据
> > > > 
> > > > <div>
> > > > 
> > > > **📊 "去打印机前" — 19步完整记录（INT8）**
> > > > 
> > > > <div style="font-size:0.82em;font-family:monospace;line-height:1.8;margin-top:8px;">
> > > > 
> > > > Step 1-6: TURN\_LEFT/TURN\_RIGHT 交替扫描（找打印机）  
> > > > <span style="color:#4ade80;">Step 7: MOVE\_FORWARD</span> ← 找到了！  
> > > > Step 8-9: TURN\_LEFT/TURN\_RIGHT（微调方向）  
> > > > <span style="color:#4ade80;">Step 10: MOVE\_FORWARD</span>  
> > > > <span style="color:#4ade80;">Step 12: MOVE\_FORWARD</span>  
> > > > Step 13-14: TURN\_LEFT（调整方向）  
> > > > <span style="color:#4ade80;">Step 15: MOVE\_FORWARD</span> ← 第三次自主前进  
> > > > <span style="color:#4ade80;">Step 16: MOVE\_FORWARD</span>  
> > > > Step 17-19: TURN\_LEFT/RIGHT
> > > > 
> > > > </div>
> > > > 
> > > > ✅ **3 次自主 MOVE\_FORWARD，零次防打转触发**——机器人交替扫描→锁定目标→前进，行为合理。  
> > > > ✅ 19 步零 OOM，零 HTTP 500。显存稳定在 10.9GB。
> > > > 
> > > > </div>
> > > > 
> > > > | 指标         | BF16          | INT8     |
> > > > | ---------- | ------------- | -------- |
> > > > | **显存占用**   | 43 GB         | 10.6 GB  |
> > > > | **稳定性**    | 第8步必崩         | 永不崩      |
> > > > | **推理速度**   | \~2-5s/步      | \~6-8s/步 |
> > > > | **自主前进次数** | 0 次（7步纯转后OOM） | 3 次（19步） |
> > > > | **防打转触发**  | 2 次           | 0 次      |
> > > > 

> > > > ### ⑤ 输出结果的含义
> > > > 
> > > > <div>
> > > > 
> > > > **每步日志解读**
> > > > 
> > > > `[vln_client] Step 7: MOVE_FORWARD (move_forward)`  
> > > > → 模型认为当前方向接近目标，建议前进 0.2m/s  
> > > >   
> > > > `[vln_client] Step 8: TURN_RIGHT`  
> > > > → 模型发现目标偏右，建议右转 0.5rad/s  
> > > >   
> > > > `[WARN] Anti-spin: 3 consecutive TURN_LEFT, forcing MOVE_FORWARD`  
> > > > → 连续3次同向转弯，防打转机制介入——模型可能在犹豫，强制直行打破僵局  
> > > >   
> > > > `[INFO] Goal reached (STOP)`  
> > > > → 模型判定已到达目标，输出 STOP，导航结束
> > > > 
> > > > </div>
> > > > 
> > > > ### ⑥ 试试调整这些
> > > > 
> > > > | 调整项              | 怎么改                                       | 预期看到什么                      |
> > > > | ---------------- | ----------------------------------------- | --------------------------- |
> > > > | **history 帧数**   | `server.py` 中改 `10` → `5` 或 `20`          | 5帧=推理更快但容易迷路；20帧=更稳但更慢      |
> > > > | **HTTP timeout** | `vln_client.py` 中 `http_timeout`（默认 15s）  | INT8 推理 6-8s，设 \< 10s 会误报超时 |
> > > > | **防打转阈值**        | `self._turn_count >= 3` 改 `2` 或 `5`       | 2=更激进打断转弯；5=更容忍原地扫描         |
> > > > | **图像分辨率**        | `max_size = 384` 改 `256` 或 `512`          | 256=更快但识别率降；512=更准但推理更慢     |
> > > > | **量化精度**         | `load_in_8bit=True` → `load_in_4bit=True` | 4bit=\~6GB显存，推理更快但质量可能微降    |
> > > > | **线/角速度**        | `linear_speed=0.2, angular_speed=0.5`     | 0.3/0.8=更快但更抖；0.1/0.3=更稳但更慢 |
> > > > 

> > > > > 💡
> > > > > 
> > > > > <div class="tip-title">
> > > > > 
> > > > > 💡 下一步 — 真机采集 + LoRA 微调
> > > > > 
> > > > > 零样本的局限性：模型不认识你的办公室布局。想让 JanusVLN 真正理解"会议室""饮水机""打印机"的具体位置， 需要用 Spark 录制真实路径数据（[8-6 rosbag](#case8-6)）→ 标注中文指令 → [8-7 LoRA 微调](#case8-7)。
> > > > > 
> > > > > <div id="case8-5" class="section">
> > > > > 
> > > > > <div class="container">
> > > > > 
> > > > > ## 8-5 · 仿真与真机测试计划
> > > > > 
> > > > > <div>
> > > > > 
> > > > > **① 案例含义**
> > > > > 
> > > > > 直接上真机风险大（撞墙、电机过载）。8-5 设计了两阶段测试计划：先在 **Gazebo 仿真** 中验证完整链路， 再上 **Spark-I 真机**。每阶段都有明确的 Pass/Fail 条件。
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ② Phase 1：Gazebo 仿真测试
> > > > > 
> > > > > **环境：**Spark-I Gazebo 仿真 + TurtleBot3 世界
> > > > > 
> > > > > | \#     | 测试项        | 操作                                    | 预期            | Pass 条件                         |
> > > > > | ------ | ---------- | ------------------------------------- | ------------- | ------------------------------- |
> > > > > | **T1** | 通信链路       | 真机端启动 image\_bridge → curl 云端 /health | 200 OK        | 3/3 请求成功                        |
> > > > > | **T2** | 单步推理       | 发一张仿真 RGB + "Go to the door"          | 返回一个有效动作      | 动作在 {FORWARD,LEFT,RIGHT,STOP} 内 |
> > > > > | **T3** | 动作映射       | FORWARD → /cmd\_vel 发布 → 检查移动         | 机器人向前移动 0.25m | 里程计位移 \> 0.2m，角度偏差 \< 5°        |
> > > > > | **T4** | 端到端单步执行    | 云端返回 FORWARD → 真机执行 0.25m             | 机器人直行 0.25m   | 里程计位移在 0.2–0.3m 之间              |
> > > > > | **T5** | 多步导航       | 连续 10 步 拍照→推理→执行 循环                   | 每步正确执行        | 10/10 步无卡死、无超时                  |
> > > > > | **T6** | 完整 episode | 发指令 → 自动运行直到 STOP                     | 机器人停在目标附近     | 最终位置距 ground-truth goal \< 2m   |
> > > > > | **T7** | 异常恢复       | 推理超时 / 网络断开 → 观察行为                    | 安全停止，不发无效指令   | 机器人不失控移动                        |
> > > > > 

> > > > > ``` 
> > > > >     复制
> > > > >     # 仿真启动顺序
> > > > > # 终端 1: 启动 Gazebo 仿真世界
> > > > > $ ros2 launch spark_bringup gazebo.launch.py world:=turtlebot3_world
> > > > > 
> > > > > # 终端 2: 启动 VLN 客户端（端到端）
> > > > > $ ros2 launch spark_vln vln_bringup.launch.py
> > > > > 
> > > > > # 终端 3 (云端): 启动推理服务
> > > > > $ ssh L40 'nohup python server.py &/tmp/srv.log 2>&1 &'
> > > > > 
> > > > > # 发送指令 → 开始导航
> > > > > $ ros2 param set /vln_client instruction "去门口停下"
> > > > > $ ros2 service call /vln/start std_srvs/srv/Trigger
> > > > > ```
> > > > > 
> > > > > </div>
> > > > > 
> > > > > ### ③ Phase 2：Spark-I 真机测试
> > > > > 
> > > > > **前置：**Phase 1 全部 T1-T7 Pass + 机器人硬件检查
> > > > > 
> > > > > | \#      | 测试项       | 特殊注意事项                    | Pass 条件               |
> > > > > | ------- | --------- | ------------------------- | --------------------- |
> > > > > | **T8**  | 相机标定验证    | 真机 RGB 尺寸/视场角与仿真不同        | 图像 resize 后送入模型无报错    |
> > > > > | **T9**  | 坐标系对齐     | 端到端输出 /cmd\_vel 是机器人坐标系   | rviz 中移动方向与实际一致       |
> > > > > | **T10** | 实景单步导航    | 真机有里程计漂移，Nav2 需实时修正       | 单步到达误差 \< 0.15m       |
> > > > > | **T11** | 动态障碍物     | 人在机器人前方走过 → Nav2 应避障      | 机器人减速/绕行，不撞人          |
> > > > > | **T12** | 10 条指令测试集 | 在办公室环境中预设 10 条导航指令        | SR ≥ 40%（10 条中 4+ 成功） |
> > > > > | **T13** | 紧急停止      | 物理急停按钮或 /vln/stop service | 电机立即断电，\< 0.5s 响应     |
> > > > > 

> > > > > > ⚠️
> > > > > > 
> > > > > > <div class="warn-title">
> > > > > > 
> > > > > > ⚠️ 真机测试安全守则
> > > > > > 
> > > > > > 1\. 首次测试用**最低速度**（0.1 m/s），逐步提高  
> > > > > > 2\. 旁边始终有人手持**急停遥控器**  
> > > > > > 3\. 测试区域**清空行人**，地面无杂物  
> > > > > > 4\. 先测试 STOP 指令（验证急停链路），再测移动  
> > > > > > 5\. 录 rosbag，失败后可回放分析
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ④ 测试记录模板
> > > > > > 
> > > > > > | 测试ID   | 日期    | 环境     | 指令                       | 结果 | 耗时  | 失败原因           |
> > > > > > | ------ | ----- | ------ | ------------------------ | -- | --- | -------------- |
> > > > > > | T6-01  | 06-18 | Gazebo | Go to the door           | ✅  | 32s | —              |
> > > > > > | T6-02  | 06-18 | Gazebo | Go to kitchen, turn left | ❌  | —   | Nav2 规划失败（无地图） |
> > > > > > | T12-01 | —     | 真机     | 走到门口停下                   | —  | —   | 待测试            |
> > > > > > 

> > > > > > <div id="case8-6" class="section">
> > > > > > 
> > > > > > <div class="container">
> > > > > > 
> > > > > > ## 8-6 · 真机采集与数据处理
> > > > > > 
> > > > > > <div>
> > > > > > 
> > > > > > **① 案例含义**
> > > > > > 
> > > > > > 要让 JanusVLN 真正理解"会议室""饮水机""打印机"的具体位置，需要采集真实办公室的导航数据。本案例涵盖三种采集方式（仿真自动、真机手动、混合策略），以及数据格式规范和质量检查清单。
> > > > > > 
> > > > > > **前置条件：**已完成 [8-4 零样本直控](#case8-4)，确认 Spark-I 底盘+摄像头可用。采集的数据将用于 [8-7 LoRA 微调](#case8-7)。
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ② 三种采集方式对比
> > > > > > 
> > > > > > | 方式            | 工具                             | 单条耗时   | 优点         | 缺点        |
> > > > > > | ------------- | ------------------------------ | ------ | ---------- | --------- |
> > > > > > | **A. 仿真自动采集** | Habitat + ShortestPathFollower | \~10 秒 | 快速、安全、可批量  | 图像与真机有分布差 |
> > > > > > | **B. 真机手动录制** | Spark-I + rosbag               | \~5 分钟 | 真实相机/光照/动态 | 慢、需人工操作   |
> > > > > > | **C. 混合策略**   | 仿真 80% + 真机 20%                | —      | 兼得速度与真实感   | 需对齐两种数据格式 |
> > > > > > 

> > > > > > ### ③ 方式 A：仿真自动采集
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # collect_training_data.py — 在 Habitat 中自动采集导航轨迹
> > > > > > import habitat, json, gzip, numpy as np
> > > > > > from habitat.tasks.nav.shortest_path_follower import ShortestPathFollower
> > > > > > 
> > > > > > env = habitat.Env(config=habitat.get_config("benchmark/nav/vln/vln_r2r.yaml"))
> > > > > > follower = ShortestPathFollower(env.sim, goal_radius=1.8, return_one_hot=False)
> > > > > > 
> > > > > > dataset = []
> > > > > > for ep_id, episode in enumerate(env.episodes):
> > > > > >     obs = env.reset()
> > > > > >     episode_data = {
> > > > > >         "episode_id": ep_id,
> > > > > >         "scene_id": episode.scene_id,
> > > > > >         "start_position": episode.start_position.tolist(),
> > > > > >         "start_rotation": episode.start_rotation.tolist(),
> > > > > >         "goals": [{"position": g.position.tolist()} for g in episode.goals],
> > > > > >         "reference_path": [p.tolist() for p in episode.reference_path],
> > > > > >         "rgb_frames": [],        # 每步的 RGB 图像
> > > > > >         "actions": [],            # 每步的专家动作
> > > > > >         "instruction": ""        # 人工标注（采集后填）
> > > > > >     }
> > > > > > 
> > > > > >     while not env.episode_over:
> > > > > >         episode_data["rgb_frames"].append(obs["rgb"].copy())
> > > > > >         action = follower.get_next_action(episode.reference_path)
> > > > > >         episode_data["actions"].append(action)
> > > > > >         obs = env.step(action)
> > > > > > 
> > > > > >     dataset.append(episode_data)
> > > > > > 
> > > > > > # 保存（不含 RGB 图片——图片单独存为 PNG 以节省 JSON 体积）
> > > > > > with gzip.open("my_scene_train.json.gz", "wt") as f:
> > > > > >     json.dump({"episodes": dataset}, f, default=str)
> > > > > > ```
> > > > > > 
> > > > > > </div>
> > > > > > 
> > > > > > ### ④ 方式 B：真机手动录制（rosbag）
> > > > > > 
> > > > > > ``` 
> > > > > >     复制
> > > > > >     # 真机采集流程（Spark-I + ROS 2）
> > > > > > 
> > > > > > # Step 1: 录 rosbag（遥控机器人走一遍路径）
> > > > > > $ ros2 bag record /camera/color/image_raw /odom /tf /tf_static \
> > > > > >     -o my_nav_path_01
> > > > > > 
> > > > > > # Step 2: 从 rosbag 提取位姿序列 → reference_path
> > > > > > $ python3 extract_poses_from_bag.py my_nav_path_01/
> > > > > > 
> > > > > > # Step 3: 人工标注指令（对着视频写）
> > > > > > #   示例："从实验室门口出发，经过机械臂工位，走到3D打印区停下"
> > > > > > 
> > > > > > # Step 4: 重复 30-50 条 → 开始微调
> > > > > > ```
> > > > > > 
> > > > > > ### ⑤ 数据质量检查清单
> > > > > > 
> > > > > > <table>
> > > > > > <colgroup>
> > > > > > <col style="width: 33%" />
> > > > > > <col style="width: 33%" />
> > > > > > <col style="width: 33%" />
> > > > > > </colgroup>
> > > > > > <thead>
> > > > > > <tr class="header">
> > > > > > <th>维度</th>
> > > > > > <th>✅ 正确做法</th>
> > > > > > <th>❌ 常见错误</th>
> > > > > > </tr>
> > > > > > </thead>
> > > > > > <tbody>
> > > > > > <tr class="odd">
> > > > > > <td><strong>路径多样性</strong></td>
> > > > > > <td>包含最短路径 + 偏离路径（70:30）</td>
> > > > > > <td>只有最短路径 → 模型没见过走错的样子</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>指令语言</strong></td>
> > > > > > <td>日常口语："走到白板前"<br />
> > > > > > 同路径 2-3 种说法</td>
> > > > > > <td>"前进 5 米，左转 30 度"→ 不是 VLN</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>光照覆盖</strong></td>
> > > > > > <td>早/中/晚各采一批</td>
> > > > > > <td>只在下午 3 点采 → 早上模型就瞎了</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>视角覆盖</strong></td>
> > > > > > <td>路径偏左/偏右/正中各一些</td>
> > > > > > <td>全都走正中间</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>动态物体</strong></td>
> > > > > > <td>有行人 / 无行人各一半</td>
> > > > > > <td>全是空房间 → 真机一有人就乱</td>
> > > > > > </tr>
> > > > > > <tr class="even">
> > > > > > <td><strong>距离梯度</strong></td>
> > > > > > <td>3m / 5m / 10m / 20m 均匀分布</td>
> > > > > > <td>全是 5m 以内的短距离</td>
> > > > > > </tr>
> > > > > > <tr class="odd">
> > > > > > <td><strong>中英对应</strong></td>
> > > > > > <td>JanusVLN 用英文：中文翻译为英文<br />
> > > > > > 或用英文直接标注</td>
> > > > > > <td>中文直接喂给英文训练的模型</td>
> > > > > > </tr>
> > > > > > </tbody>
> > > > > > </table>
> > > > > > 
> > > > > > ### ⑥ 最小可行数据集
> > > > > > 
> > > > > > | 场景规模  | 最少条数   | 采集时间     | 预期 SR（微调后） |
> > > > > > | ----- | ------ | -------- | ---------- |
> > > > > > | 单个房间  | 30 条   | 1 小时（仿真） | \~55%      |
> > > > > > | 一层办公楼 | 100 条  | 3 小时（仿真） | \~65%      |
> > > > > > | 整栋建筑  | 300+ 条 | 1 天（仿真）  | \~70%      |
> > > > > > 

> > > > > > > ⚠️
> > > > > > > 
> > > > > > > <div class="warn-title">
> > > > > > > 
> > > > > > > ⚠️ 数据准备详见 [8-6 真机采集与数据处理](#case8-6)
> > > > > > > 
> > > > > > > 30 条高质量数据（路径多样 + 指令自然 + 光照覆盖）比 200 条劣质数据有效得多。 劣质数据的典型信号：微调后 SR 反而下降 → 说明数据引入了噪声而非信号。 如果时间有限，宁可花 80% 时间打磨 30 条数据，不要赶工产 100 条。
> > > > > > > 
> > > > > > > </div>
> > > > > > > 
> > > > > > > > 💡
> > > > > > > > 
> > > > > > > > <div class="tip-title">
> > > > > > > > 
> > > > > > > > 💡 下一步：LoRA 微调
> > > > > > > > 
> > > > > > > > 数据准备好后，进入 [8-7 LoRA 微调 JanusVLN](#case8-7)，将采集的数据用于适配新场景。
> > > > > > > > 
> > > > > > > > <div id="case8-7" class="section">
> > > > > > > > 
> > > > > > > > <div class="container">
> > > > > > > > 
> > > > > > > > ## 8-7 · LoRA 微调 JanusVLN
> > > > > > > > 
> > > > > > > > <div>
> > > > > > > > 
> > > > > > > > **① 案例含义**
> > > > > > > > 
> > > > > > > > [7-6](habitat-textbook-step7.html#case7-6) 和 [8-4](#case8-4) 展示了 JanusVLN 的零样本能力。如果想在**自己的场景**上提升性能—— 比如办公室、工厂、家庭——就需要微调。8-7 介绍三种微调方案及其硬件需求。
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > ### ② 三种微调方案
> > > > > > > > 
> > > > > > > > | 方案                  | 原理                    | 显存需求         | L40 可行？  | 适用场景                |
> > > > > > > > | ------------------- | --------------------- | ------------ | -------- | ------------------- |
> > > > > > > > | **A. 分组件微调**        | 冻结视觉编码器，只训练 LLM + 投影层 | \~60 GB（8 卡） | ❌        | JanusVLN 原版训练方式     |
> > > > > > > > | **B. LoRA 微调**      | 冻结全部权重，插入少量可训练的秩分解矩阵  | \~30 GB（单卡）  | **✅ 可行** | JanusVLN 适配新场景，最低成本 |
> > > > > > > > | **C. Seq2Seq 全量微调** | 2700 万参数全部训练          | \~8 GB（单卡）   | ✅        | 我们的小模型在新数据上微调       |
> > > > > > > > 

> > > > > > > > > ⚠️
> > > > > > > > > 
> > > > > > > > > <div class="warn-title">
> > > > > > > > > 
> > > > > > > > > ⚠️ 为什么方案 A 需要 8 卡
> > > > > > > > > 
> > > > > > > > > 方案 A 训练 LLM 全部 70 亿参数 + 投影层，即使用 DeepSpeed ZeRO-3 分片也需要 8 卡。 L40 单卡 46GB 只够推理，不够训练。但 **方案 B（LoRA）在原代码基础上只需加 \~30 行**， 就能在单卡上微调 JanusVLN。
> > > > > > > > > 
> > > > > > > > > </div>
> > > > > > > > > 
> > > > > > > > > ### ③ LoRA 原理解析
> > > > > > > > > 
> > > > > > > > > LoRA（Low-Rank Adaptation）不修改原始权重 **W**，而是在旁边插入两个小矩阵 **A 和 B**：
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 标准全量微调：修改 W 的全部 4096×4096 = 16M 参数
> > > > > > > > > h = W @ x + b          # W 可训练，16M 参数
> > > > > > > > > 
> > > > > > > > > # LoRA 微调：W 冻结，只训练 A 和 B
> > > > > > > > > h = W @ x + b + (B @ A) @ x   # W 冻结，A+B 共 4096×16×2 = 131K 参数
> > > > > > > > > #                  ↑ 秩 r=16，可训练参数减少 120 倍
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > | 对比     | 全量微调     | LoRA (r=16)    |
> > > > > > > > > | ------ | -------- | -------------- |
> > > > > > > > > | 可训练参数  | \~80 亿   | \~4000 万（0.5%） |
> > > > > > > > > | 显存（训练） | \~120 GB | \~30 GB        |
> > > > > > > > > | 训练速度   | 基准       | 快 1.5-2×       |
> > > > > > > > > | 推理开销   | 无        | 可合并回 W（无额外开销）  |
> > > > > > > > > | 性能     | 最佳       | 通常持平，差距 \<2%   |
> > > > > > > > > 

> > > > > > > > > ### ④ LoRA 微调 JanusVLN（L40 单卡）
> > > > > > > > > 
> > > > > > > > > **Step 1 — 安装 peft**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     pip install peft -i https://pypi.doubanio.com/simple
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 2 — 修改 train\_qwen.py，在模型加载后插入 LoRA**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     from peft import LoraConfig, get_peft_model, TaskType
> > > > > > > > > 
> > > > > > > > > # 在模型加载完成后，添加：
> > > > > > > > > lora_config = LoraConfig(
> > > > > > > > >     r=16,                          # LoRA 秩（越大效果越好，显存越多）
> > > > > > > > >     lora_alpha=32,                 # 缩放因子
> > > > > > > > >     target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
> > > > > > > > >     lora_dropout=0.05,
> > > > > > > > >     bias="none",
> > > > > > > > >     task_type=TaskType.CAUSAL_LM,
> > > > > > > > > )
> > > > > > > > > model = get_peft_model(model, lora_config)
> > > > > > > > > model.print_trainable_parameters()
> > > > > > > > > # 输出: trainable params: 41,943,040 || all params: 8,294,967,296 || trainable%: 0.506%
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 3 — 冻结 VGGT + 视觉编码器（节省更多显存）**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 冻结 VGGT（3D 特征提取器——通用能力，不需要微调）
> > > > > > > > > for param in model.vggt.parameters():
> > > > > > > > >     param.requires_grad = False
> > > > > > > > > 
> > > > > > > > > # 冻结视觉编码器（Qwen2.5-VL 的视觉 tower）
> > > > > > > > > for param in model.visual.parameters():
> > > > > > > > >     param.requires_grad = False
> > > > > > > > > 
> > > > > > > > > # 只训练：LoRA adapter + 投影层 (merger) + token embedding
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > **Step 4 — 单卡训练命令（移除 DeepSpeed）**
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 原版需要 8 卡 + DeepSpeed，LoRA 版本单卡即可
> > > > > > > > > python src/qwen_vl/train/train_qwen.py \
> > > > > > > > >     --model_name_or_path ./weights/misstl/JanusVLN_Base \
> > > > > > > > >     --vggt_model_path facebook/VGGT-1B \
> > > > > > > > >     --tune_mm_llm True \
> > > > > > > > >     --tune_mm_vision False \
> > > > > > > > >     --tune_mm_mlp True \
> > > > > > > > >     --use_lora True \
> > > > > > > > >     --lora_r 16 \
> > > > > > > > >     --dataset_use train_r2r \
> > > > > > > > >     --output_dir ./JanusVLN_LoRA_Office \
> > > > > > > > >     --bf16 \
> > > > > > > > >     --per_device_train_batch_size 1 \
> > > > > > > > >     --gradient_accumulation_steps 16 \
> > > > > > > > >     --learning_rate 1e-4 \
> > > > > > > > >     --num_train_epochs 3 \
> > > > > > > > >     --save_steps 500 \
> > > > > > > > >     --max_pixels $((576*28*28)) \               # 降低分辨率省显存
> > > > > > > > >     --gradient_checkpointing                     # 用时间换显存
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > ### ⑤ 微调数据准备
> > > > > > > > > 
> > > > > > > > > 需要把自己的场景做成 R2R 格式的 JSON：
> > > > > > > > > 
> > > > > > > > > ``` 
> > > > > > > > >     复制
> > > > > > > > >     # 每条训练数据 = 一个 navigation episode
> > > > > > > > > {
> > > > > > > > >   "episodes": [
> > > > > > > > >     {
> > > > > > > > >       "episode_id": 1,
> > > > > > > > >       "scene_id": "mp3d/my_office/my_office.glb",
> > > > > > > > >       "start_position": [0, 0, 0],
> > > > > > > > >       "start_rotation": [0, 0.923, 0, 0.382],
> > > > > > > > >       "goals": [{"position": [5.2, 0, -3.1]}],
> > > > > > > > >       "reference_path": [[0,0,0], [0.5,0,0], ..., [5.2,0,-3.1]],
> > > > > > > > >       "instruction": {
> > > > > > > > >         "instruction_text": "Walk to the whiteboard and stop"
> > > > > > > > >       }
> > > > > > > > >     }
> > > > > > > > >   ],
> > > > > > > > >   "instruction_vocab": {...}  # 复用 R2R 原始词表
> > > > > > > > > }
> > > > > > > > > ```
> > > > > > > > > 
> > > > > > > > > | 场景来源          | 数据制作方式                                             | 最少条数     |
> > > > > > > > > | ------------- | -------------------------------------------------- | -------- |
> > > > > > > > > | Habitat 仿真新场景 | 用 ShortestPathFollower 自动生成 reference\_path，人工标注指令 | 50-100 条 |
> > > > > > > > > | 真机录制的轨迹       | SLAM 记录位姿序列 → 转成 reference\_path，人工标注指令            | 30-50 条  |
> > > > > > > > > | 现有 R2R 子集     | 从 R2R 训练集中筛选与目标场景相似的 episode                       | 200+ 条   |
> > > > > > > > > 

> > > > > > > > > ### ⑥ 微调完整流程
> > > > > > > > > 
> > > > > > > > > | 步骤             | 操作                                          | 预计时间   |
> > > > > > > > > | -------------- | ------------------------------------------- | ------ |
> > > > > > > > > | **1. 数据采集**    | 在新场景中收集 50-200 条导航指令+轨迹                     | 2-4 小时 |
> > > > > > > > > | **2. 格式转换**    | 转为 R2R JSON + gzip 压缩                       | 30 分钟  |
> > > > > > > > > | **3. LoRA 训练** | L40 单卡，3 epoch，batch\_size=1，grad\_accum=16 | 4-8 小时 |
> > > > > > > > > | **4. 合并权重**    | `model.merge_and_unload()` → LoRA 合并回原始权重   | 1 分钟   |
> > > > > > > > > | **5. 评估**      | 在新场景的 val split 上跑 eval，对比微调前后              | 30 分钟  |
> > > > > > > > > 

> > > > > > > > > > ⚠️
> > > > > > > > > > 
> > > > > > > > > > <div class="warn-title">
> > > > > > > > > > 
> > > > > > > > > > 💡 微调预期效果
> > > > > > > > > > 
> > > > > > > > > > 在 R2R 上零样本 SR=46.7%。如果用自己的 50-100 条数据进行 LoRA 微调：  
> > > > > > > > > > • **同场景 SR：**预期提升到 60-75%（模型"记住"了你的环境）  
> > > > > > > > > > • **跨场景泛化：**可能轻微下降（LoRA 的灾难性遗忘），需要混合原始 R2R 数据  
> > > > > > > > > > • **训练技巧：**前 1 epoch 混合 70% R2R + 30% 新数据，后 2 epoch 只用新数据
> > > > > > > > > > 
> > > > > > > > > > </div>
> > > > > > > > > > 
> > > > > > > > > > ### ⑦ 方案 C：微调我们自己的 Seq2Seq
> > > > > > > > > > 
> > > > > > > > > > 如果我们不想用 JanusVLN（硬件要求高），也可以微调自己在 §N 训练的 2700 万参数模型：
> > > > > > > > > > 
> > > > > > > > > > ``` 
> > > > > > > > > >     复制
> > > > > > > > > >     # 加载 §N 训练的 checkpoint
> > > > > > > > > > model = Seq2SeqAgent(embed_dim=300, hidden_dim=512)
> > > > > > > > > > model.load_state_dict(torch.load('ckpt/seq2seq_best.pth'))
> > > > > > > > > > 
> > > > > > > > > > # 在新数据上全量微调（27M 参数全部可训练）
> > > > > > > > > > optimizer = AdamW(model.parameters(), lr=1e-4)
> > > > > > > > > > for epoch in range(5):
> > > > > > > > > >     for rgb, instruction, action_gt in new_dataloader:
> > > > > > > > > >         pred = model(rgb, instruction)
> > > > > > > > > >         loss = CrossEntropyLoss(pred, action_gt)
> > > > > > > > > >         loss.backward()
> > > > > > > > > >         optimizer.step()
> > > > > > > > > > 
> > > > > > > > > > # 优点：快（10 分钟训完）、省显存（8GB）、可跑 DAgger
> > > > > > > > > > # 缺点：模型上限低（没有 VLM 的世界知识）
> > > > > > > > > > ```
> > > > > > > > > > 
> > > > > > > > > > | 对比            | Seq2Seq 微调  | JanusVLN LoRA  |
> > > > > > > > > > | ------------- | ----------- | -------------- |
> > > > > > > > > > | 显存            | \~8 GB      | \~30 GB        |
> > > > > > > > > > | 训练时间（100 条数据） | \~10 分钟     | \~4 小时         |
> > > > > > > > > > | SR 上限         | \~40-50%    | \~60-75%       |
> > > > > > > > > > | 适合场景          | 快速原型，验证数据质量 | 最终部署，追求性能      |
> > > > > > > > > > | 可做 DAgger     | ✅ 轻量，训练快    | ⚠️ 每轮 4 小时，迭代慢 |
> > > > > > > > > > 

> > > > > > > > > > > 💡
> > > > > > > > > > > 
> > > > > > > > > > > <div class="tip-title">
> > > > > > > > > > > 
> > > > > > > > > > > 💡 推荐策略：两级微调
> > > > > > > > > > > 
> > > > > > > > > > > **第一级：**用 Seq2Seq 在新数据上快速微调（10 分钟），验证数据质量和任务可行性  
> > > > > > > > > > > **第二级：**确认数据没问题后，用 JanusVLN LoRA 做正式微调（4-8 小时），拿到最优 SR  
> > > > > > > > > > > 这样避免了"花 4 小时训练发现数据有 bug"的情况。
> > > > > > > > > > > 
> > > > > > > > > > > <div id="case8-8" class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 8-8 · 两种方法全面对比
> > > > > > > > > > > 
> > > > > > > > > > > <div>
> > > > > > > > > > > 
> > > > > > > > > > > **① 对比维度**
> > > > > > > > > > > 
> > > > > > > > > > > 以下是方法一（VLN + ROS Nav2）和方法二（VLM 端到端）在 12 个关键维度上的并列对比。
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > | 维度               | 方法一：VLN + ROS Nav2              | 方法二：VLM 端到端                  |
> > > > > > > > > > > | ---------------- | ------------------------------- | ---------------------------- |
> > > > > > > > > > > | **是否需要地图**       | ✅ 需要预建 2D 占据栅格地图                | ❌ 不需要任何地图                    |
> > > > > > > > > > > | **是否需要 ROS 导航栈** | ✅ 需要 move\_base / Nav2          | ❌ 直接输出 /cmd\_vel             |
> > > > > > > > > > > | **对新环境的适应**      | 需要重新建图（15-30min）                | 即开即用（但可能在陌生环境退化）             |
> > > > > > > > > > > | **避障能力**         | ✅ Nav2 成熟避障（全局+局部）              | ⚠️ 依赖 VLM 的视觉判断 + 安全屏障       |
> > > > > > > > > > > | **路径最优性**        | ✅ 全局最优路径（A\*/Dijkstra）          | ❌ 局部贪心，可能绕路                  |
> > > > > > > > > > > | **计算资源**         | 中等（CPU 跑 Nav2 + VLN 推理）         | 高（需要 GPU 或云 API，大模型推理）       |
> > > > > > > > > > > | **网络依赖**         | 无（全本地）                          | 用云端 API 时有，本地模型则无            |
> > > > > > > > > > > | **延迟**           | 低（Nav2 规划 \~50ms + VLN \~100ms） | 中等–高（云端 0.5–2s，本地量化 \~300ms） |
> > > > > > > > > > > | **语言理解粒度**       | 受 VLN 模型限制（数据集固定模板）             | ✅ 极强（理解任意自然语言）               |
> > > > > > > > > > > | **代码复杂度**        | 5 个节点，3 种通信模式                   | 1 个核心节点，极简                   |
> > > > > > > > > > > | **系统工程成熟度**      | ✅ 高（Nav2 经过多年验证）                | ⚠️ 低（VLM 导航仍在快速发展中）          |
> > > > > > > > > > > | **最适合的场景**       | 固定环境、频繁使用、稳定性优先                 | 新环境探索、研究原型、Demo              |
> > > > > > > > > > > 

> > > > > > > > > > > <div class="highlight-box">
> > > > > > > > > > > 
> > > > > > > > > > > #### 🎯 决策指南
> > > > > > > > > > > 
> > > > > > > > > > > **选方法一，如果：**  
> > > > > > > > > > > • 你的工作场景是固定的（办公室/家庭楼层布局不变）  
> > > > > > > > > > > • 你重视安全性和路径最优性  
> > > > > > > > > > > • 你的团队有 ROS 经验  
> > > > > > > > > > > • 你需要在 Spark-I / Leo 上低延迟运行  
> > > > > > > > > > >   
> > > > > > > > > > > **选方法二，如果：**  
> > > > > > > > > > > • 你需要快速验证 VLN 的概念而不想配置导航栈  
> > > > > > > > > > > • 你的使用场景不固定（多变的临时环境）  
> > > > > > > > > > > • 你更偏向 CV/ML 背景而非 ROS 背景  
> > > > > > > > > > > • 你可以接受较高的 API 费用和网络延迟  
> > > > > > > > > > > • 你想探索最前沿的 VLM 能力边界  
> > > > > > > > > > >   
> > > > > > > > > > > **最优方案：两者结合。**用方法二做**全局语义规划**（VLM 看全景图 → "先去厨房，再去卧室"）， 用方法一做**局部路径执行**（Nav2 负责每个段落的安全导航）。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="section">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="container">
> > > > > > > > > > > 
> > > > > > > > > > > ## 部署轨全总结
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module-grid">
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-vlm);">
> > > > > > > > > > > 
> > > > > > > > > > > ### ✅ 完成本章后你应该能
> > > > > > > > > > > 
> > > > > > > > > > >   - 设计云-边-端 VLN 推理架构
> > > > > > > > > > >   - 解释 VLM 导航和传统 VLN 的本质区别
> > > > > > > > > > >   - 根据硬件条件选择合适的 VLM 方案并配置 INT8 量化
> > > > > > > > > > >   - 在真机上部署 JanusVLN 零样本直控，理解防打转策略
> > > > > > > > > > >   - 制定仿真与真机的分层测试计划
> > > > > > > > > > >   - 用 ros2 bag 录制导航数据供后续微调
> > > > > > > > > > >   - 使用 LoRA 在单卡上微调 JanusVLN 适配新场景
> > > > > > > > > > >   - 在 12 个维度上对比两种方法并做出选型决策
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > <div class="module" style="border-left-color: var(--accent-tip);">
> > > > > > > > > > > 
> > > > > > > > > > > ### 🎓 部署轨学习路径回顾
> > > > > > > > > > > 
> > > > > > > > > > > [第6章](habitat-textbook-step6.html) → RL 训练入门  
> > > > > > > > > > > [第7章](habitat-textbook-step7.html) → VLN 仿真训练（配置→训练→评估→诊断）  
> > > > > > > > > > > [第8章](#) → 真机部署（架构→选型→直控→采集→微调→对比）  
> > > > > > > > > > >   
> > > > > > > > > > > 三条路径相互补充。你可以选择其中一条深入，也可以全部掌握。
> > > > > > > > > > > 
> > > > > > > > > > > <div class="page-nav">
> > > > > > > > > > > 
> > > > > > > > > > > [← 第7章：VLN 仿真训练](habitat-textbook-step7.html) [第9章：Rearrange 操作 →](habitat-textbook-step9.html)
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > > > > 
> > > > > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > > > 
> > > > > > > > </div>
> > > > > > 
> > > > > > </div>
> > > > > 
> > > > > </div>
> > > > > 
> > > > > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> > 
> > </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
> </div>
> 
>
