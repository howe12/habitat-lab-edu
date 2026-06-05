#!/usr/bin/env bash
# Stop hook: check curriculum plan progress and report remaining gaps.
# Scans CURRICULUM_PLAN.md CHECK markers, verifies file existence.
set -euo pipefail

PROJECT_ROOT="/develop/habitat-lab"
PLAN_FILE="$PROJECT_ROOT/CURRICULUM_PLAN.md"

if [ ! -f "$PLAN_FILE" ]; then
    exit 0
fi

echo ""
echo "============================================"
echo " 课程计划进度检查"
echo "============================================"

total=0
done_count=0
pending=""

# Parse CHECK lines: grep them, then use bash string ops
grep -n 'CHECK:' "$PLAN_FILE" | while IFS= read -r line; do
    :
done || true  # consume grep output without error on no-match

# Actually do the counting in a way that survives subshell
markers=$(grep 'CHECK:' "$PLAN_FILE" || true)
if [ -z "$markers" ]; then
    echo " (无检查点)"
    exit 0
fi

# Use process substitution to avoid subshell issues
while IFS= read -r raw; do
    # Extract CHECK id and file hint from the line
    check_id=$(echo "$raw" | sed -n 's/.*CHECK:\([A-Z0-9_]*\).*/\1/p')
    file_hint=$(echo "$raw" | sed -n 's/.*文件:[[:space:]]*//p' | sed 's/).*//')

    if [ -z "$check_id" ]; then
        continue
    fi
    total=$((total + 1))

    found=false
    case "$check_id" in
        STEP1B)
            [ -f "$PROJECT_ROOT/habitat-viz/habitat-textbook-step1b.html" ] && found=true ;;
        STEP9)
            [ -f "$PROJECT_ROOT/habitat-viz/habitat-textbook-step9.html" ] && found=true ;;
        STEP5B)
            [ -f "$PROJECT_ROOT/habitat-viz/habitat-textbook-step5b.html" ] && found=true ;;
        P1_SEMANTIC)
            grep -q "semantic\|Semantic\|语义" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step4.html" 2>/dev/null && found=true ;;
        P1_MEASURE)
            (grep -q "register_measure\|自定义.*Measure\|自定义指标" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step4.html" 2>/dev/null) && found=true
            [ "$found" = false ] && (grep -q "register_measure\|自定义.*Measure\|自定义指标" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step6.html" 2>/dev/null) && found=true ;;
        P1_HRL)
            grep -q "HRL\|Hierarchical\|分层\|VER\|ver" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step5.html" 2>/dev/null && found=true ;;
        P1_DOCKER)
            (grep -q "docker\|Docker\|容器" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step1.html" 2>/dev/null) && found=true
            [ "$found" = false ] && (grep -q "docker\|Docker\|容器" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step7.html" 2>/dev/null) && found=true ;;
        P1_EQA)
            grep -q "EQA\|问答\|Question Answering" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step5.html" 2>/dev/null && found=true ;;
        P1_GYM)
            grep -q "gym_definitions\|HabitatPick\|HabitatPlace\|Gym.*注册" "$PROJECT_ROOT/habitat-viz/habitat-textbook-step2.html" 2>/dev/null && found=true ;;
        *)
            found=true ;;
    esac

    if $found; then
        done_count=$((done_count + 1))
        echo " [OK] $check_id — $file_hint"
    else
        pending="$pending  - $check_id: $file_hint"$'\n'
        echo " [  ] $check_id — $file_hint"
    fi
done <<< "$markers"

echo ""
echo " 完成: $done_count / $total"

if [ "$done_count" -lt "$total" ]; then
    pct=$(( (done_count * 100) / total ))
    echo " 进度: ${pct}%"
    echo ""
    echo " 待完成:"
    echo -n "$pending"
fi

echo "============================================"
echo ""
