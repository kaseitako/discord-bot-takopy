# discord-bot-takopy

Nextcord library を使用した Discord bot です。

## 機能

- `/ping` - bot が応答しているかの確認
- `/echo <message>` - メッセージをオウム返し

## セットアップ

### 1. Poetry のインストール

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. 依存関係のインストール

```bash
poetry install
```

### 3. 環境変数の設定

`.env` ファイルに Discord bot トークンとサーバー ID を設定してください：

```
DISCORD_BOT_TOKEN=your_bot_token_here
SERVER_ID=your_server_id_here
```

### 4. bot の起動

```bash
poetry run python discord_bot_takopy/main.py
```

## 開発環境

- Python 3.12 以上
- Nextcord 3.0.1 以上
- Poetry（パッケージ管理）

## トラブルシューティング

### Poetry install でエラーが出る場合

1. `poetry lock --no-update` で lock ファイルを更新
2. 再度 `poetry install` を実行

### Python バージョンエラーの場合

pyproject.toml の Python 要求バージョンを確認してください（現在は 3.12 以上）。

## Docker を使用する場合

Docker を使用して bot をコンテナデプロイできます。

### 前提条件

- Docker Desktop

### 使用方法

1. イメージをビルド：
```bash
docker build -t discord-bot-takopy .
```

2. コンテナを実行：
```bash
docker run -e DISCORD_BOT_TOKEN="your_token" -e SERVER_ID="your_server_id" discord-bot-takopy
```

### 環境変数ファイルを使用する場合

`.env` ファイルがある場合：
```bash
docker run --env-file .env discord-bot-takopy
```

## Dev Container を使用する場合

VS Code の Dev Container 機能を使用すると、一貫した開発環境を構築できます。

### 前提条件

- Docker Desktop
- VS Code
- Dev Containers 拡張機能

### 使用方法

1. VS Code でプロジェクトを開く
2. コマンドパレット（Ctrl+Shift+P）で "Dev Containers: Reopen in Container" を選択
3. 初回はコンテナの構築に時間がかかります
4. 構築完了後、コンテナ内で開発が可能になります

Dev Container には以下が含まれます：

- Python 3.12
- Poetry
- Claude Code CLI
- Git（最新版）
- 必要な VS Code 拡張機能（Python、Pylint、isort、debugpy）