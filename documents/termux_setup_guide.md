# 📱 Termux WordPress + Gemini CLI 設定ガイド

## 🔧 初期設定手順

### 1. Termuxスクリプトの配置
```bash
# スクリプトをTermuxにコピー
cp termux_wordpress_setup.py ~/wordpress-blog/wp.py
cd ~/wordpress-blog
```

### 2. WordPress認証設定
```bash
# WordPressの設定
python wp.py setup

# 入力項目:
# Site URL: https://uc.x0.com
# Username: あなたのWordPressユーザー名
# App Password: WordPressアプリパスワード
```

**WordPressアプリパスワード取得方法：**
1. WordPress管理画面 → ユーザー → プロフィール
2. 「アプリケーションパスワード」セクションで新規作成
3. 生成されたパスワードをコピー

### 3. 基本的な使い方

**インタラクティブ投稿：**
```bash
python wp.py post
```

**クイック投稿：**
```bash
python wp.py quick "投稿タイトル" "投稿内容"

# 画像付き投稿
python wp.py quick "投稿タイトル" "投稿内容" "画像パス.jpg"
```

## 🤖 Gemini CLIとの連携

### 1. コンテンツ生成スクリプト
```bash
#!/bin/bash
# gemini_blog.sh

echo "📝 Gemini Blog Generator"
echo "テーマを入力してください:"
read TOPIC

echo "🤖 Geminiでコンテンツを生成中..."
CONTENT=$(gemini generate "Write a blog post about: $TOPIC. Write in English, suitable for a personal blog. Include personal experiences and insights.")

echo "📱 WordPressに投稿中..."
python wp.py quick "$TOPIC" "$CONTENT"

echo "✅ 投稿完了！"
```

### 2. 使用例
```bash
# スクリプトに実行権限を付与
chmod +x gemini_blog.sh

# 実行
./gemini_blog.sh
```

## 📸 画像管理

**画像の保存場所：**
```bash
# 画像ディレクトリを作成
mkdir ~/wordpress-blog/images

# スマホから画像をコピー
cp /sdcard/DCIM/Camera/IMG_20250831.jpg ~/wordpress-blog/images/
```

**画像付き投稿：**
```bash
python wp.py quick "今日の写真" "今日撮った写真です" "images/IMG_20250831.jpg"
```

## 🔄 自動化スクリプト例

### 日記投稿スクリプト
```bash
#!/bin/bash
# daily_blog.sh

DATE=$(date '+%Y年%m月%d日')
echo "📅 $DATE の日記"
echo "今日あったことを入力してください:"
read DIARY_TEXT

# Geminiで文章を整える
FORMATTED=$(gemini generate "Rewrite this diary entry in English for a personal blog: $DIARY_TEXT")

# WordPressに投稿
python wp.py quick "$DATE - Daily Reflection" "$FORMATTED"

echo "✅ 日記を投稿しました！"
```

### 写真ブログスクリプト
```bash
#!/bin/bash
# photo_blog.sh

echo "📸 写真ブログ作成"
echo "画像ファイル名を入力:"
read IMAGE_FILE

echo "写真の説明を入力:"
read DESCRIPTION

# Geminiで説明文を拡張
CONTENT=$(gemini generate "Write a blog post about this photo: $DESCRIPTION. Make it personal and engaging.")

# タイトル生成
TITLE=$(gemini generate "Create a catchy title for a blog post about: $DESCRIPTION" | head -1)

# 投稿
python wp.py quick "$TITLE" "$CONTENT" "images/$IMAGE_FILE"

echo "✅ 写真ブログを投稿しました！"
```

## 🛡️ セキュリティ設定

**設定ファイルの保護：**
```bash
# 設定ファイルの権限を制限
chmod 600 wp_config.json

# .gitignoreに追加（Gitを使う場合）
echo "wp_config.json" >> .gitignore
```

## 🚀 高度な使い方

### 1. テンプレート機能
```bash
# テンプレートディレクトリ作成
mkdir templates

# テンプレートファイル作成
echo "<!-- wp:heading -->
<h2>今日の出来事</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{CONTENT}</p>
<!-- /wp:paragraph -->" > templates/daily.html
```

### 2. 一括投稿スクリプト
```bash
#!/bin/bash
# bulk_post.sh

for file in drafts/*.txt; do
    TITLE=$(basename "$file" .txt)
    CONTENT=$(cat "$file")
    
    python wp.py quick "$TITLE" "$CONTENT"
    echo "✅ 投稿完了: $TITLE"
    
    sleep 2  # API制限対策
done
```

## 📋 トラブルシューティング

**よくある問題と解決法：**

1. **認証エラー**
   ```bash
   # 設定確認
   cat wp_config.json
   
   # 再設定
   python wp.py setup
   ```

2. **画像アップロードエラー**
   ```bash
   # ファイル存在確認
   ls -la images/
   
   # 権限確認
   file images/your_image.jpg
   ```

3. **Gemini CLI接続エラー**
   ```bash
   # API設定確認
   gemini config list
   
   # 再設定
   gemini config set-api-key YOUR_API_KEY
   ```

## 📱 使用例

**完全な投稿ワークフロー：**
```bash
# 1. 画像をコピー
cp /sdcard/DCIM/Camera/20250831.jpg ~/wordpress-blog/images/

# 2. Geminiでコンテンツ生成
TOPIC="temple visit experience"
CONTENT=$(gemini generate "Write a personal blog post about visiting a Japanese temple. Include cultural insights and personal reflections.")

# 3. WordPressに投稿
python wp.py quick "Temple Visit Reflection" "$CONTENT" "images/20250831.jpg"
```

これで、Termux環境でGemini CLIとWordPressを使った完全なブログ投稿システムが構築できます！🎉