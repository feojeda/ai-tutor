# AI Tutor

**Trasforma qualsiasi agente CLI (OpenCode, Claude Code, Gemini, Codex) in un tutor socratico che ti insegna ciò che vuoi imparare.**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 Installare

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### Chiedi al tuo agente di farlo

Incolla questo in qualsiasi agente CLI:

```
Clona https://github.com/feojeda/ai-tutor.git in ~/.ai-tutor ed esegui python3 ~/.ai-tutor/install.py. Poi dimmi quali agenti ha rilevato.
```

### Disinstallare

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

L'installer rileva quali agenti hai e copia la skill nella posizione corretta:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ Corso 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Opzioni

```bash
python install.py --list          # Vedi agenti rilevati
python install.py --agent opencode # Installa solo per un agente
python install.py --dry-run       # Anteprima senza modifiche
python install.py --uninstall     # Rimuovi da tutti gli agenti
python install.py --course nome   # Installa un corso specifico
```

---

## Cos'è

Un insieme di skill e corsi in markdown che, caricati nel tuo agente di coding, lo trasformano in un insegnante interattivo. Non ti sputa informazioni — fa domande, verifica la comprensione e adatta il ritmo al tuo livello.

Due parti:

- **Skill del tutor** (`skills/tutor/SKILL.md`) — Definisce COME insegnare: metodo socratico, verifica della comprensione, ritmo adattivo. Indipendente dal tema.
- **Corsi** (`cursos/`) — Definisce COSA insegnare: programma, esercizi, progetti. Un corso per tema.

---

## Come usarlo

Dopo l'installazione, apri il tuo agente e digli:

```
"Carica la skill tutor. Voglio imparare il machine learning."
```

L'agente carica le regole pedagogiche e inizia a guidarti sessione per sessione.

---

## Agenti supportati

| Agente | Posizione skill | Attivazione |
|--------|----------------|-------------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Corsi disponibili

### `ejemplo-ml` — Machine Learning da zero
4-5 sessioni. Da "cos'è il ML" fino ad addestrare il tuo primo classificatore con scikit-learn. Prerequisito: Python base.

---

## Creare il tuo corso

1. Copia `cursos/ejemplo-ml/` con un altro nome
2. Modifica `curriculum.md` con il tuo contenuto
3. Aggiungi esercizi in `ejercicios/`
4. Esegui `python install.py --course tuo-corso`

Struttura di un corso:

```
cursos/tuo-corso/
├── curriculum.md    ← Programma (sessioni, obiettivi, esercizi)
├── rules.md         ← (opzionale) Regole pedagogiche specifiche del tema
└── ejercicios/      ← (opzionale) Esercizi dettagliati
    ├── 01-intro.md
    └── 02-avanzato.md
```

### Regole per un buon programma

1. **Una sessione = un concetto.** Non mettere due idee nuove nella stessa sessione.
2. **Esercizio dopo la teoria.** Ogni sessione deve avere almeno un esercizio pratico.
3. **Verifica della comprensione.** Termina ogni sessione con una domanda che verifichi l'apprendimento.
4. **Prerequisiti chiari.** Lo studente deve sapere esattamente cosa serve prima di iniziare.
5. **Esempi reali.** Usa dati e problemi del mondo reale, non esempi giocattolo.

---

## Filosofia

La maggior parte delle persone non ha bisogno di un altro tutorial su YouTube. Ha bisogno di qualcuno che:
- Faccia le domande giuste al momento giusto
- Si accorga quando non ha capito e torni indietro
- Celebra i piccoli progressi
- Adatti il ritmo al suo livello reale

Un LLM con le regole giuste può farlo. Questo progetto gli dà quelle regole.

---

## Licenza

MIT. Usalo per insegnare ciò che vuoi a chi vuoi.
