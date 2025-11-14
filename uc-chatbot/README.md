# UCチャットボット

UCさんについての質問に答えるAIチャットボットです。

## 特徴

- UCさんの人格、経歴、実績についての詳細な知識ベース
- Claude APIによる自然な会話（オプション）
- キーワードベースのフォールバック応答システム
- WordPressへの簡単な埋め込み
- レスポンシブデザイン

## セットアップ手順

### 1. 依存関係のインストール

```bash
npm install
```

### 2. 環境変数の設定（オプション）

```bash
cp .env.example .env
```

`.env`ファイルを編集して、Anthropic APIキーを設定してください。
APIキーがない場合は、キーワードベースの応答システムが自動的に使用されます。

Anthropic APIキーの取得方法：
1. https://console.anthropic.com/ にアクセス
2. アカウントを作成
3. API Keysセクションでキーを生成

### 3. サーバーの起動

```bash
npm start
```

または開発モード（自動再起動付き）：

```bash
npm run dev
```

サーバーは http://localhost:3000 で起動します。

### 4. チャットボットのテスト

ブラウザで以下のURLにアクセス：

```
http://localhost:3000/chatbot-widget.html
```

## WordPressへの埋め込み

### 方法1: カスタムHTMLウィジェット

1. WordPressダッシュボードにログイン
2. **外観 > ウィジェット** に移動
3. 「カスタムHTML」ウィジェットを追加
4. `wordpress-embed-code.html` の内容をコピー&ペースト
5. **API_URL** を本番環境のURLに変更：
   ```javascript
   const API_URL = 'https://your-domain.com:3000/api/chat';
   ```
6. 保存

### 方法2: 固定ページ/投稿に埋め込む

1. 固定ページまたは投稿を編集
2. カスタムHTMLブロックを追加
3. `wordpress-embed-code.html` の内容をペースト
4. **API_URL** を本番環境のURLに変更
5. 公開

### 方法3: テーマのfooter.phpに追加

1. **外観 > テーマファイルエディター**
2. `footer.php` を開く
3. `</body>` タグの直前に `wordpress-embed-code.html` の内容を追加
4. **API_URL** を本番環境のURLに変更
5. ファイルを更新

## 本番環境へのデプロイ

### サーバーの常駐化

PM2を使用してサーバーを常駐化することをお勧めします：

```bash
npm install -g pm2
pm2 start chatbot-server.js --name uc-chatbot
pm2 save
pm2 startup
```

### リバースプロキシの設定（Nginx）

Nginxを使用してリバースプロキシを設定すると、HTTPSでアクセスできます：

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /path/to/ssl/cert.pem;
    ssl_certificate_key /path/to/ssl/key.pem;

    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## APIエンドポイント

### POST /api/chat

チャットメッセージを送信します。

**リクエスト:**
```json
{
  "message": "UCって誰ですか？",
  "history": []
}
```

**レスポンス:**
```json
{
  "response": "UCは中嶋雄士さんのニックネームです！...",
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

### GET /api/health

サーバーのヘルスチェック。

**レスポンス:**
```json
{
  "status": "ok",
  "knowledgeBaseLoaded": true,
  "hasAnthropicKey": false
}
```

### GET /api/knowledge

知識ベースの内容を取得（デバッグ用）。

## ファイル構成

```
uc-site/
├── chatbot-server.js          # バックエンドサーバー
├── package.json                # Node.js依存関係
├── .env.example                # 環境変数テンプレート
├── .env                        # 環境変数（作成が必要）
├── uc-knowledge-base.json      # UCさんの知識ベース
├── CLAUDE.md                   # 認証情報
├── README.md                   # このファイル
├── wordpress-embed-code.html   # WordPress埋め込みコード
└── public/
    └── chatbot-widget.html     # スタンドアロンチャットウィジェット
```

## カスタマイズ

### デザインのカスタマイズ

`wordpress-embed-code.html` または `public/chatbot-widget.html` のCSSセクションを編集してください。

主なカスタマイズポイント：
- カラースキーム（グラデーション）
- ボタンサイズと位置
- チャットウィンドウのサイズ
- フォント

### 知識ベースの更新

`uc-knowledge-base.json` を編集して、UCさんの情報を追加・更新できます。

### 応答のカスタマイズ

`chatbot-server.js` の `getKeywordBasedResponse()` 関数を編集して、キーワードベースの応答をカスタマイズできます。

## トラブルシューティング

### チャットボットが応答しない

1. サーバーが起動しているか確認：
   ```bash
   npm start
   ```

2. API URLが正しいか確認（`wordpress-embed-code.html`）

3. ブラウザのコンソールでエラーを確認

### CORS エラーが発生する

`chatbot-server.js` のCORS設定を確認してください。本番環境では特定のドメインのみ許可することをお勧めします。

### Anthropic API エラー

1. APIキーが正しく設定されているか確認
2. APIクレジットが残っているか確認
3. APIキーがない場合は自動的にキーワードベースの応答に切り替わります

## ライセンス

MIT

## サポート

問題や質問がある場合は、UCさんに直接連絡してください！
