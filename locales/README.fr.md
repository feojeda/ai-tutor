# AI Tutor

**Transformez n'importe quel agent CLI (OpenCode, Claude Code, Gemini, Codex) en tuteur socratique qui vous enseigne ce que vous voulez apprendre.**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 Installer

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### Demandez à votre agent de le faire

Collez ceci dans n'importe quel agent CLI :

```
Clone https://github.com/feojeda/ai-tutor.git dans ~/.ai-tutor et exécute python3 ~/.ai-tutor/install.py. Ensuite, dis-moi quels agents il a détectés.
```

### Désinstaller

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

L'installateur détecte les agents installés et copie la skill au bon endroit :

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ Cours 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Options

```bash
python install.py --list          # Voir les agents détectés
python install.py --agent opencode # Installer pour un seul agent
python install.py --dry-run       # Aperçu sans modifier
python install.py --uninstall     # Supprimer de tous les agents
python install.py --course nom    # Installer un cours spécifique
```

---

## Qu'est-ce que c'est

Un ensemble de skills et de cours en markdown qui, une fois chargés dans votre agent de coding, le transforment en professeur interactif. Il ne vous crache pas l'information — il pose des questions, vérifie votre compréhension et adapte le rythme à votre niveau.

Deux parties :

- **Skill du tuteur** (`skills/tutor/SKILL.md`) — Définit COMMENT enseigner : méthode socratique, vérification de la compréhension, rythme adaptatif. Indépendant du sujet.
- **Cours** (`cursos/`) — Définit QUOI enseigner : programme, exercices, projets. Un cours par sujet.

---

## Comment l'utiliser

Une fois installé, ouvrez votre agent et dites :

```
"Charge la skill tutor. Je veux apprendre le machine learning."
```

L'agent charge les règles pédagogiques et commence à vous guider session par session.

---

## Agents supportés

| Agent | Emplacement de la skill | Activation |
|-------|------------------------|------------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Cours disponibles

### `ejemplo-ml` — Machine Learning à partir de zéro
4-5 sessions. De « qu'est-ce que le ML » jusqu'à l'entraînement de votre premier classifieur avec scikit-learn. Prérequis : Python de base.

---

## Créer votre propre cours

1. Copiez `cursos/ejemplo-ml/` avec un autre nom
2. Modifiez `curriculum.md` avec votre contenu
3. Ajoutez des exercices dans `ejercicios/`
4. Exécutez `python install.py --course votre-cours`

Structure d'un cours :

```
cursos/votre-cours/
├── curriculum.md    ← Programme (sessions, objectifs, exercices)
├── rules.md         ← (optionnel) Règles pédagogiques spécifiques au sujet
└── ejercicios/      ← (optionnel) Exercices détaillés
    ├── 01-intro.md
    └── 02-avance.md
```

### Règles pour un bon programme

1. **Une session = un concept.** Ne mettez pas deux idées nouvelles dans la même session.
2. **Exercice après la théorie.** Chaque session doit avoir au moins un exercice pratique.
3. **Vérification de la compréhension.** Terminez chaque session par une question qui vérifie l'apprentissage.
4. **Prérequis clairs.** L'étudiant doit savoir exactement ce dont il a besoin avant de commencer.
5. **Exemples réels.** Utilisez des données et problèmes du monde réel, pas des exemples jouets.

---

## Philosophie

La plupart des gens n'ont pas besoin d'un autre tutoriel YouTube. Ils ont besoin de quelqu'un qui :
- Pose les bonnes questions au bon moment
- Remarque quand ils n'ont pas compris et revient en arrière
- Célèbre les petites victoires
- Adapte le rythme à leur niveau réel

Un LLM avec les bonnes règles peut faire cela. Ce projet lui donne ces règles.

---

## Licence

MIT. Utilisez ceci pour enseigner ce que vous voulez à qui vous voulez.
