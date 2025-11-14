# UCチャットボット - 本番環境デプロイガイド

## 現在の状態

✅ **完了したこと:**
- UCさんの知識ベース作成（uc-knowledge-base.json）
- チャットボットバックエンドサーバー作成（Node.js + Express）
- フロントエンドチャットウィジェット作成
- WordPressページ作成（https://uc.x0.com/ucチャットボット/）
- ローカルサーバーでのテスト完了

⚠️ **残りの作業:**
- サーバーを本番環境にデプロイ
- 外部からアクセスできるようにする

## デプロイ方法

### オプション1: PM2で常駐化（推奨）

PM2を使用すると、サーバーが常に動作し、再起動時にも自動的に起動します。

```bash
# PM2をグローバルにインストール
npm install -g pm2

# チャットボットサーバーを起動
cd /home/uc/uc-site
pm2 start chatbot-server.js --name uc-chatbot

# 設定を保存
pm2 save

# システム起動時に自動起動するように設定
pm2 startup

# ステータス確認
pm2 status

# ログ確認
pm2 logs uc-chatbot

# 再起動
pm2 restart uc-chatbot

# 停止
pm2 stop uc-chatbot
```

### オプション2: Nginxでリバースプロキシ設定（HTTPS対応）

Nginxを使用すると、HTTPSでアクセスでき、ドメイン名を使用できます。

1. **Nginxインストール（まだの場合）:**

```bash
sudo apt update
sudo apt install nginx
```

2. **SSL証明書取得（Let's Encrypt）:**

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d uc.x0.com
```

3. **Nginx設定ファイル作成:**

```bash
sudo nano /etc/nginx/sites-available/uc-chatbot
```

以下の内容を追加：

```nginx
server {
    listen 443 ssl;
    server_name uc.x0.com;

    ssl_certificate /etc/letsencrypt/live/uc.x0.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/uc.x0.com/privkey.pem;

    # チャットボットAPI用
    location /chatbot-api/ {
        proxy_pass http://localhost:3000/api/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

4. **設定を有効化:**

```bash
sudo ln -s /etc/nginx/sites-available/uc-chatbot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

5. **wordpress-embed-code.html のAPI_URLを更新:**

```javascript
const API_URL = 'https://uc.x0.com/chatbot-api/chat';
```

### オプション3: シンプルなポート公開（テスト用のみ）

**⚠️ セキュリティリスクあり。本番環境では推奨しません。**

```bash
# ファイアウォールでポート3000を開く
sudo ufw allow 3000

# サーバーを起動
cd /home/uc/uc-site
npm start
```

wordpress-embed-code.html のAPI_URLを更新：

```javascript
const API_URL = 'http://your-server-ip:3000/api/chat';
```

## Anthropic Claude API設定（オプション）

より自然な会話を実現するには、Anthropic Claude APIを設定します。

1. **APIキー取得:**
   - https://console.anthropic.com/ にアクセス
   - アカウント作成
   - API Keysセクションでキーを生成

2. **環境変数設定:**

```bash
cd /home/uc/uc-site
cp .env.example .env
nano .env
```

以下を追加：

```
ANTHROPIC_API_KEY=sk-ant-xxxxx
PORT=3000
```

3. **サーバー再起動:**

```bash
pm2 restart uc-chatbot
```

## WordPressへの統合

### 現在のページ

チャットボット説明ページが作成されました：
- URL: https://uc.x0.com/ucチャットボット/
- ページID: 180

### サイト全体に表示する方法

全ページにチャットボットを表示するには：

1. **WordPressダッシュボードにログイン**

2. **外観 > ウィジェット**

3. **「カスタムHTML」ウィジェットをフッターエリアに追加**

4. **wordpress-embed-code.html の内容をコピー&ペースト**

5. **API_URLを本番環境のURLに変更:**

```javascript
// 変更前
const API_URL = 'http://localhost:3000/api/chat';

// 変更後（Nginxを使用する場合）
const API_URL = 'https://uc.x0.com/chatbot-api/chat';

// または（ポート公開の場合）
const API_URL = 'http://your-server-ip:3000/api/chat';
```

6. **保存**

## トラブルシューティング

### サーバーが起動しない

```bash
# ログ確認
pm2 logs uc-chatbot

# ポートが使用中か確認
sudo lsof -i :3000

# 依存関係を再インストール
cd /home/uc/uc-site
rm -rf node_modules
npm install
```

### チャットボットが応答しない

1. サーバーのステータス確認:
   ```bash
   pm2 status
   ```

2. ヘルスチェック:
   ```bash
   curl http://localhost:3000/api/health
   ```

3. ブラウザのコンソールでエラー確認

### CORS エラー

chatbot-server.js のCORS設定を確認:

```javascript
app.use(cors({
  origin: 'https://uc.x0.com',  // WordPressのドメインを指定
  credentials: true
}));
```

## メンテナンス

### ログの確認

```bash
pm2 logs uc-chatbot --lines 100
```

### サーバーの再起動

```bash
pm2 restart uc-chatbot
```

### サーバーの停止

```bash
pm2 stop uc-chatbot
```

### 知識ベースの更新

1. uc-knowledge-base.json を編集
2. サーバーを再起動: `pm2 restart uc-chatbot`

## セキュリティ

### 本番環境での推奨事項

1. **HTTPS を使用** - Let's Encrypt + Nginx
2. **環境変数でAPIキーを管理** - .envファイルを使用
3. **CORS設定を厳格化** - 特定のドメインのみ許可
4. **レート制限を実装** - 悪用を防ぐ
5. **定期的なアップデート** - 依存関係を最新に保つ

```bash
# 依存関係の更新
cd /home/uc/uc-site
npm update
pm2 restart uc-chatbot
```

## サポート

問題が発生した場合は、以下を確認してください：

1. README.md - 基本的なセットアップ手順
2. pm2 logs - サーバーログ
3. ブラウザコンソール - フロントエンドエラー

---

**作成日:** 2024年
**最終更新:** 2024年
