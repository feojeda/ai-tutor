# AI Tutor

**Transforme qualquer agente CLI (OpenCode, Claude Code, Gemini, Codex) em um tutor socrático que ensina o que você quiser aprender.**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 Instalar

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### Peça ao seu agente para instalar

Cole isto em qualquer agente CLI:

```
Clone https://github.com/feojeda/ai-tutor.git em ~/.ai-tutor e execute python3 ~/.ai-tutor/install.py. Depois me diga quais agentes foram detectados.
```

### Desinstalar

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

O instalador detecta quais agentes você tem e copia a skill para o local correto:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ Curso 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Opções

```bash
python install.py --list          # Ver agentes detectados
python install.py --agent opencode # Instalar apenas para um agente
python install.py --dry-run       # Pré-visualizar sem alterar
python install.py --uninstall     # Remover de todos os agentes
python install.py --course nome   # Instalar um curso específico
```

---

## O que é isto

Um conjunto de skills e cursos em markdown que, quando carregados no seu agente de coding, o transformam em um professor interativo. Ele não cospe informação — faz perguntas, verifica sua compreensão e adapta o ritmo ao seu nível.

Duas partes:

- **Skill do tutor** (`skills/tutor/SKILL.md`) — Define COMO ensinar: método socrático, verificação de compreensão, ritmo adaptativo. Agnóstico ao tema.
- **Cursos** (`cursos/`) — Define O QUE ensinar: currículo, exercícios, projetos. Um curso por tema.

---

## Como usar

Depois de instalado, abra seu agente e diga:

```
"Carregue a skill tutor. Quero aprender sobre machine learning."
```

O agente carrega as regras pedagógicas e começa a guiá-lo sessão por sessão.

---

## Agentes suportados

| Agente | Local da skill | Ativação |
|--------|---------------|----------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Cursos disponíveis

### `ejemplo-ml` — Machine Learning do zero
4-5 sessões. Do "o que é ML" até treinar seu primeiro classificador com scikit-learn. Pré-requisito: Python básico.

---

## Criar seu próprio curso

1. Copie `cursos/ejemplo-ml/` com outro nome
2. Edite `curriculum.md` com seu conteúdo
3. Adicione exercícios em `ejercicios/`
4. Execute `python install.py --course seu-curso`

Estrutura de um curso:

```
cursos/seu-curso/
├── curriculum.md    ← Plano de estudos (sessões, objetivos, exercícios)
├── rules.md         ← (opcional) Regras pedagógicas específicas do tema
└── ejercicios/      ← (opcional) Exercícios detalhados
    ├── 01-intro.md
    └── 02-avancado.md
```

### Regras para um bom currículo

1. **Uma sessão = um conceito.** Não coloque duas ideias novas na mesma sessão.
2. **Exercício após teoria.** Toda sessão precisa de pelo menos um exercício prático.
3. **Verificação de compreensão.** Termine cada sessão com uma pergunta que verifique o aprendizado.
4. **Pré-requisitos claros.** O aluno deve saber exatamente o que precisa antes de começar.
5. **Exemplos reais.** Use dados e problemas do mundo real, não exemplos artificiais.

---

## Filosofia

A maioria das pessoas não precisa de mais um tutorial do YouTube. Elas precisam de alguém que:
- Faça as perguntas certas no momento certo
- Perceba quando não entenderam e volte atrás
- Celebre os pequenos avanços
- Adapte o ritmo ao nível real delas

Um LLM com as regras certas pode fazer isso. Este projeto dá a ele essas regras.

---

## Licença

MIT. Use isto para ensinar o que quiser para quem quiser.
