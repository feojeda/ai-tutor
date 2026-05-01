# AI Tutor

**Turn any CLI coding agent (OpenCode, Claude Code, Gemini, Codex) into a Socratic tutor that teaches you whatever you want to learn.**

[English](README.md) | [Español](locales/README.es.md) | [Português](locales/README.pt.md) | [Français](locales/README.fr.md) | [Deutsch](locales/README.de.md) | [Italiano](locales/README.it.md) | [हिन्दी](locales/README.hi.md) | [العربية](locales/README.ar.md) | [中文](locales/README.zh.md) | [日本語](locales/README.ja.md)

---

## 🚀 Install

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### Tell your agent to do it

Paste this into any CLI agent:

```
Clone https://github.com/feojeda/ai-tutor.git into ~/.ai-tutor and run python3 ~/.ai-tutor/install.py. Then tell me which agents it detected.
```

### Uninstall

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

The installer detects which agents you have and copies the skill where it belongs:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ Course 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Options

```bash
python install.py --list          # See detected agents
python install.py --agent opencode # Install for one agent only
python install.py --dry-run       # Preview without making changes
python install.py --uninstall     # Remove from all agents
python install.py --course name   # Install a specific course
```

---

## What is this?

A set of skills and markdown courses that, when loaded into your coding agent, turn it into an interactive teacher. It doesn't spit information at you — it asks questions, checks your understanding, and adapts the pace to your level.

Two parts:

- **Tutor skill** (`skills/tutor/SKILL.md`) — Defines HOW to teach: Socratic method, comprehension checks, adaptive pacing. Topic-agnostic.
- **Courses** (`cursos/`) — Defines WHAT to teach: curriculum, exercises, projects. One course per topic.

---

## How to use

Once installed, open your agent and say:

```
"Load the tutor skill. I want to learn about machine learning."
```

The agent loads the pedagogical rules and begins guiding you session by session.

---

## Supported agents

| Agent | Skill location | Activation |
|-------|---------------|------------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Available courses

### `ejemplo-ml` — Machine Learning from scratch
4-5 sessions. From "what is ML" to training your first classifier with scikit-learn. Prerequisite: basic Python.

---

## Create your own course

1. Copy `cursos/ejemplo-ml/` with a new name
2. Edit `curriculum.md` with your content
3. Add exercises to `ejercicios/`
4. Run `python install.py --course your-course`

Course structure:

```
cursos/your-course/
├── curriculum.md    ← Study plan (sessions, objectives, exercises)
├── rules.md         ← (optional) Topic-specific pedagogical rules
└── ejercicios/      ← (optional) Detailed exercises
    ├── 01-intro.md
    └── 02-advanced.md
```

### Rules for a good curriculum

1. **One session = one concept.** Don't pack two new ideas into one session.
2. **Exercise after theory.** Every session needs at least one hands-on exercise.
3. **Comprehension check.** End each session with a question that verifies learning.
4. **Clear prerequisites.** The student must know exactly what they need before starting.
5. **Real examples.** Use real-world data and problems, not toy examples.

---

## Philosophy

Most people don't need another YouTube tutorial. They need someone who:
- Asks the right questions at the right time
- Notices when they didn't understand and goes back
- Celebrates small wins
- Adapts the pace to their real level

An LLM with the right rules can do that. This project gives it those rules.

---

## License

MIT. Use this to teach whatever you want to whomever you want.
