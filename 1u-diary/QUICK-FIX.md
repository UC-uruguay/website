# Mixed Contentエラーの修正手順

## 問題
```
Mixed Content: The page at 'https://uc.x0.com/1u-diary/' was loaded over HTTPS,
but requested an insecure resource 'http://35.200.56.246:5678/webhook/kids-diary-audio'.
This request has been blocked
```

HTTPSサイトからHTTPのn8nにアクセスしようとしてブロックされています。

---

## 解決策：WordPressプロキシ経由でアクセス

### 1. 新しいファイルをアップロード

**3つのファイル**をテーマディレクトリにアップロード（既存は上書き）：

```
/wp-content/themes/あなたの子テーマ名/
├── kids-diary-shortcode.php  （既存を上書き）
├── kids-diary-recorder.js    （既存を上書き）
└── kids-diary-proxy.php      （新規追加）← これが重要！
```

### 2. functions.phpを更新

**外観 > テーマファイルエディター > functions.php** の最後に以下を追加（既に1行目があれば、2行目のみ追加）：

```php
// いちゆう日記レコーダー
require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';
require_once get_stylesheet_directory() . '/kids-diary-proxy.php';  ← この行を追加
```

### 3. ブラウザのキャッシュをクリア

- Chrome: `Ctrl+Shift+R`（Mac: `Cmd+Shift+R`）

### 4. 動作確認

1. https://uc.x0.com/1u-diary にアクセス
2. F12キーでコンソールを開く
3. 録音 → 停止を実行
4. コンソールに以下が表示されることを確認：

```
[デバッグ] Webhook URL: https://uc.x0.com/wp-json/kids-diary/v1/proxy
                         ↑ HTTPSになっている！
```

5. Mixed Contentエラーが出ないことを確認

---

## 仕組み

### 変更前（エラー）
```
ブラウザ --[HTTPS]--> ❌ --[HTTP]--> n8n
                      ↑ ここでブロック
```

### 変更後（成功）
```
ブラウザ --[HTTPS]--> WordPress Proxy --[HTTP]--> n8n
         ✅ OK                          ✅ OK
```

ブラウザからはWordPressにHTTPSでアクセスし、WordPressサーバーからn8nにHTTPでアクセスします。サーバー間通信なので、HTTPでも問題ありません。

---

## トラブルシューティング

### プロキシのURLを確認

ブラウザで以下にアクセス：
```
https://uc.x0.com/wp-json/kids-diary/v1/proxy
```

表示される内容：
- 正常: 何らかのエラーメッセージ（"Missing audio file" など）
- 異常: 404 Not Found → プロキシが登録されていない

### 404 Not Foundが出る場合

1. functions.phpに `kids-diary-proxy.php` の読み込みを追加したか確認
2. WordPressの管理画面で **設定 > パーマリンク** を開いて「変更を保存」をクリック（REST APIのルートを再登録）
3. ブラウザのキャッシュをクリア

### それでも動かない場合

WordPressのエラーログを確認：
```
/wp-content/debug.log
```

`[Kids Diary Proxy]` で始まる行を探してください。
