# いちゆう日記レコーダー WordPress設定手順

## 1. ファイルをアップロード

FTPまたはファイルマネージャーで、以下の3つのファイルをテーマディレクトリにアップロード：

1. `kids-diary-shortcode.php`
2. `kids-diary-recorder.js`
3. `kids-diary-proxy.php` ← **新規追加（Mixed Contentエラー対策）**

アップロード先：
```
/wp-content/themes/あなたの子テーマ名/kids-diary-shortcode.php
/wp-content/themes/あなたの子テーマ名/kids-diary-recorder.js
/wp-content/themes/あなたの子テーマ名/kids-diary-proxy.php
```

子テーマを使っていない場合は親テーマのディレクトリでもOK

## 2. functions.phpに追加

WordPressの管理画面から：

1. **外観 > テーマファイルエディター** を開く
2. 右側のファイル一覧から **functions.php** を選択
3. ファイルの**一番最後**に以下のコードを追加：

```php
// いちゆう日記レコーダー
require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';
require_once get_stylesheet_directory() . '/kids-diary-proxy.php';
```

4. 「ファイルを更新」をクリック

## 3. ページにショートコードを追加

1. WordPressの管理画面で **固定ページ > 1u-diary** を編集
2. **既存のコンテンツを全て削除**
3. 「+」ボタンで **ショートコード** ブロックを追加
4. 以下を入力：

```
[kids_diary_recorder]
```

5. 「公開」または「更新」をクリック

## 4. 動作確認

1. https://uc.x0.com/1u-diary にアクセス
2. 「🎙️ 録音開始」ボタンが表示されることを確認
3. F12キーでコンソールを開く
4. ボタンをクリックして録音を試す
5. コンソールに `[デバッグ] Webhook URL: https://uc.x0.com/wp-json/kids-diary/v1/proxy` と表示されることを確認（HTTPSになっている）
6. Mixed Contentエラーが出ないことを確認

---

## プロキシの仕組み

### 問題
- HTTPSサイトからHTTPのn8nにアクセスするとMixed Contentエラーが発生

### 解決策
- WordPressサーバーにプロキシエンドポイントを作成
- 通信の流れ:
  ```
  ブラウザ --[HTTPS]--> WordPress Proxy --[HTTP]--> n8n
  ```

### メリット
1. ✅ Mixed Contentエラーが発生しない
2. ✅ ブラウザからはHTTPS通信のみ
3. ✅ n8nのURLを直接公開する必要がない
4. ✅ サーバー間通信なのでHTTPでも安全

## トラブルシューティング

### エラー: "require_once: failed to open stream"

functions.phpのパスが間違っています。以下を試してください：

```php
// 方法1: 子テーマのディレクトリ
require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';

// 方法2: 親テーマのディレクトリ
require_once get_template_directory() . '/kids-diary-shortcode.php';

// 方法3: 絶対パス（上記が動かない場合）
require_once ABSPATH . 'wp-content/themes/あなたのテーマ名/kids-diary-shortcode.php';
```

### ショートコードが表示されない

PHPファイルが正しくアップロードされているか確認してください。

### Webhook URLを変更したい

ショートコードで指定できます：

```
[kids_diary_recorder webhook_url="https://新しいURL"]
```
