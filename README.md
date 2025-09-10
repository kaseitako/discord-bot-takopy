# discord-bot-takopy

Nextcord library を使用した Discord bot。

## 開発環境

VS Code の Dev Container 機能を使用して開発する。

### 使用方法

1. VS Code でプロジェクトを開く
2. コマンドパレット（Ctrl+Shift+P）で "Dev Containers: Reopen in Container" を選択
3. 初回はコンテナの構築に時間がかかる
4. 構築完了後、コンテナ内で開発が可能になる

### Dev Container に含まれるもの

- Python 3.12
- Poetry（依存関係管理）
- Claude Code CLI
- Git（最新版）
- VS Code 拡張機能（Python、Pylint、isort、debugpy）

### 開発時の環境変数設定

開発時は `.env` ファイルをプロジェクトルートに作成し、必要な環境変数を設定する
必要な変数は [## 必要な環境変数](#必要な環境変数) を参照。


## 必要な環境変数

bot を動作させるために以下の環境変数を設定する必要がある

| 環境変数 | 説明 | 取得方法 |
|---------|------|---------|
| `DISCORD_BOT_TOKEN` | Discord bot のトークン | [Discord Developer Portal](https://discord.com/developers/applications) でアプリケーションを作成し、Bot セクションでトークンを生成 |
| `SERVER_ID` | bot を使用するサーバーの ID | Discord でサーバーを右クリックして「ID をコピー」（開発者モードを有効にする必要がある） |


## デプロイ方法

このリポジトリには GitHub Actions ワークフローが設定されており、main ブランチにマージされると自動的に Docker イメージが GitHub Container Registry にプッシュされる。

### 自動デプロイの流れ

1. main ブランチへのプッシュまたはプルリクエストのマージ
2. GitHub Actions が Docker イメージをビルド
3. GitHub Container Registry (`ghcr.io`) にイメージをプッシュ
4. タグ付け：`latest`、ブランチ名、コミット SHA

### イメージの取得と実行

```bash
# イメージを取得
docker pull ghcr.io/[your-username]/discord-bot-takopy:latest

# コンテナを実行
docker run -e DISCORD_BOT_TOKEN="your_token" -e SERVER_ID="your_server_id" ghcr.io/[your-username]/discord-bot-takopy:latest
```

## ローカルでの Docker 使用

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
