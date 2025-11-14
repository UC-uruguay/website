# さくらインターネットへのデプロイガイド

## 現在の状況

✅ **完了:**
- UCさんの情報を修正（中嶋雄士、福岡出身）
- Anthropic APIキー設定（.envファイルに安全に保存）
- ローカルサーバー動作確認

⚠️ **注意:**
- Anthropic APIのクレジット残高が不足していますが、キーワードベースの応答システムは正常動作
- クレジットを追加すると、より自然な会話が可能になります

## さくらインターネットの種類

さくらインターネットには複数のサービスがあります：

### 1. さくらのレンタルサーバー
- **Node.jsサポート**: プランによって異なる
- **推奨**: 外部サービス（Vercel、Railway等）にデプロイしてAPIを提供

### 2. さくらのVPS / クラウド
- **Node.jsサポート**: フルサポート
- **推奨**: 直接Node.jsサーバーを動かせる

## デプロイ方法

### オプション1: 外部サービス（Railway）にデプロイ【推奨・無料】

Railwayは無料でNode.jsアプリをホスティングできます。

#### 手順:

1. **Railwayアカウント作成**
   - https://railway.app/ にアクセス
   - GitHubでログイン

2. **新しいプロジェクト作成**
   ```bash
   # GitHubリポジトリにプッシュ
   cd /home/uc/uc-site
   git init
   git add .
   git commit -m "Initial commit: UC chatbot"

   # GitHubにリポジトリ作成（ブラウザで）
   # その後
   git remote add origin https://github.com/your-username/uc-chatbot.git
   git push -u origin main
   ```

3. **Railwayでデプロイ**
   - Railway ダッシュボード > New Project
   - Deploy from GitHub repo を選択
   - uc-chatbot リポジトリを選択
   - 環境変数を設定:
     - `ANTHROPIC_API_KEY`: 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
     - `PORT`: 3000
     - `NODE_ENV`: production

4. **デプロイURL取得**
   - Railwayが自動でURLを発行: `https://uc-chatbot-xxx.up.railway.app`

5. **WordPress埋め込みコード更新**
   ```javascript
   const API_URL = 'https://uc-chatbot-xxx.up.railway.app/api/chat';
   ```

### オプション2: Vercelにデプロイ【無料・簡単】

1. **Vercelアカウント作成**
   - https://vercel.com にアクセス
   - GitHubでログイン

2. **vercel.json 作成**
   ```bash
   cd /home/uc/uc-site
   ```

3. **Vercel CLIでデプロイ**
   ```bash
   npm install -g vercel
   vercel login
   vercel --prod
   ```

4. **環境変数設定**
   - Vercel ダッシュボード > Settings > Environment Variables
   - `ANTHROPIC_API_KEY` を追加

### オプション3: さくらのVPS / クラウド【有料】

さくらのVPSまたはクラウドを使用している場合：

#### 1. サーバーにSSH接続

```bash
ssh user@your-sakura-server.jp
```

#### 2. Node.jsインストール

```bash
# nvm経由でNode.js をインストール
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 22
node --version
```

#### 3. ファイルをアップロード

```bash
# ローカルから
scp -r /home/uc/uc-site user@your-sakura-server.jp:/home/user/
```

または

```bash
# サーバー上で
cd /home/user
git clone https://github.com/your-username/uc-chatbot.git
cd uc-chatbot
```

#### 4. 依存関係インストール

```bash
cd /home/user/uc-site
npm install
```

#### 5. .envファイル作成

```bash
nano .env
```

以下を追加:
```
ANTHROPIC_API_KEY=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
PORT=3000
NODE_ENV=production
```

保存: Ctrl+X, Y, Enter

#### 6. PM2で常駐化

```bash
npm install -g pm2
pm2 start chatbot-server.js --name uc-chatbot
pm2 save
pm2 startup
```

#### 7. Nginxでリバースプロキシ設定

```bash
sudo apt install nginx
sudo nano /etc/nginx/sites-available/uc-chatbot
```

