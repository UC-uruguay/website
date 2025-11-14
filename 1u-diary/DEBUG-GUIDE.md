# デバッグガイド - いちゆう日記レコーダー

## 1. ブラウザでの確認

### 新しいJSファイルをアップロード

1. **修正した `kids-diary-recorder.js` をアップロード**（既存のファイルを上書き）
2. ブラウザのキャッシュをクリア：
   - Chrome: `Ctrl+Shift+Delete` → 「キャッシュされた画像とファイル」をクリア
   - または、ハードリロード: `Ctrl+Shift+R`（Mac: `Cmd+Shift+R`）

### コンソールでログを確認

1. https://uc.x0.com/1u-diary にアクセス
2. **F12キー** を押してデベロッパーツールを開く
3. **Console** タブを選択
4. 録音 → 停止を実行
5. 以下のようなログが表示されます：

```
[デバッグ] 音声Blob作成完了: 123456 bytes
[デバッグ] Webhook URL: http://35.200.56.246:5678/webhook/kids-diary-audio
[デバッグ] 送信データ: child_name=いちゆう, date=2025/10/27
[デバッグ] レスポンスステータス: 200 OK
[デバッグ] レスポンスボディ（生データ）: {"ok":true,"link":"https://...","id":123}
[デバッグ] 処理結果: ...
```

### エラーパターンと対処法

#### ❌ CORS エラー
```
Access to fetch at 'http://...' from origin 'https://...' has been blocked by CORS
```
**原因:** n8nのWebhookがCORSを許可していない
**対処:** n8nのWebhookノード設定で「CORS Enabled」をONにする

#### ❌ ネットワークエラー
```
Failed to fetch
```
**原因:** n8nが停止している、またはURLが間違っている
**対処:**
- n8nが起動しているか確認
- Webhook URLが正しいか確認
- `http://` ではなく `https://` が必要な場合がある

#### ❌ 404 Not Found
```
[デバッグ] レスポンスステータス: 404 Not Found
```
**原因:** Webhookのパスが間違っている、またはワークフローが無効化されている
**対処:**
- n8nでワークフローが「Active」になっているか確認
- Webhook URLを再確認

#### ❌ 500 Internal Server Error
```
[デバッグ] レスポンスステータス: 500 Internal Server Error
```
**原因:** n8nのワークフロー内でエラーが発生
**対処:** n8nの実行履歴でエラー詳細を確認（次のセクション参照）

---

## 2. n8nでの確認

### ワークフローの状態確認

1. n8nにアクセス（http://35.200.56.246:5678）
2. 「Kids Diary」ワークフローを開く
3. 右上のトグルスイッチが **「Active」** になっているか確認
4. 緑色のチェックマークが表示されていればOK

### Webhook URLの確認

1. 「Webhook (Audio)」ノードをクリック
2. 下部に表示される **「Production URL」** をコピー
3. このURLが `kids-diary-shortcode.php` の `webhook_url` と一致しているか確認

### 実行履歴の確認

1. n8nの左メニューから **「Executions」**（実行履歴）を開く
2. 最新の実行が表示される
3. 成功の場合: 緑色の「Success」
4. 失敗の場合: 赤色の「Error」

### エラーの詳細確認

実行履歴で「Error」の行をクリック：

#### ケース1: Whisperノードでエラー
```
Error: Request failed with status code 401
```
**原因:** OpenAI APIキーが無効
**対処:** APIキーを確認・更新

#### ケース2: Mergeノードでエラー
```
Error: Not enough data from all inputs
```
**原因:** 2つの入力が正しく接続されていない
**対処:** ワークフローの接続を確認

#### ケース3: Build Promptノードでエラー
```
TypeError: Cannot read property 'child_name' of undefined
```
**原因:** データ構造が期待と異なる
**対処:** Functionノードのコードを確認

#### ケース4: WordPress投稿でエラー
```
Error: Request failed with status code 401
```
**原因:** WordPress認証が無効
**対処:** Basic認証の資格情報を確認

```
Error: Request failed with status code 403
```
**原因:** 投稿権限がない
**対処:** WordPressユーザーの権限を確認

---

## 3. n8nワークフローのテスト

### 手動実行でテスト

1. n8nでワークフローを開く
2. 「Webhook (Audio)」ノードをクリック
3. **「Listen For Test Event」** をクリック
4. ブラウザで録音 → 停止を実行
5. n8nに「Execution successful」と表示されればOK

### 各ノードの出力確認

実行後、各ノードをクリックして出力データを確認：

- **Webhook (Audio)**: `audio` バイナリデータと `child_name`, `date` があるか
- **OpenAI Whisper**: 文字起こしテキストが返ってきているか
- **Merge**: 両方のデータが統合されているか
- **Build Prompt**: `system` と `user` が正しく生成されているか
- **OpenAI Chat**: JSON形式で `title`, `excerpt`, `content_html` が返ってきているか
- **Build WP Body**: WordPress投稿用のデータに整形されているか
- **WordPress Create Post**: `link` と `id` が返ってきているか

---

## 4. よくある問題と解決策

### 問題: 録音はできるが「送信中」のまま止まる

**確認:**
1. ブラウザのコンソールでネットワークエラーを確認
2. n8nが起動しているか確認
3. Webhook URLが正しいか確認

### 問題: n8nは動くがWordPress投稿されない

**確認:**
1. n8nの実行履歴で「WordPress Create Post」ノードのエラーを確認
2. WordPress URLが正しいか確認（https://uc.x0.com/wp-json/wp/v2/posts）
3. Basic認証が正しいか確認
4. WordPressで手動投稿できるか確認

### 問題: 投稿されたがリンクが表示されない

**確認:**
1. n8nの「Respond to Webhook」ノードの設定を確認
2. レスポンスに `link` フィールドが含まれているか確認
3. ブラウザのコンソールで実際のレスポンスを確認

### 問題: 音声は送信されるが文字起こしが空

**確認:**
1. OpenAI Whisper APIキーが有効か確認
2. 音声ファイルのフォーマットが対応しているか確認（webm, mp4）
3. n8nの「OpenAI Whisper」ノードで `binaryPropertyName` が `data` になっているか確認

---

## 5. 完全な動作フロー

正常に動作する場合、以下の流れになります：

1. 👤 **ユーザー**: 録音ボタンを押す → 話す → 停止ボタンを押す
2. 🌐 **ブラウザ**: 音声データをn8n Webhookに送信
3. 🔗 **n8n Webhook**: データを受信
4. 🎙️ **OpenAI Whisper**: 音声をテキストに変換
5. 🔀 **Merge**: 文字起こし + メタデータを統合
6. 📝 **Build Prompt**: ChatGPT用のプロンプトを生成
7. 🤖 **OpenAI Chat**: 日記記事（JSON）を生成
8. 🔧 **Build WP Body**: WordPress用にデータを整形
9. 📤 **WordPress Create Post**: WordPressに投稿
10. ✅ **Respond to Webhook**: 投稿URLを返却
11. 🌐 **ブラウザ**: 「公開完了！」を表示 + リンクを表示

各ステップでどこまで進んでいるか、n8nの実行履歴とブラウザのコンソールで確認できます。
