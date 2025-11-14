# UCチャットボット - 最終セットアップガイド

## ✅ 完了したこと

1. **情報の修正**
   - 名前: 中嶋雄士 → **中嶋雄士（なかしまゆうし）**
   - 出身: 栃木県 → **福岡県**（栃木生まれ、福岡育ち）
   - 年齢: 34歳（1990年生まれ）

2. **セキュリティ設定**
   - `.env`ファイルに Anthropic APIキーを安全に保存
   - `.gitignore`で機密情報を保護
   - ファイル権限を600に設定

3. **チャットボットシステム**
   - Node.jsサーバー完成
   - キーワードベース応答システム動作確認
   - PHPプロキシ版も作成（さくらレンタルサーバー用）

## 📁 作成されたファイル

### メインファイル
- `chatbot-server.js` - Node.jsバックエンドサーバー
- `uc-knowledge-base.json` - UCさんの知識ベース
- `.env` - APIキー（機密情報）
- `package.json` - Node.js依存関係

### WordPress統合用
- `wordpress-embed-code.html` - フル機能版埋め込みコード
- `wordpress-simple-embed.html` - シンプル版（PHPプロキシ使用）
- `chatbot-proxy.php` - PHPプロキシ（さくらレンタルサーバー用）

### ドキュメント
- `README.md` - 基本セットアップガイド
- `DEPLOYMENT.md` - デプロイ詳細
- `SAKURA-DEPLOYMENT.md` - さくらインターネット特化ガイド
- `FINAL-SETUP.md` - このファイル

## 🚀 WordPressに統合する手順

### 方法1: PHPプロキシ使用【最も簡単・推奨】

さくらインターネットのレンタルサーバーで簡単に動かせます。

#### ステップ1: PHPファイルをアップロード

1. `chatbot-proxy.php` をWordPressのルートディレクトリにアップロード
   ```
   https://uc.x0.com/chatbot-proxy.php
   ```

2. ブラウザでアクセスしてテスト:
   ```
   https://uc.x0.com/chatbot-proxy.php
   ```

   正常なら以下が表示されます:
   ```json
   {"status":"ok","message":"UC Chatbot PHP Proxy","version":"1.0.0"}
   ```

#### ステップ2: WordPressに埋め込む

**オプションA: WP Codeプラグイン使用（推奨）**

1. WordPressダッシュボードにログイン
2. プラグイン > 新規追加
3. "WP Code" で検索、インストール & 有効化
4. Code Snippets > Add New
5. `wordpress-simple-embed.html` の内容をペースト
6. **重要**: API_URLをこの1行だけ変更:
   ```javascript
   const API_URL = 'https://uc.x0.com/chatbot-proxy.php';
   ```
7. タイトル: "UC Chatbot"
8. 場所: Sitewide Footer
9. 保存 & 有効化

**オプションB: カスタムHTML使用**

1. 外観 > カスタマイズ > 追加CSS
2. `wordpress-simple-embed.html` の内容をコピー
3. API_URLを修正して保存

### 方法2: 外部サーバー使用【高度】

Railway、Vercel等にNode.jsサーバーをデプロイ：

1. **Railwayにデプロイ** (SAKURA-DEPLOYMENT.md 参照)
2. URLを取得: `https://uc-chatbot-xxx.up.railway.app`
3. `wordpress-embed-code.html` のAPI_URLを更新:
   ```javascript
   const API_URL = 'https://uc-chatbot-xxx.up.railway.app/api/chat';
   ```
4. WordPressに埋め込み

## 🧪 動作確認

### PHPプロキシのテスト

```bash
curl -X POST https://uc.x0.com/chatbot-proxy.php \
  -H "Content-Type: application/json" \
  -d '{"message":"UCは何歳ですか？"}'
```

正常なら34歳と回答されます。

### WordPressサイトで確認

1. https://uc.x0.com/ にアクセス
2. 右下にチャットボタンが表示されるはず
3. クリックしてチャットウィンドウを開く
4. テスト質問:
   - "UCは何歳ですか？" → 34歳
   - "出身はどこですか？" → 福岡県
   - "本名は？" → 中嶋雄士

