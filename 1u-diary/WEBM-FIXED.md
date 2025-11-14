# webm固定で簡素化しました

## 変更内容

### 概要
音声フォーマットを**webm固定**にして、複雑な判定ロジックを削除しました。

---

## 修正したファイル

### 1. kids-diary-recorder.js

**変更点:**
- ❌ 削除: `pickMimeType()` 関数（複雑な形式判定）
- ✅ 追加: webm固定で録音
- ✅ 追加: Blobを直接ファイル名付きでFormDataに追加

**修正前:**
```javascript
function pickMimeType() {
    var candidates = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4'];
    // ... 複雑な判定ロジック
}

var audioFile = new File([blob], 'kids-diary.webm', { type: 'audio/webm' });
fd.append('data', audioFile);
```

**修正後:**
```javascript
// webm固定で録音
mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });

// Blobを直接ファイル名付きでappend
fd.append('data', blob, 'kids-diary.webm');
```

---

### 2. kids-diary-proxy.php

**変更点:**
- ❌ 削除: 複雑な拡張子・MIMEタイプ判定ロジック
- ✅ 簡素化: webmに固定

**修正前:**
```php
// MIMEタイプから拡張子を決定
$ext = 'webm';
if (strpos($mime_type, 'mp4') !== false) {
    $ext = 'mp4';
} elseif (strpos($mime_type, 'mp3') !== false) {
    // ... 複雑な判定
}
```

**修正後:**
```php
// ファイル名がUUID形式や拡張子なしの場合は修正（webm固定）
if (!preg_match('/\.(webm|mp3|mp4|wav|m4a|ogg)$/i', $filename)) {
    $filename = 'kids-diary.webm';
}

// MIMEタイプが正しくない場合は修正
if (strpos($mime_type, 'audio/') === false) {
    $mime_type = 'audio/webm';
}
```

---

### 3. 1u-diary.json (n8n)

**変更点:**
- ✅ 簡素化: Fix Binary Metadataノードをwebm固定に

**修正前:**
```javascript
// 拡張子を判定
let ext = 'webm';
if (originalMimeType.includes('mp4')) {
    ext = 'mp4';
    // ... 複雑な判定
}
```

**修正後:**
```javascript
// ファイル名とMIMEタイプをwebmに固定
binary.data.fileName = 'kids-diary.webm';
binary.data.mimeType = 'audio/webm';
```

---

## メリット

### 1. コードがシンプルに
- 複雑な条件分岐を削除
- メンテナンスが容易
- バグが減る

### 2. 確実な動作
- webm固定で一貫性が保たれる
- OpenAI Whisper APIで確実に認識される
- ファイル名とMIMEタイプの不一致が発生しない

### 3. Chrome/Firefox最適化
- webmはChrome、Firefoxで標準サポート
- Opus codecで高品質・小サイズ
- オープンフォーマット

---

## 更新手順

### 1. ファイルをアップロード

以下の2つのファイルを**上書きアップロード**：

```
/wp-content/themes/あなたの子テーマ名/
├── kids-diary-recorder.js  （更新）
└── kids-diary-proxy.php    （更新）
```

### 2. n8nワークフローを再インポート

1. n8nで既存の「Kids Diary」ワークフローを削除
2. 更新した `1u-diary.json` をインポート
3. OpenAI APIキーを再設定（WhisperノードとChatノード）
4. ワークフローを **Active** に設定

### 3. ブラウザのキャッシュをクリア

`Ctrl+Shift+R`（Mac: `Cmd+Shift+R`）

### 4. テスト

1. https://uc.x0.com/1u-diary にアクセス
2. F12でコンソールを開く
3. 録音 → 停止を実行
4. コンソールで確認：

```
[デバッグ] 音声Blob作成完了: 163000 bytes, type: audio/webm
[デバッグ] FormData作成完了: kids-diary.webm (audio/webm)
```

5. n8nの「Fix Binary Metadata」ノードの出力を確認：
   - File Name: `kids-diary.webm` ✅
   - Mime Type: `audio/webm` ✅

---

## トラブルシューティング

### Safari/iOSで録音できない

**症状:** Safariでエラーが出る

**原因:** Safariはwebmをサポートしていません

**対処法:**

#### オプション1: Safariユーザーにはメッセージ表示
```javascript
if (!MediaRecorder.isTypeSupported('audio/webm')) {
    alert('このブラウザは対応していません。Chromeをご利用ください。');
}
```

#### オプション2: mp4にフォールバック（将来の拡張）
```javascript
var mimeType = MediaRecorder.isTypeSupported('audio/webm')
    ? 'audio/webm'
    : 'audio/mp4';
```

---

## まとめ

✅ **webm固定でシンプルかつ確実に動作**
✅ **Chrome/Firefoxで最適化**
✅ **OpenAI Whisper APIで確実に認識**
✅ **コードがメンテナンスしやすい**

主にChromeを使用する環境では、この設定が最適です！
