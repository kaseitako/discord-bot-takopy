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