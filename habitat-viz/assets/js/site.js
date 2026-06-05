// ═══════════════════════════════════════════════════════════
//  Habitat-Lab 教程共享脚本
//  - copy-btn: 一键复制代码块
//  - checklist: 进度条 (page-specific totalStages)
//  ═══════════════════════════════════════════════════════════

(function () {
  'use strict';

  // ── 1. 一键复制按钮 ─────────────────────────────────
  // 两种 HTML 结构都支持：
  //   a)  <pre class="code-block">           （site.js 自动包裹 + 创建按钮）
  //   b)  <div class="code-block-wrapper">   （HTML 已包好，按钮在 <button class="copy-btn">）
  function makeCopyHandler(block, btn) {
    return function () {
      var text = block.textContent || block.innerText || '';
      navigator.clipboard.writeText(text).then(function () {
        btn.textContent = '已复制!';
        btn.classList.add('copied');
        setTimeout(function () {
          btn.textContent = '复制';
          btn.classList.remove('copied');
        }, 1500);
      });
    };
  }

  function initCopyButtons() {
    // a) 未包裹的 .code-block — 自动创建 wrapper + 按钮
    document.querySelectorAll('.code-block').forEach(function (block) {
      if (block.parentNode.classList.contains('code-block-wrapper')) return;
      var wrapper = document.createElement('div');
      wrapper.className = 'code-block-wrapper';
      block.parentNode.insertBefore(wrapper, block);
      wrapper.appendChild(block);
      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.textContent = '复制';
      btn.onclick = makeCopyHandler(block, btn);
      wrapper.appendChild(btn);
    });

    // b) 已包裹的 .code-block-wrapper 但按钮还没绑定 — 绑定现有按钮
    document.querySelectorAll('.code-block-wrapper').forEach(function (wrapper) {
      var block = wrapper.querySelector('.code-block');
      var btn = wrapper.querySelector('.copy-btn');
      if (!block || !btn) return;
      if (btn.onclick) return;  // 已绑定
      btn.onclick = makeCopyHandler(block, btn);
    });
  }

  // ── 2. Checklist 进度（页面须在 <body> 末定义 window.totalStages） ─
  function toggleCheck(el, stage) {
    el.classList.toggle('checked');
    updateProgress();
  }
  function updateProgress() {
    var total = window.totalStages || 0;
    if (total === 0) return;
    var checked = document.querySelectorAll('.checkbox.checked').length;
    var fill = document.getElementById('progress-fill');
    var text = document.getElementById('progress-text');
    if (fill) fill.style.width = (checked / total * 100) + '%';
    if (text) text.textContent = checked + ' / ' + total + ' 阶段完成';
  }
  // 暴露到全局
  window.toggleCheck = toggleCheck;
  window.updateProgress = updateProgress;

  // ── Boot ─────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCopyButtons);
  } else {
    initCopyButtons();
  }
})();
