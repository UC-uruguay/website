# UCチャットボット - プロジェクトサマリー

## 🎉 完成しました！

UCさんに関する質問に答えるAIチャットボットを作成し、WordPressサイトに統合しました。

---

## 📦 作成されたファイル

### コアファイル
- **chatbot-server.js** - Node.js + Expressバックエンドサーバー
- **uc-knowledge-base.json** - UCさんの詳細な知識ベース
- **package.json** - Node.js依存関係

### フロントエンド
- **public/chatbot-widget.html** - スタンドアロンチャットウィジェット
- **wordpress-embed-code.html** - WordPress埋め込み用コード

### デプロイ・設定
- **deploy-to-wordpress.py** - WordPress自動デプロイスクリプト
- **.env.example** - 環境変数テンプレート
- **CLAUDE.md** - WordPress認証情報

### ドキュメント
- **README.md** - セットアップ手順と使用方法
- **DEPLOYMENT.md** - 本番環境デプロイガイド
- **SUMMARY.md** - このファイル

---

## ✨ 主な機能

### 1. 豊富な知識ベース

UCさんについての詳細情報：
- 個人情報（名前、生年月日、家族構成）
- 哲学と価値観（「とりあえず」精神、人生の目標）
- 経歴（学歴、職歴、起業）
- 会社（TORIAEZU OÜ、Chant-through）
- 実績（サハラマラソン、エベレスト、タイムカプセル、UC少額奨学金）
- プロジェクト（例のプールパーティー、オンラインベビーシッター）
- 趣味、友達哲学、将来の目標

### 2. インテリジェントな応答システム

- **Claude API統合**（オプション）- 自然で文脈を理解した会話
- **キーワードベースフォールバック** - APIキーなしでも動作
- 会話履歴の保持（最大20メッセージ）

### 3. ユーザーフレンドリーなUI

- モダンなデザイン（グラデーション、アニメーション）
- レスポンシブ（モバイル対応）
- クイック質問ボタン
- タイピングインジケータ
- 右下に固定されたチャットボタン

### 4. WordPress統合

- 専用ページ作成済み（https://uc.x0.com/ucチャットボット/）
- 簡単な埋め込みコード
- サイト全体に表示可能

---

## 🚀 現在の状態

### ✅ 完了

1. **知識ベース作成** - UCさんの情報を構造化
2. **バックエンドサーバー** - Node.js + Express
3. **フロントエンドUI** - レスポンシブなチャットウィジェット
4. **ローカルテスト** - 正常に動作確認済み
5. **WordPress統合** - ページ作成完了

### ⏳ 次のステップ

1. **サーバーを本番環境にデプロイ**
   ```bash
   # PM2で常駐化
   npm install -g pm2
   pm2 start chatbot-server.js --name uc-chatbot
   pm2 save
   pm2 startup
   ```

2. **API URLを更新**
   - wordpress-embed-code.html のAPI_URLを変更
   - localhost:3000 → 本番環境のURL

3. **Anthropic API設定**（オプション、より自然な会話のため）
   - APIキー取得: https://console.anthropic.com/
   - .envファイルに追加

4. **サイト全体に表示**（オプション）
   - WordPressダッシュボード > 外観 > ウィジェット
   - カスタムHTMLウィジェットに埋め込みコード追加

---

## 📊 技術スタック

### バックエンド
- Node.js v22.16.0
- Express.js 4.x
- Anthropic Claude API（オプション）

### フロントエンド
- Vanilla JavaScript
- CSS3（グラデーション、アニメーション）
- Fetch API

### インフラ
- PM2（プロセス管理）
- Nginx（リバースプロキシ、オプション）
- WordPress REST API

---

## 🔑 重要な情報

### WordPress認証情報

**ファイル:** CLAUDE.md

- URL: https://uc.x0.com/
- Username: uc-japan
- Application Password: DSFT uQ8S s5aG YRl3 2boM FEKG

### 作成されたWordPressページ

- **ページID:** 180
- **URL:** https://uc.x0.com/ucチャットボット/
- **ステータス:** 公開済み

---

## 📚 ドキュメント

### セットアップ

詳細なセットアップ手順は **README.md** を参照してください：
- 依存関係のインストール
- 環境変数の設定
- サーバーの起動
- チャットボットのテスト

### デプロイ

本番環境へのデプロイ方法は **DEPLOYMENT.md** を参照してください：
- PM2で常駐化
- Nginxでリバースプロキシ設定
- HTTPS対応
- WordPress統合の詳細手順

---

## 🎯 使用例

### 質問の例

チャットボットに聞けること：

1. **基本情報**
   - UCって誰ですか？
   - 家族構成を教えて
   - どこに住んでいますか？

2. **経歴**
   - どんな会社を経営していますか？
   - 学歴は？
   - 職歴について教えて

3. **実績・プロジェクト**
   - サハラマラソンについて
   - タイムカプセルって何？
   - 例のプールパーティーって？
   - UC少額奨学金について

4. **哲学・価値観**
   - 「とりあえず」精神って何？
   - 人生の目標は？
   - 友達についての考え方

5. **旅行・移住**
   - どんな国に住んだことがある？
   - エストニアでの経験
   - ルワンダでの活動

---

## 🔧 カスタマイズ

### デザイン変更

wordpress-embed-code.html のCSSセクションを編集：
- カラースキーム
- ボタンサイズ・位置
- チャットウィンドウサイズ
- フォント

### 知識ベース更新

uc-knowledge-base.json を編集して情報を追加・更新：
```bash
nano /home/uc/uc-site/uc-knowledge-base.json
# 編集後
pm2 restart uc-chatbot
```

### 応答のカスタマイズ

chatbot-server.js の `getKeywordBasedResponse()` 関数を編集

---

## 🐛 トラブルシューティング

### サーバーが起動しない

```bash
pm2 logs uc-chatbot
sudo lsof -i :3000
```

### チャットボットが応答しない

1. サーバー確認: `pm2 status`
2. ヘルスチェック: `curl http://localhost:3000/api/health`
3. ブラウザコンソールでエラー確認

### CORS エラー

chatbot-server.js のCORS設定を確認・更新

---

## 📞 サポート

- **README.md** - 基本的なセットアップ
- **DEPLOYMENT.md** - デプロイ詳細
- **ログ確認** - `pm2 logs uc-chatbot`

---

## 🎊 完了！

UCチャットボットシステムの構築が完了しました。

**次のアクション:**

1. サーバーを本番環境にデプロイ（DEPLOYMENT.md参照）
2. WordPressで埋め込みコードのAPI URLを更新
3. テストして公開！

**Enjoy!** 🚀

---

**プロジェクト作成日:** 2024年11月14日
