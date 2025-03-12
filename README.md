# ml-project-template

<a href="https://opensource.org/licenses/MIT">
    <img alt="python versions" src="https://img.shields.io/badge/python-3.12-blue?color=5271FF">
</a>
<a href="https://opensource.org/licenses/MIT">
    <img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green?color=5271FF">
</a>
<a href="https://github.com/astral-sh/ruff">
    <img alt="Ruff" src="https://img.shields.io/badge/code%20style-Ruff-000000.svg?color=5271FF">
</a>
<a href="https://github.com/python/mypy">
    <img alt="mypy" src="https://img.shields.io/badge/typing-mypy-blue?color=5271FF">
</a>

VSCode × Docker × Pythonでの機械学習リポジトリのテンプレート🥳🥳🥳

## Environment

### ローカル環境

uvインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh && exec $SHELL -l
```

CPU環境用

```bash
uv python pin "$(cat .python-version)" && uv sync --extra cpu
```

GPU環境用

```bash
uv python pin "$(cat .python-version)" && uv sync --extra cuda
```

### Docker環境

CPU環境用

```bash
docker compose up -d --build cpu
```

GPU環境用

```bash
docker compose up -d --build cuda
```

> [!WARNING]
> macで以下のエラーが出ることがあります
>
> ```bash
> failed to solve with frontend dockerfile.v0: failed to create LLB definition: rpc error: code = Unknown desc = error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
> ```
>
> その場合は以下の手順で`~/.docker/config.json`を修正すると解決できます
>
> - `sudo vi ~/.docker/config.json`でファイルを開く
> - `credsStore` -> `credStore`に変更し保存
> <https://stackoverflow.com/a/74413229>

#### コンテナにアタッチ

次にVScode左下の`><`ボタンより`コンテナで再度開く`でコンテナにアクセス

#### 拡張機能インストール

無事コンテナが開いたら, 「拡張機能の推奨事項があります」という通知が出ると思います.
この通知を許可すると, `.vscode/extensions.json`に記載されている拡張機能が自動的にインストールされます.
もし通知が出なかった場合は, 左のメニューから`拡張機能`を選択し, `フィルターアイコン`->`推奨`‐>`インストールアイコン`を押せば一括インストールできます.
