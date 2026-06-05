#!/usr/bin/env python3
"""Habitat-Viz 站点构建脚本。

功能：
  1. 把每个 step 页的 inline <style> 块替换为 <link> 到 assets/css/theme.css
  2. 把通用"复制按钮" <script> 块替换为 <script src="assets/js/site.js">
  3. 调整 checklist <script> 以通过 window.totalStages 配置
  4. 模板化 topnav / footer / page-nav（基于 site.json）

用法：
  python3 build.py         # 默认从 _src/ 渲染到当前目录
  python3 build.py --check # 只检查，不写文件
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC_DIR = ROOT / "_src"  # 源文件（包含模板占位符）
SITE_JSON = ROOT / "_data" / "site.json"

# ── 替换规则 ─────────────────────────────────────
LINK_THEME = '<link rel="stylesheet" href="assets/css/theme.css">\n'
LINK_SITE_JS = '<script src="assets/js/site.js"></script>\n'


def extract_inline_style(html: str) -> str | None:
    """提取 <style>...</style> 块内容。"""
    m = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
    return m.group(1) if m else None


def extract_copy_button_script(html: str) -> str | None:
    """提取通用复制按钮 <script> 块（匹配含 'code-block-wrapper' 的）"""
    m = re.search(
        r"<script>\s*\n//\s*─+\s*一键复制按钮[\s\S]*?</script>", html
    )
    return m.group(0) if m else None


def extract_checklist_script(html: str) -> str | None:
    """提取 checklist <script> 块（page-specific totalStages）"""
    m = re.search(
        r"<script>\s*\n//\s*Checklist interactive behavior[\s\S]*?</script>",
        html,
    )
    return m.group(0) if m else None


def extract_combined_script(html: str) -> tuple[str, int] | None:
    """合并的 <script> 块（含 checklist + 复制按钮），返回 (整段, totalStages)"""
    blocks = re.findall(r"<script>([\s\S]*?)</script>", html)
    for body in blocks:
        m_stages = re.search(r"const totalStages\s*=\s*(\d+);", body)
        m_copy = re.search(r"//\s*─+\s*一键复制按钮", body)
        if m_stages and m_copy:
            return body, int(m_stages.group(1))
    return None


def extract_prewrapped_copy_script(html: str) -> str | None:
    """已预包裹的复制按钮 <script>（step6/7/8 模式：只附加 handler）"""
    # 匹配：(function() { ... querySelectorAll('.code-block-wrapper') ... btn.onclick ...
    m = re.search(
        r"<script>\s*\(function\(\)\s*\{[\s\S]*?querySelectorAll\('\.code-block-wrapper'\)[\s\S]*?btn\.onclick[\s\S]*?\}\)\(\);[\s\S]*?</script>",
        html,
    )
    return m.group(0) if m else None


def migrate_page(src_html: str) -> tuple[str, dict]:
    """迁移单个页面：剥离内联样式和通用脚本，返回 (新 HTML, 报告)。

    幂等：如果页面已经引用 assets/css/theme.css，则保留其后所有
    <style> 块作为页面专属样式，不再抽走。
    """
    report = {
        "css_inlined_lines": 0,
        "copy_btn_replaced": False,
        "checklist_kept": False,
        "skipped_already_migrated": False,
    }

    already_migrated = 'href="assets/css/theme.css"' in src_html

    # 1. 抽 CSS（仅当还没迁过）
    if not already_migrated:
        css = extract_inline_style(src_html)
        if css:
            report["css_inlined_lines"] = len(css.splitlines())
            src_html = re.sub(
                r"<style>.*?</style>", LINK_THEME, src_html, count=1, flags=re.DOTALL
            )
    else:
        report["skipped_already_migrated"] = True

    # 2. 抽"独立"的复制按钮 <script>（step1/3/4/5）
    copy_btn = extract_copy_button_script(src_html)
    if copy_btn:
        report["copy_btn_replaced"] = True
        src_html = src_html.replace(copy_btn, LINK_SITE_JS)

    # 3. 抽"独立"的 checklist <script>
    checklist = extract_checklist_script(src_html)
    if checklist:
        report["checklist_kept"] = True
        new_checklist = re.sub(
            r"const totalStages\s*=\s*(\d+);",
            r"window.totalStages = \1;",
            checklist,
        )
        src_html = src_html.replace(checklist, new_checklist)

    # 4. 抽"合并"的 <script> 块（step2/6/7/8：checklist + 复制按钮在同一 script）
    combined = extract_combined_script(src_html)
    if combined:
        body, total = combined
        report["copy_btn_replaced"] = True
        report["checklist_kept"] = True
        new_script = (
            f"<script>\nwindow.totalStages = {total};\n"
            f"function toggleCheck(el) {{ el.classList.toggle('checked'); updateProgress(); }}\n"
            f"function updateProgress() {{\n"
            f"  const checked = document.querySelectorAll('.checkbox.checked').length;\n"
            f"  if (window.totalStages > 0) {{\n"
            f"    const fill = document.getElementById('progress-fill');\n"
            f"    const text = document.getElementById('progress-text');\n"
            f"    if (fill) fill.style.width = (checked / window.totalStages * 100) + '%';\n"
            f"    if (text) text.textContent = checked + ' / ' + window.totalStages + ' 完成';\n"
            f"  }}\n"
            f"}}\n</script>\n{LINK_SITE_JS}"
        )
        # 替换整段 <script>...</script>（注意：只替换包含 totalStages + 复制按钮的那个）
        src_html = re.sub(
            r"<script>[\s\S]*?const totalStages[\s\S]*?//\s*─+\s*一键复制按钮[\s\S]*?</script>",
            new_script,
            src_html,
            count=1,
        )

    # 5. 抽"已预包裹"的复制按钮 <script>（step6/7/8：只附加 handler）
    prewrapped = extract_prewrapped_copy_script(src_html)
    if prewrapped:
        report["copy_btn_replaced"] = True
        src_html = src_html.replace(prewrapped, LINK_SITE_JS)

    return src_html, report


def load_site_config() -> dict:
    """加载 site.json 配置。"""
    if SITE_JSON.exists():
        return json.loads(SITE_JSON.read_text(encoding="utf-8"))
    return {}


def main():
    check_only = "--check" in sys.argv

    # 决定源目录与目标目录
    src_dir = SRC_DIR if SRC_DIR.exists() else ROOT
    pages = sorted(src_dir.glob("habitat-textbook-step*.html"))
    if not pages:
        pages = sorted(ROOT.glob("habitat-textbook-step*.html"))

    if not pages:
        print("⚠ 找不到 step 页面", file=sys.stderr)
        return 1

    total_saved_lines = 0
    print(f"发现 {len(pages)} 个 step 页面，{'仅检查' if check_only else '开始迁移'}...")
    print()

    for src in pages:
        if src_dir == SRC_DIR:
            dst = ROOT / src.name
        else:
            dst = src

        original = src.read_text(encoding="utf-8")
        migrated, report = migrate_page(original)

        saved = report["css_inlined_lines"]
        total_saved_lines += saved
        status = "✓" if report["copy_btn_replaced"] else "○"
        print(
            f"  {status} {src.name}: 抽 CSS {saved} 行"
            f"  | 复制按钮 {'已替换' if report['copy_btn_replaced'] else '未找到'}"
            f"  | checklist {'保留' if report['checklist_kept'] else '无'}"
        )

        if not check_only and migrated != original:
            dst.write_text(migrated, encoding="utf-8")

    print()
    print(f"总计消除 {total_saved_lines} 行重复 CSS（{len(pages)} 个页面）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
