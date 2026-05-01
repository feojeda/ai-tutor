# AI Tutor

**あらゆるCLIエージェント（OpenCode、Claude Code、Gemini、Codex）を、あなたが学びたいことを教えるソクラテス式のチューターに変えます。**

[English](../README.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [中文](README.zh.md) | [日本語](README.ja.md)

---

## 🚀 インストール

```bash
git clone https://github.com/feojeda/ai-tutor.git ~/.ai-tutor && python3 ~/.ai-tutor/install.py
```

### エージェントにインストールを依頼する

任意のCLIエージェントにこれを貼り付けてください：

```
https://github.com/feojeda/ai-tutor.git を ~/.ai-tutor にクローンし、python3 ~/.ai-tutor/install.py を実行してください。その後、検出されたエージェントを教えてください。
```

### アンインストール

```bash
python3 ~/.ai-tutor/install.py --uninstall && rm -rf ~/.ai-tutor
```

インストーラーはインストール済みのエージェントを検出し、スキルを適切な場所にコピーします：

```
✅ OpenCode: Installed → ~/.opencode/skills/tutor/
✅ Claude Code: Installed → ~/.claude/skills/tutor/
✅ コース 'ejemplo-ml': Installed → ~/.ai-tutor/cursos/ejemplo-ml/
```

### オプション

```bash
python install.py --list          # 検出されたエージェントを表示
python install.py --agent opencode # 特定のエージェントのみにインストール
python install.py --dry-run       # 変更せずにプレビュー
python install.py --uninstall     # すべてのエージェントから削除
python install.py --course name   # 特定のコースをインストール
```

---

## これは何か

マークダウン形式のスキルとコースのセットで、コーディングエージェントに読み込むと対話型の教師に変身します。情報を一方的に吐き出すのではなく、質問を投げかけ、理解度を確認し、あなたのレベルに合わせてペースを調整します。

2つの要素：

- **チュータースキル** (`skills/tutor/SKILL.md`) — どのように教えるかを定義：ソクラテス式メソッド、理解度チェック、適応型ペース配分。トピックに依存しません。
- **コース** (`cursos/`) — 何を教えるかを定義：カリキュラム、演習、プロジェクト。1トピックにつき1コース。

---

## 使い方

インストール後、エージェントを開いてこう言ってください：

```
「チュータースキルを読み込んで。機械学習について学びたい。」
```

エージェントが教育ルールを読み込み、セッションごとにガイドを開始します。

---

## 対応エージェント

| エージェント | スキルの場所 | 起動方法 |
|------------|------------|---------|
| [OpenCode](https://github.com/nousresearch/opencode) | `~/.opencode/skills/tutor/` | `@tutor` |
| [Claude Code](https://claude.ai/code) | `~/.claude/skills/tutor/` | `/tutor` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `~/.gemini/tools/tutor/` | `:tutor` |
| [Codex CLI](https://github.com/openai/codex) | `~/.codex/skills/tutor/` | `!tutor` |

---

## 利用可能なコース

### `ejemplo-ml` — 機械学習をゼロから
4-5セッション。「MLとは何か」から scikit-learn を使った初めての分類器の訓練まで。前提条件：Pythonの基礎。

---

## 自分のコースを作成する

1. `cursos/ejemplo-ml/` を新しい名前でコピー
2. `curriculum.md` を自分のコンテンツで編集
3. `ejercicios/` に演習を追加
4. `python install.py --course あなたのコース` を実行

コースの構造：

```
cursos/あなたのコース/
├── curriculum.md    ← 学習計画（セッション、目標、演習）
├── rules.md         ← （オプション）トピック固有の教育ルール
└── ejercicios/      ← （オプション）詳細な演習
    ├── 01-intro.md
    └── 02-advanced.md
```

### 良いカリキュラムのためのルール

1. **1セッション = 1つの概念。** 1つのセッションに2つの新しいアイデアを詰め込まない。
2. **理論の後に演習。** すべてのセッションに少なくとも1つの実践演習が必要。
3. **理解度チェック。** 学習を確認する質問で各セッションを終える。
4. **明確な前提条件。** 学習者は始める前に何が必要かを正確に把握できること。
5. **実例。** おもちゃの例ではなく、現実世界のデータと問題を使用する。

---

## 哲学

ほとんどの人は別のYouTubeチュートリアルを必要としていません。必要なのは：
- 適切なタイミングで適切な質問をしてくれる人
- 理解できていないことに気づき、戻ってくれる人
- 小さな進歩を称えてくれる人
- 実際のレベルにペースを合わせてくれる人

適切なルールを持つLLMはそれを実現できます。このプロジェクトはそのルールを提供します。

---

## ライセンス

MIT。これを使って、誰にでも、何でも教えてください。
