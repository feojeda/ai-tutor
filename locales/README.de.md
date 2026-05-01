# AI Tutor

**Verwandle jeden CLI-Agenten (OpenCode, Claude Code, Gemini, Codex) in einen sokratischen Tutor, der dir alles beibringt, was du lernen möchtest.**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 Installieren

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### Lass deinen Agenten installieren

Füge dies in einen beliebigen CLI-Agenten ein:

```
Klone https://github.com/feojeda/ai-tutor.git nach ~/.ai-tutor und führe python3 ~/.ai-tutor/install.py aus. Sag mir dann, welche Agenten erkannt wurden.
```

### Deinstallieren

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

Der Installer erkennt installierte Agenten und kopiert die Skill an die richtige Stelle:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ Kurs 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Optionen

```bash
python install.py --list          # Erkannte Agenten anzeigen
python install.py --agent opencode # Nur für einen Agenten installieren
python install.py --dry-run       # Vorschau ohne Änderungen
python install.py --uninstall     # Von allen Agenten entfernen
python install.py --course name   # Bestimmten Kurs installieren
```

---

## Was ist das

Eine Sammlung von Skills und Kursen in Markdown, die deinen Coding-Agenten in einen interaktiven Lehrer verwandeln. Er spuckt keine Informationen aus — er stellt Fragen, überprüft dein Verständnis und passt das Tempo an dein Niveau an.

Zwei Teile:

- **Tutor-Skill** (`skills/tutor/SKILL.md`) — Definiert WIE gelehrt wird: sokratische Methode, Verständnisprüfung, adaptives Tempo. Themenunabhängig.
- **Kurse** (`cursos/`) — Definiert WAS gelehrt wird: Lehrplan, Übungen, Projekte. Ein Kurs pro Thema.

---

## Verwendung

Nach der Installation öffne deinen Agenten und sage:

```
"Lade den Tutor-Skill. Ich möchte Machine Learning lernen."
```

Der Agent lädt die pädagogischen Regeln und beginnt, dich Sitzung für Sitzung zu führen.

---

## Unterstützte Agenten

| Agent | Skill-Speicherort | Aktivierung |
|-------|-------------------|-------------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Verfügbare Kurse

### `ejemplo-ml` — Machine Learning von Grund auf
4-5 Sitzungen. Von „Was ist ML" bis zum Training deines ersten Klassifikators mit scikit-learn. Voraussetzung: grundlegende Python-Kenntnisse.

---

## Eigenen Kurs erstellen

1. Kopiere `cursos/ejemplo-ml/` mit neuem Namen
2. Bearbeite `curriculum.md` mit deinem Inhalt
3. Füge Übungen in `ejercicios/` hinzu
4. Führe `python install.py --course dein-kurs` aus

Kursstruktur:

```
cursos/dein-kurs/
├── curriculum.md    ← Lehrplan (Sitzungen, Ziele, Übungen)
├── rules.md         ← (optional) Themenspezifische pädagogische Regeln
└── ejercicios/      ← (optional) Detaillierte Übungen
    ├── 01-intro.md
    └── 02-fortgeschritten.md
```

### Regeln für einen guten Lehrplan

1. **Eine Sitzung = ein Konzept.** Packe nicht zwei neue Ideen in eine Sitzung.
2. **Übung nach Theorie.** Jede Sitzung braucht mindestens eine praktische Übung.
3. **Verständnisprüfung.** Beende jede Sitzung mit einer Frage, die das Gelernte überprüft.
4. **Klare Voraussetzungen.** Der Lernende muss genau wissen, was er vorher können muss.
5. **Echte Beispiele.** Verwende reale Daten und Probleme, keine Spielzeugbeispiele.

---

## Philosophie

Die meisten Menschen brauchen kein weiteres YouTube-Tutorial. Sie brauchen jemanden, der:
- Die richtigen Fragen zur richtigen Zeit stellt
- Bemerkt, wenn sie etwas nicht verstanden haben, und zurückgeht
- Kleine Fortschritte feiert
- Das Tempo an ihr tatsächliches Niveau anpasst

Ein LLM mit den richtigen Regeln kann das. Dieses Projekt gibt ihm diese Regeln.

---

## Lizenz

MIT. Verwende dies, um zu lehren, was du willst, wem du willst.
