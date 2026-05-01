# AI Tutor

**حوّل أي وكيل CLI (OpenCode، Claude Code، Gemini، Codex) إلى معلم سقراطي يعلمك ما تريد تعلمه.**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 تثبيت

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### اطلب من وكيلك التثبيت

الصق هذا في أي وكيل CLI:

```
انسخ https://github.com/feojeda/ai-tutor.git إلى ~/.ai-tutor وشغّل python3 ~/.ai-tutor/install.py. ثم أخبرني أي الوكلاء اكتشف.
```

### إلغاء التثبيت

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

يكتشف المثبّت الوكلاء المثبتين لديك وينسخ المهارة إلى المكان الصحيح:

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ دورة 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### خيارات

```bash
python install.py --list          # عرض الوكلاء المكتشفين
python install.py --agent opencode # تثبيت لوكيل واحد فقط
python install.py --dry-run       # معاينة بدون تغييرات
python install.py --uninstall     # إزالة من جميع الوكلاء
python install.py --course name   # تثبيت دورة محددة
```

---

## ما هذا

مجموعة من المهارات والدورات بصيغة markdown، عند تحميلها في وكيل البرمجة الخاص بك، تحوله إلى معلم تفاعلي. لا يلقي المعلومات عليك — بل يطرح أسئلة، ويتحقق من فهمك، ويكيّف الوتيرة مع مستواك.

جزآن:

- **مهارة المعلم** (`skills/tutor/SKILL.md`) — تحدد كيفية التدريس: الطريقة السقراطية، التحقق من الفهم، وتيرة تكيّفية. مستقلة عن الموضوع.
- **الدورات** (`cursos/`) — تحدد ماذا تدرّس: منهج، تمارين، مشاريع. دورة واحدة لكل موضوع.

---

## كيفية الاستخدام

بعد التثبيت، افتح وكيلك وقل له:

```
"حمّل مهارة المعلم. أريد تعلم تعلم الآلة."
```

يحمل الوكيل القواعد التربوية ويبدأ في إرشادك جلسة تلو الأخرى.

---

## الوكلاء المدعومون

| الوكيل | موقع المهارة | التفعيل |
|--------|-------------|---------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## الدورات المتاحة

### `ejemplo-ml` — تعلم الآلة من الصفر
4-5 جلسات. من "ما هو تعلم الآلة" إلى تدريب أول مصنّف لك باستخدام scikit-learn. المتطلب: أساسيات Python.

---

## إنشاء دورتك الخاصة

1. انسخ `cursos/ejemplo-ml/` باسم جديد
2. عدّل `curriculum.md` بمحتواك
3. أضف تمارين في `ejercicios/`
4. شغّل `python install.py --course دورتك`

هيكل الدورة:

```
cursos/دورتك/
├── curriculum.md    ← خطة الدراسة (جلسات، أهداف، تمارين)
├── rules.md         ← (اختياري) قواعد تربوية خاصة بالموضوع
└── ejercicios/      ← (اختياري) تمارين مفصلة
    ├── 01-intro.md
    └── 02-advanced.md
```

### قواعد لمنهج جيد

1. **جلسة واحدة = مفهوم واحد.** لا تضع فكرتين جديدتين في نفس الجلسة.
2. **تمرين بعد النظرية.** كل جلسة تحتاج إلى تمرين عملي واحد على الأقل.
3. **التحقق من الفهم.** أنهِ كل جلسة بسؤال يتحقق من التعلم.
4. **متطلبات واضحة.** يجب أن يعرف الطالب بالضبط ما يحتاجه قبل البدء.
5. **أمثلة حقيقية.** استخدم بيانات ومشاكل من العالم الحقيقي، وليس أمثلة لعب.

---

## الفلسفة

معظم الناس لا يحتاجون إلى درس آخر على YouTube. يحتاجون إلى شخص:
- يطرح الأسئلة الصحيحة في الوقت المناسب
- يلاحظ عندما لا يفهمون ويعود للخلف
- يحتفل بالانتصارات الصغيرة
- يكيّف الوتيرة مع مستواهم الحقيقي

يمكن لنموذج لغوي كبير بالقواعد الصحيحة أن يفعل ذلك. هذا المشروع يمنحه تلك القواعد.

---

## الرخصة

MIT. استخدم هذا لتعليم ما تريد لمن تريد.
