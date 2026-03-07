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
