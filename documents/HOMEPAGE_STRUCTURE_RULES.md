# トップページ構成ルール / Homepage Structure Rules

## 🚨 絶対に変更してはいけない構成 / NEVER CHANGE THIS STRUCTURE

このルールは今後の修正があっても**絶対に変更しない**こと。

### セクション構成 / Section Structure

#### 1. ヒーローセクション / Hero Section
- **Homeテキストは表示しない** (CSSで非表示)
- "Hi, I'm UC! 👋" のタイトル
- ウェルカムメッセージ
- グレー背景 (#f8f9fa)

#### 2. About Meセクション / About Me Section  
- プロフィール写真（左側40%）
- **SNSリンクはロゴのみ表示**（テキスト名は非表示）
- About Me情報（右側60%）
- Family & Daily Life
- Hobbies & Interests

#### 3. Travel & Culture + Inspirationsセクション / Travel & Culture Section
- **この構成は絶対に変更しない**
- Travel & Culture（左カラム）
- Inspirations（右カラム）
- 白背景 (#ffffff)

#### 4. Recent Postsセクション / Recent Posts Section
- タイトル: "📝 Recent Posts" 
- 説明文: "Discover my latest thoughts, experiences, and creative projects"
- **画像サイズ**: 120px x 120px 固定、object-fit: cover
- 3投稿表示、著者非表示、日付表示
- "View All Posts →" ボタン

#### 5. Gallery & Interestsセクション / Gallery & Interests Section
- タイトル: "🎨 Gallery & Interests"
- **4つのカテゴリ（絶対に変更しない）**:
  1. 📸 Greatest Moments → `/greatest-moments/`
  2. 📦 Products → `/products/`
  3. 💼 Portfolio → `/portfolio/`
  4. 📅 Event Info → `/event-info/`

#### 6. フッターセクション / Footer Section
- 引用文: "I believe in connecting with others through vision and empathy..."
- SNSリンク（ロゴのみ、テキスト非表示）
- **区切り線と "With Love from UC ❤️" は削除済み**

### 技術的なCSS設定 / Technical CSS Settings

```css
/* ページタイトル非表示 */
.entry-title, .page-title, h1.entry-title {
    display: none !important;
}

/* Recent Posts画像サイズ固定 */
.featured-image-fixed .wp-block-latest-posts__featured-image img {
    width: 120px !important;
    height: 120px !important;
    object-fit: cover !important;
    border-radius: 8px !important;
}

/* SNSリンクのテキスト非表示 */
.wp-block-social-links .wp-social-link .wp-block-social-link-anchor {
    text-decoration: none !important;
}
.wp-block-social-links .wp-social-link-anchor::after {
    content: none !important;
}
.wp-block-social-links.has-icon-color .wp-social-link-anchor:hover,
.wp-block-social-links.has-icon-color .wp-social-link-anchor:focus {
    opacity: 0.7;
}
```

### 重要な注意事項 / Important Notes

1. **この構成は今後の修正があっても絶対に変更しない**
2. セクションの順序、レイアウト、基本構成は固定
3. 内容の更新は可能だが、構造は維持する
4. SNSリンクは常にロゴのみ表示
5. Recent Postsの画像サイズは120px固定
6. Footer部分の区切り線と"With Love from UC ❤️"は削除済み
7. **🌐 全ページ英語で作成 - ALL PAGES MUST BE CREATED IN ENGLISH ONLY** (最優先ルール)

このルールに従って今後の修正を行うこと。