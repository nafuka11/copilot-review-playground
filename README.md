# Copilot Review Playground

GitHub Copilot code review のエージェントアーキテクチャにおける、カスタムインストラクションのファイル読み込み挙動を検証するリポジトリです。

## 検証内容

Copilot review がどのファイルをプロアクティブに読み込むかを確認します。各実験では、ベースブランチにルールを配置済みの状態で、PRには違反コードのみを含めます（ルールファイル自体は PR の差分に含めない）。

| 実験 | ルールの場所 | PR |
|------|------------|-----|
| A | `.github/copilot-instructions.md` に直接記載 | [PR-A2](https://github.com/nafuka11/copilot-review-playground/pull/6) |
| B | `docs/rules.md` に記載し、`copilot-instructions.md` から参照 | [PR-B2](https://github.com/nafuka11/copilot-review-playground/pull/7) |
| C | `.github/instructions/coding.md` に記載 | [PR-C](https://github.com/nafuka11/copilot-review-playground/pull/3) |
| D | `.github/skills/naming-convention/SKILL.md` に記載 | [PR-D2](https://github.com/nafuka11/copilot-review-playground/pull/5) |

## ルール設計

各実験には異なるプレフィックスルールを使用します。これにより、Copilot がどのファイルからルールを取得したかを特定できます。

- **Rule A** (`fnA_`): `copilot-instructions.md` に直接記載
- **Rule B** (`fnB_`): `docs/rules.md` に記載（外部ファイル）
- **Rule C** (`fnC_`): `.github/instructions/coding.md` に記載
- **Rule D** (`fnD_`): `.github/skills/naming-convention/SKILL.md` に記載

違反コードは各PRで同一の構造（`fnX_` プレフィックスのない関数3つ）を使用します。

## ファイル構成

```
.github/
  copilot-instructions.md       # 実験ごとに内容を変える
  instructions/
    coding.md                   # Rule C（実験 C で使用）
  skills/
    naming-convention/
      SKILL.md                  # Rule D（実験 D で使用）
docs/
  rules.md                      # Rule B（実験 B で使用）
src/
  pr_a2_violation.py            # 実験 A の違反コード
  pr_b2_violation.py            # 実験 B の違反コード
  pr_c_violation.py             # 実験 C の違反コード
  pr_d2_violation.py            # 実験 D の違反コード
```

## 検証結果

| 実験 | ルールの場所 | 結果 |
|------|------------|------|
| A | `.github/copilot-instructions.md` | **読まれる** |
| B | `docs/rules.md`（`copilot-instructions.md` から参照） | **読まれる** |
| C | `.github/instructions/coding.md` | **読まれる** |
| D | `.github/skills/naming-convention/SKILL.md` | **読まれない** |

### 実験 A：`copilot-instructions.md` は常に読まれる

`fnA_` 違反を3件すべて指摘。ベースブランチに存在する `copilot-instructions.md` はプロアクティブに読み込まれます。

### 実験 B：`copilot-instructions.md` から参照した外部ファイルも読まれる

`copilot-instructions.md` に以下の1行だけ記載した状態で、Copilot は `docs/rules.md` を実際に読み込み、`fnB_` 違反を指摘しました。

```
Please read and follow the coding rules defined in `docs/rules.md`.
```

「`copilot-instructions.md` と `instructions/` しか読まない」とする[ドキュメント](https://docs.github.com/en/copilot/reference/custom-instructions-support#githubcom)とは異なり、参照先の外部ファイルも読み込まれます。

### 実験 C：`.github/instructions/` は常に読まれる

`fnC_` 違反を3件すべて指摘。`copilot-instructions.md` に記載がなくても `.github/instructions/` 配下のファイルはプロアクティブに読み込まれます。

### 実験 D：`.github/skills/` は読まれない

`fnD_` 違反は指摘されませんでした。`.github/skills/` はドキュメント通り coding agent 向けの機能であり、code review では読み込まれません。
