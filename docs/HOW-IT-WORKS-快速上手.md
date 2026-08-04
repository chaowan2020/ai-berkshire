# AI Berkshire 快速上手：原理 + 多模型对比测试指南

> 给第一次接触这个项目的人。读完 3 分钟即可跑起来。

## 一、它是什么 / 不是什么

- **不是**一个要部署的服务、没有后端、没有数据库。
- **是**一套写给 AI Agent 的研究流程指令（`skills/*.md`）+ 零依赖 Python 验证工具（`tools/*.py`）。
- 运行方式：AI Agent（Claude Code / Codex / Kimi Code）读到 skill 指令后，按流程自己上网抓公开数据、调本地工具验算、把报告写进 `reports/`。

## 二、需要接 API 吗？

| 项目 | 需要吗 | 说明 |
|------|--------|------|
| 金融数据 API | ❌ | 数据源全是免注册公开网站（macrotrends / stockanalysis / aastocks / 东方财富 / 巨潮），Agent 运行时直接抓 |
| Python 依赖 | ❌ | 核心工具只用标准库，Python ≥ 3.7 即可，无需 pip install |
| 模型 API / 订阅 | ✅ 唯一需要 | 在 Agent 工具侧：Claude Code（Anthropic）、Codex（OpenAI）、Kimi Code（Moonshot），三选一 |
| Wind / iFinD 等专业数据源 | 可选 | 增强用，非必需 |

## 三、3 步跑起来

```bash
git clone <repo> && cd ai-berkshire

# 1. 安装 skills 到你的 Agent（三选一）
./scripts/install-claude-commands.sh    # Claude Code → ~/.claude/commands
./scripts/install-codex-skills.sh       # Codex
# Kimi Code：无需安装，直接让它读 skills/ 目录

# 2. 确认日期（研究规则强制要求，作为数据基准）
date

# 3. 在 Agent 里发指令
/investment-research 英伟达        # Claude Code / Codex 斜杠命令
# 或 Kimi Code 里说："按 skills/investment-research.md 研究英伟达"
```

报告产出在 `reports/`。

## 四、让别人试 / 多模型对比

项目与模型完全解耦——同一个 skill 可以在任何 Agent 上跑，这正好适合做横向对比：

1. **分享**：直接给对方 git 仓库地址 + 本文件，对方只需有自己的任一 Agent 工具。
2. **多模型对比**：用同一 skill、同一家公司，分别在 Claude Code / Codex / Kimi Code 各跑一遍。
   - Claude Code：`/model` 切换模型（Opus/Sonnet），prompt 里加 "think hard" 等关键词调思考深度
   - Codex：`--model` 选模型，`-c model_reasoning_effort=high` 调推理级别
   - Kimi Code：直接换后端模型
3. **对比产出**：约定输出文件名带模型后缀，如 `reports/NVDA-研究-claude-opus-20260804.md`、`reports/NVDA-研究-gpt5-high-20260804.md`，然后直接 diff 或并排读。
4. **评判标准**：用项目自带审计工具保证底线质量——
   `python3 tools/report_audit.py <报告路径>`，
   再人工比较：数据准确率（是否过了 financial_rigor 验算）、反面检验深度、结论是否有独立判断。

## 五、质量红线（无论谁跑都要遵守）

- 每个关键财务数据 ≥ 2 个独立来源，误差 >1% 必须标记
- 市值必须程序化验算：`python3 tools/financial_rigor.py verify-market-cap ...`
- 报告头部写明数据截止日期（以 `date` 为准）
- 本项目仅供学习研究，不构成投资建议
