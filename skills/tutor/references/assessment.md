# Assessment Framework

When assessing a student's current level on a topic, use this framework to generate diagnostic questions.

## Level Definitions

| Level | Label | Description |
|-------|-------|-------------|
| 0 | Complete beginner | Never heard of the topic or only knows the name |
| 1 | Aware | Knows basic terminology, can name key concepts but can't apply them |
| 2 | Familiar | Has done tutorials, watched videos, can follow guided examples |
| 3 | Practitioner | Has built real projects, can work independently, understands tradeoffs |
| 4 | Expert | Could teach the topic, understands underlying principles, contributes to the field |

## Question Templates by Level

For any topic, generate questions following these patterns:

### Level 0 → 1 questions (testing basic awareness)
- "Have you heard of [key concept]? If so, what do you think it means?"
- "In your own words, what do you think [topic] is about?"
- "Have you ever [done basic activity related to topic]?"

### Level 1 → 2 questions (testing conceptual understanding)
- "Can you explain the difference between [concept A] and [concept B]?"
- "Why would someone use [tool/technique] instead of [alternative]?"
- "What are the main steps in [process related to topic]?"

### Level 2 → 3 questions (testing practical experience)
- "Tell me about a project where you used [skill]. What went well? What didn't?"
- "How would you approach [realistic scenario]? Walk me through your thinking."
- "What's the biggest mistake you've made with [topic] and what did you learn?"

### Level 3 → 4 questions (testing depth)
- "If you had to teach [advanced concept] to a beginner, how would you explain it?"
- "What are the limitations of [standard approach] and when would you not use it?"
- "How has your thinking about [topic] changed over time?"

## Adaptive Question Flow

1. **Start at expected level**: Ask 2 questions at the level you think they might be (based on what they told you)
2. **Adjust up or down**: If they nail both → ask 2 more at next level up. If they struggle → ask 2 more at level down.
3. **Stop when level is clear**: You don't need 10 questions. Once the pattern is consistent, stop.
4. **Confirm**: "Based on your answers, I'd place you at approximately Level [N]. Does that feel right to you?"

## Gap Analysis Output

After assessment, produce a concise summary:

```
Current level: [N/4] — [label]
Target level: [M/4] — [what they want to achieve]

Main gaps:
1. [Gap 1] — currently at [X], need [Y]
2. [Gap 2] — currently at [X], need [Y]
3. [Gap 3] — currently at [X], need [Y]

Estimated effort: [time] at [hours/week]
```

## Special Cases

- **Complete beginner (Level 0)**: Skip assessment questions. Just confirm interest and start from zero.
- **Career changer**: Focus questions on transferable skills. "What from your current role might help with [topic]?"
- **Self-taught practitioner**: They often have gaps in fundamentals. Test the basics even if they seem advanced.