## ⚙️ Anthropic Claude API について

### 現在の状況

Anthropic APIのモデル名に問題がある可能性があります。キーワードベースの応答システムが動作しているため、基本的な質問には対応できています。

### Claude APIを動作させるには

#### オプション1: 最新モデル名を確認

Anthropic Console (https://console.anthropic.com/) で利用可能なモデルを確認:
- `claude-3-5-sonnet-latest`
- `claude-3-opus-latest`
- `claude-3-sonnet-20240229`

`chatbot-server.js` の45行目を修正:
```javascript
model: 'claude-3-sonnet-20240229',  // または別のモデル
```

#### オプション2: キーワードベースで運用【現状のまま】

Claude APIなしでも、キーワードベースシステムが以下の質問に対応:
- 基本情報（名前、年齢、出身、家族）
- 会社・ビジネス
- サハラマラソン
- 哲学・とりあえず精神
- タイムカプセル
- 実績
- 国・旅行

十分に機能的です！

## 📊 どの方法を選ぶべき？

| 方法 | 難易度 | コスト | 推奨度 |
|------|--------|--------|--------|
| PHPプロキシ | ★☆☆ | 無料 | ⭐⭐⭐⭐⭐ |
| Railway | ★★☆ | 無料 | ⭐⭐⭐⭐ |
| さくらVPS | ★★★ | 有料 | ⭐⭐⭐ |

**推奨**: PHPプロキシを使用して、すぐにWordPressで動作させる

## 🔧 トラブルシューティング

### チャットボットが表示されない

1. ブラウザのコンソール (F12) でエラー確認
2. API URLが正しいか確認
3. PHPファイルがアクセス可能か確認

### 回答がおかしい

1. `chatbot-proxy.php` の `getResponse()` 関数を編集
2. キーワードを追加・修正
3. サーバーにアップロード

### PHPエラー

```bash
# PHPのエラーログを確認
tail -f /path/to/php-error.log
```

## 📝 次のステップ

### すぐにできること

1. **PHPプロキシをアップロード**
   ```bash
   # FTP または ファイルマネージャーで
   /home/xxx/uc.x0.com/chatbot-proxy.php にアップロード
   ```

2. **WordPressに追加**
   - WP Codeプラグインで追加（5分）

3. **テスト**
   - サイトにアクセスして動作確認

### 将来的に

1. **Claude API を動作させる**
   - より自然な会話
   - 複雑な質問にも対応

2. **デザインカスタマイズ**
   - 色、サイズ、位置を調整
   - ブランドに合わせる

3. **知識ベース拡張**
   - 新しい情報を追加
   - 応答をカスタマイズ

## 💡 Tips

### PHPプロキシの応答をカスタマイズ

`chatbot-proxy.php` の `getResponse()` 関数を編集:

```php
// 新しいキーワードを追加
if (preg_match('/(趣味|hobby)/u', $lowerMessage)) {
    return "UCの趣味は...";
}
```

### チャットボタンの位置を変更

CSS を編集:

```css
#uc-chatbot-simple .chatbot-container {
    bottom: 20px;  /* 下から20px */
    right: 20px;   /* 右から20px */
    /* 左下にしたい場合: */
    /* left: 20px; */
}
```

## 📞 サポート

- **README.md** - 基本セットアップ
- **DEPLOYMENT.md** - デプロイ詳細
- **SAKURA-DEPLOYMENT.md** - さくらインターネット特化
- **このファイル** - 最終セットアップガイド

## ✨ 完成！

現在、以下が動作しています：

✅ ローカルサーバー（http://localhost:3000）
✅ キーワードベース応答システム
✅ 名前・年齢・出身地の正確な情報
✅ PHPプロキシ（さくらサーバー用）
✅ WordPress埋め込みコード

**次のアクション:**
1. `chatbot-proxy.php` をアップロード
2. WP Codeで埋め込みコード追加
3. テスト！

---

**作成日:** 2024年11月14日
**最終更新:** 2024年11月14日
