# 緊急修正：WordPressが開けない場合

## 原因
functions.phpに追加したコードでエラーが発生しています。ファイルパスが間違っているか、PHPの構文エラーの可能性があります。

---

## 修正方法1：FTPでfunctions.phpを編集（推奨）

### 手順

1. **FTPクライアントでサーバーに接続**

2. **functions.phpを開く**
   ```
   /wp-content/themes/あなたの子テーマ名/functions.php
   ```

3. **最後に追加した以下の行を削除またはコメントアウト**

   削除する行：
   ```php
   // いちゆう日記レコーダー
   require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';
   require_once get_stylesheet_directory() . '/kids-diary-proxy.php';
   ```

   または、コメントアウト（先頭に `//` を追加）：
   ```php
   // いちゆう日記レコーダー
   // require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';
   // require_once get_stylesheet_directory() . '/kids-diary-proxy.php';
   ```

4. **ファイルを保存**

5. **サイトにアクセスして確認**
   - https://uc.x0.com/wp-admin/ にアクセス
   - 管理画面が表示されればOK

---

## 修正方法2：ファイルマネージャーで編集

cPanelなどのファイルマネージャーを使用している場合：

1. ファイルマネージャーにログイン
2. `/wp-content/themes/あなたの子テーマ名/functions.php` を探す
3. 右クリック → 「編集」
4. 最後に追加した3行を削除またはコメントアウト
5. 保存

---

## 修正方法3：テーマを一時的に変更

### cPanel/PhpMyAdminを使う場合

1. **PhpMyAdminにログイン**

2. **WordPressのデータベースを選択**

3. **`wp_options`テーブルを開く**

4. **`option_name = 'template'` の行を探す**
   - `option_value` を `twentytwentyfour` などのデフォルトテーマに変更

5. **`option_name = 'stylesheet'` の行を探す**
   - `option_value` も同じく `twentytwentyfour` に変更

6. **サイトにアクセス**
   - デフォルトテーマで表示される
   - 管理画面にログインできる

7. **管理画面で元のテーマに戻す前に、functions.phpを修正**

---

## 修正方法4：wp-config.phpでデバッグモードを有効化

エラーの詳細を確認したい場合：

1. **FTPで `wp-config.php` を開く**（ルートディレクトリ）

2. **以下の行を探す**
   ```php
   define( 'WP_DEBUG', false );
   ```

3. **以下に変更**
   ```php
   define( 'WP_DEBUG', true );
   define( 'WP_DEBUG_LOG', true );
   define( 'WP_DEBUG_DISPLAY', false );
   ```

4. **保存して、サイトにアクセス**

5. **エラーログを確認**
   ```
   /wp-content/debug.log
   ```

6. **エラー内容を確認して修正**

---

## よくあるエラーの原因と修正

### エラー1: ファイルが見つからない
```
Warning: require_once(/path/to/kids-diary-shortcode.php): failed to open stream
```

**原因:** ファイルがアップロードされていない、またはパスが間違っている

**修正:**
```php
// パターン1: 子テーマを使用している場合
require_once get_stylesheet_directory() . '/kids-diary-shortcode.php';

// パターン2: 親テーマを使用している場合
require_once get_template_directory() . '/kids-diary-shortcode.php';

// パターン3: 絶対パスで指定
require_once ABSPATH . 'wp-content/themes/テーマ名/kids-diary-shortcode.php';
```

### エラー2: PHPの構文エラー
```
Parse error: syntax error, unexpected...
```

**原因:** PHPの構文が間違っている（閉じ括弧の不足など）

**修正:** functions.phpの最後を確認し、`}` や `;` が正しく閉じられているか確認

---

## 修正後の確認

管理画面にアクセスできたら：

1. **外観 > テーマファイルエディター** を開く
2. **functions.php** を開く
3. 以下の**安全なバージョン**に置き換える：

```php
// いちゆう日記レコーダー（安全版）
$kids_diary_shortcode = get_stylesheet_directory() . '/kids-diary-shortcode.php';
$kids_diary_proxy = get_stylesheet_directory() . '/kids-diary-proxy.php';

if (file_exists($kids_diary_shortcode)) {
    require_once $kids_diary_shortcode;
} else {
    error_log('Kids Diary: kids-diary-shortcode.php が見つかりません: ' . $kids_diary_shortcode);
}

if (file_exists($kids_diary_proxy)) {
    require_once $kids_diary_proxy;
} else {
    error_log('Kids Diary: kids-diary-proxy.php が見つかりません: ' . $kids_diary_proxy);
}
```

この安全版は、ファイルが存在しない場合でもエラーを起こさず、ログに記録するだけです。

---

## サポートが必要な場合

1. エラーログの内容を共有してください：`/wp-content/debug.log`
2. 使用しているテーマ名を教えてください
3. FTPアクセスの有無を教えてください
