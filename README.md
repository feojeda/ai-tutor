# AI Tutor

**Convierte cualquier agente CLI (OpenCode, Claude Code, Gemini, Codex) en un tutor socrático que te enseña lo que quieras aprender.**

---

## Qué es esto

Un conjunto de skills y cursos en markdown que, al cargarlos en tu agente de coding preferido, lo transforman en un profesor interactivo. No te escupe información — te hace preguntas, verifica que entendiste, y adapta el ritmo a tu nivel.

El proyecto tiene dos partes:

| Componente | Qué hace |
|-----------|---------|
| **Skill del tutor** (`skills/tutor/SKILL.md`) | Define CÓMO enseñar: método socrático, validación de comprensión, pacing adaptativo. Agnostico de tema. |
| **Cursos** (`cursos/`) | Define QUÉ enseñar: curriculum, ejercicios, proyectos. Cada curso es un tema específico. |

---

## Instalación rápida

```bash
git clone https://github.com/feojeda/ai-tutor.git
cd ai-tutor
python install.py
```

El installer detecta qué agentes tienes instalados y copia la skill donde corresponde:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/SKILL.md
✅ Claude Code: Installed → ~/.claude/skills/tutor/SKILL.md
✅ Course 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### Opciones

```bash
python install.py --list          # Ver qué agentes detecta
python install.py --agent opencode # Instalar solo para un agente
python install.py --dry-run       # Ver qué haría sin hacerlo
python install.py --uninstall     # Remover skills de todos los agentes
python install.py --course nuevo-curso  # Instalar un curso específico
```

---

## Cómo usarlo

Una vez instalado, abre tu agente y dile:

```
"Carga la skill tutor y abre ~/.ai-tutor/cursos/ejemplo-ml/curriculum.md.
Quiero aprender Machine Learning."
```

El agente cargará las reglas pedagógicas + el currículum del curso y comenzará a guiarte sesión por sesión.

---

## Agentes soportados

| Agente | Skill location | Comando para activar |
|--------|---------------|---------------------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## Cursos disponibles

### `ejemplo-ml` — Machine Learning desde cero
4-5 sesiones. Desde "qué es ML" hasta entrenar tu primer clasificador con scikit-learn. Prerrequisito: Python básico.

---

## Crear tu propio curso

1. Copia `cursos/ejemplo-ml/` con otro nombre
2. Edita `curriculum.md` con tu contenido
3. Agrega ejercicios en `ejercicios/`
4. Corre `python install.py --course tu-curso`

Estructura de un curso:

```
cursos/tu-curso/
├── curriculum.md    ← El plan de estudios (sesiones, objetivos, ejercicios)
├── rules.md         ← (opcional) Reglas pedagógicas específicas del tema
└── ejercicios/      ← (opcional) Ejercicios detallados
    ├── 01-intro.md
    └── 02-avanzado.md
```

### Reglas para escribir un buen curriculum

1. **Una sesión = un concepto.** No metas dos ideas nuevas en la misma sesión.
2. **Ejercicio después de teoría.** Cada sesión debe tener al menos un ejercicio práctico.
3. **Check de comprensión.** Termina cada sesión con una pregunta que verifique lo aprendido.
4. **Prerrequisitos claros.** El estudiante debe saber exactamente qué necesita antes de empezar.
5. **Ejemplos reales.** Usa datos y problemas del mundo real, no ejemplos de juguete.

---

## Filosofía

La mayoría de la gente no necesita otro tutorial de YouTube. Necesita a alguien que:
- Le haga las preguntas correctas en el momento correcto
- Detecte cuando no entendió y vuelva atrás
- Celebre los avances pequeños
- Adapte el ritmo a su nivel real

Un LLM con las reglas correctas puede hacer eso. Este proyecto le da esas reglas.

---

## Licencia

MIT. Usa esto para enseñar lo que quieras a quien quieras.
