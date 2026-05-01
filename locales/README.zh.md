# AI Tutor

**将任何 CLI 编程助手（OpenCode、Claude Code、Gemini、Codex）转变为苏格拉底式导师，教你任何你想学的内容。**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 安装

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### 让你的助手来安装

将以下内容粘贴到任何 CLI 编程助手中：

```
将 https://github.com/feojeda/ai-tutor.git 克隆到 ~/.ai-tutor，然后运行 python3 ~/.ai-tutor/install.py。之后告诉我它检测到了哪些助手。
```

### 卸载

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

安装程序会检测你安装了哪些编程助手，并将技能文件复制到正确的位置：

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ 课程 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### 选项

```bash
python install.py --list          # 查看检测到的助手
python install.py --agent opencode # 仅为某个助手安装
python install.py --dry-run       # 预览而不做更改
python install.py --uninstall     # 从所有助手中移除
python install.py --course name   # 安装特定课程
```

---

## 这是什么

一组用 Markdown 编写的技能和课程，加载到你的编程助手中后，将其转变为互动教师。它不会向你灌输信息——它会提问、检查你的理解，并根据你的水平调整节奏。

两个部分：

- **导师技能** (`skills/tutor/SKILL.md`) — 定义如何教学：苏格拉底式方法、理解检查、自适应节奏。与主题无关。
- **课程** (`cursos/`) — 定义教什么：课程大纲、练习、项目。每个主题一个课程。

---

## 如何使用

安装后，打开你的编程助手并说：

```
"加载导师技能。我想学习机器学习。"
```

助手加载教学规则，并开始逐节课引导你。

---

## 支持的编程助手

| 助手 | 技能位置 | 激活方式 |
|------|---------|---------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## 可用课程

### `ejemplo-ml` — 机器学习从零开始
4-5 节课。从"什么是机器学习"到用 scikit-learn 训练你的第一个分类器。前提条件：Python 基础。

---

## 创建你自己的课程

1. 用新名称复制 `cursos/ejemplo-ml/`
2. 编辑 `curriculum.md` 填入你的内容
3. 在 `ejercicios/` 中添加练习
4. 运行 `python install.py --course 你的课程`

课程结构：

```
cursos/你的课程/
├── curriculum.md    ← 学习计划（课时、目标、练习）
├── rules.md         ← （可选）主题特定的教学规则
└── ejercicios/      ← （可选）详细练习
    ├── 01-intro.md
    └── 02-advanced.md
```

### 优质课程大纲的规则

1. **一节课 = 一个概念。** 不要在一节课中塞入两个新概念。
2. **理论之后实践。** 每节课至少需要一次动手练习。
3. **理解检查。** 用确认学习成果的问题结束每节课。
4. **明确的前置条件。** 学员必须清楚知道开始前需要什么。
5. **真实案例。** 使用真实世界的数据和问题，而非玩具示例。

---

## 理念

大多数人不需要另一个 YouTube 教程。他们需要的是有人能够：
- 在正确的时间提出正确的问题
- 发现他们没理解并回头重讲
- 庆祝每一个小进步
- 根据他们的真实水平调整节奏

一个加载了正确规则的大语言模型可以做到这一切。这个项目为它提供了这些规则。

---

## 许可证

MIT。用它教你想教的任何人任何知识。