以下を追加:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /chatbot-api/ {
        proxy_pass http://localhost:3000/api/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

有効化:
```bash
sudo ln -s /etc/nginx/sites-available/uc-chatbot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

#### 8. SSL証明書（Let's Encrypt）

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## WordPressに統合

### 方法1: サイト全体にチャットボットを表示

1. **WordPressダッシュボード** にログイン: https://uc.x0.com/wp-admin/

2. **外観 > カスタマイズ > 追加CSS** または **外観 > テーマファイルエディター**

3. **footer.php** を編集（または「追加のCSS」と「カスタムHTML」ウィジェット使用）

4. **wordpress-embed-code.html の内容をコピー**して以下を修正:

```javascript
// API_URLを本番環境のURLに変更
const API_URL = 'https://your-railway-app.up.railway.app/api/chat';
// または
const API_URL = 'https://your-domain.com/chatbot-api/chat';
```

5. **保存**

### 方法2: WP Code Snippetsプラグイン使用【推奨】

1. **プラグインインストール**
   - ダッシュボード > プラグイン > 新規追加
   - "WP Code" または "Code Snippets" で検索
   - インストール & 有効化

2. **新しいスニペット作成**
   - Code Snippets > Add New
   - タイトル: "UC Chatbot"
   - コードタイプ: HTML Snippet
   - wordpress-embed-code.html の内容をペースト
   - API_URLを本番環境のURLに変更
   - 場所: Footer
   - 保存 & 有効化

## 動作確認

1. **サーバー確認**
   ```bash
   curl https://your-api-url/api/health
   ```

2. **WordPressサイトで確認**
   - https://uc.x0.com/ にアクセス
   - 右下にチャットボタンが表示されるはず

3. **テスト質問**
   - "UCは何歳ですか？" → 34歳と回答
   - "出身はどこですか？" → 福岡県と回答
   - "本名は？" → 中嶋雄士と回答

## APIクレジットについて

現在のAnthropicAPIキーのクレジット残高が不足しています。

### クレジット追加方法:

1. **Anthropic Console にアクセス**
   - https://console.anthropic.com/

2. **Plans & Billing**
   - クレジットカードを登録
   - クレジットを購入（$5から）

3. **サーバー再起動**
   ```bash
   pm2 restart uc-chatbot
   # または Railwayで自動再デプロイ
   ```

### クレジットがない場合:

キーワードベースの応答システムが自動的に使用されます。基本的な質問には十分対応できます。

## セキュリティ

### ✅ 実装済み:

- `.env` ファイルに機密情報を保存
- `.gitignore` で `.env` を除外
- ファイル権限を600に設定（`chmod 600 .env`）

### 追加推奨:

1. **環境変数をサーバーで設定**（Railwayの場合は自動）

2. **CORS設定を厳格化**
   ```javascript
   app.use(cors({
     origin: 'https://uc.x0.com',
     credentials: true
   }));
   ```

3. **レート制限**
   ```bash
   npm install express-rate-limit
   ```

## トラブルシューティング

### チャットボットが表示されない

1. ブラウザのコンソールを確認（F12）
2. API URLが正しいか確認
3. CORSエラーがないか確認

### APIが応答しない

```bash
# サーバー確認
pm2 status
pm2 logs uc-chatbot

# ヘルスチェック
curl https://your-api-url/api/health
```

### Anthropic APIエラー

- クレジット残高を確認
- APIキーが正しいか確認
- `.env` ファイルが読み込まれているか確認

## まとめ

**最も簡単な方法:**
1. Railwayにデプロイ（無料、5分で完了）
2. 発行されたURLをwordpress-embed-code.htmlに設定
3. WordPressにWP Codeプラグインでスニペット追加

**ローカルテスト:**
```bash
cd /home/uc/uc-site
node chatbot-server.js
# ブラウザで http://localhost:3000/chatbot-widget.html
```

**質問・サポート:**
- README.md - 基本セットアップ
- DEPLOYMENT.md - 詳細デプロイ手順
- このファイル - さくらインターネット特化
