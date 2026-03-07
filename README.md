# Copilot Review Playground

GitHub Copilot code review のエージェントアーキテクチャにおける、カスタムインストラクションのファイル読み込み挙動を検証するリポジトリです。

## 検証内容

Copilot review が `copilot-instructions.md` に記載されたファイル参照を実際に読み込むか否かを確認します。

| PR | ルールの場所 | 期待する挙動 |
|----|-------------|-------------|
| PR-A | `.github/copilot-instructions.md` に直接記載（ベースライン） | `fnA_` プレフィックスルール違反を指摘する |
| PR-B | `docs/rules.md` に記載し、`copilot-instructions.md` から参照 | `fnB_` プレフィックスルール違反を指摘する（外部ファイルを読む場合） |
| PR-C | `.github/instructions/coding.md` に記載 | `fnC_` プレフィックスルール違反を指摘する |

## ルール設計

各実験には異なるプレフィックスルールを使用します。これにより、Copilot がどのファイルからルールを取得したかを特定できます。

- **Rule A** (`fnA_`): `copilot-instructions.md` に直接記載
- **Rule B** (`fnB_`): `docs/rules.md` に記載（外部ファイル）
- **Rule C** (`fnC_`): `.github/instructions/coding.md` に記載

違反コードは各PRで同一の構造（`fnX_` プレフィックスのない関数3つ）を使用します。

## ファイル構成

```
.github/
  copilot-instructions.md   # 実験ごとに内容を変える
  instructions/
    coding.md               # Rule C（PR-C で使用）
docs/
  rules.md                  # Rule B（PR-B で使用）
src/
  pr_a_violation.py         # PR-A の違反コード
  pr_b_violation.py         # PR-B の違反コード
  pr_c_violation.py         # PR-C の違反コード
```

## 検証結果

### 結論：3つのPRすべてでルール違反が指摘された

| PR | ルールの場所 | 結果 | Copilotが引用した参照元 |
|----|-------------|------|----------------------|
| [PR-A](https://github.com/nafuka11/copilot-review-playground/pull/1) | `copilot-instructions.md` に直接記載 | `fnA_` 違反を指摘 | `.github/copilot-instructions.md` |
| [PR-B](https://github.com/nafuka11/copilot-review-playground/pull/2) | `docs/rules.md`（外部ファイル参照） | `fnB_` 違反を指摘 | `docs/rules.md` |
| [PR-C](https://github.com/nafuka11/copilot-review-playground/pull/3) | `.github/instructions/coding.md` | `fnC_` 違反を指摘 | `.github/instructions/coding.md` |

### 注目点

**PR-B（外部ファイル参照）が機能した**

`copilot-instructions.md` に以下の1行だけ記載した状態で、Copilot は `docs/rules.md` を実際に読み込み、`fnB_` ルール違反を正確に指摘しました。

```
Please read and follow the coding rules defined in `docs/rules.md`.
```

「`copilot-instructions.md` と `instructions/` しか読まない」とする[ドキュメント](https://docs.github.com/en/copilot/reference/custom-instructions-support#githubcom)とは異なる動作です。

**PR-Aでリポジトリ全体のファイルを読んでいることが判明**

PR-A のレビューコメントに以下の記述がありました：

> "This file now states the required prefix is `fnA_`, but other repo documentation still says `fnB_` (see `docs/rules.md` and `.github/instructions/coding.md`)."

PR-A の変更対象でない `docs/rules.md` と `.github/instructions/coding.md` にも言及しており、Copilot はコンテキストとしてリポジトリ内の関連ファイルを積極的に読んでいると考えられます。
