# WordPress投稿ルール / WordPress Post Rules

## 🚨 第一優先ルール / TOP PRIORITY RULE

### **EVERYTHING MUST BE IN ENGLISH - ALWAYS - ABSOLUTELY MANDATORY**
- **ALL titles must be in English - NO EXCEPTIONS**
- **ALL content must be in English - NO EXCEPTIONS** 
- **ALL URL slugs must be in English - NO EXCEPTIONS**
- **ALL page names must be in English - NO EXCEPTIONS**
- **ALL new pages must be in English - NO EXCEPTIONS**
- **ALL existing pages must be converted to English - NO EXCEPTIONS**
- **This applies to EVERY SINGLE PAGE including Products, Portfolio, About, etc.**
- **日本語は一切禁止 - Japanese is ABSOLUTELY FORBIDDEN**
- **NO exceptions - English is mandatory for everything - PERIOD**

### **絶対に守る / ABSOLUTELY MANDATORY ENFORCEMENT**
- 新規ページ作成時は必ず英語で作成
- 既存ページの更新時は必ず英語に変換
- 日本語コンテンツを見つけたら即座に英語に変換
- この ルールに違反した場合は即座に修正する

## 必須ルール / Required Rules

### 1. 英語使用 / English Usage (REINFORCED)
- **タイトルは常に英語 / Title must ALWAYS be in English**
- **URLスラグは常に英語 / URL slug must ALWAYS be in English** 
- **内容も英語で書く / Content must ALWAYS be in English**
- **ページ名も英語 / Page names must ALWAYS be in English**

### 2. コンテンツのリライト / Content Rewriting
- **ユーザーの入力を基にカッコよく書き換える / Always rewrite user input to make it cool and engaging**
- **ストーリーテリング的に魅力的にする / Make it compelling with storytelling**
- **感情やインサイトを強調する / Emphasize emotions and insights**

### 例 / Examples

#### URL例 / URL Examples
```
❌ 悪い例 / Bad: /戸田達昭さんの会/
✅ 良い例 / Good: /toda-tatsuaki-event/

❌ 悪い例 / Bad: /山梨旅行記/
✅ 良い例 / Good: /yamanashi-travel-diary/
```

#### コンテンツ例 / Content Examples
```
❌ 悪い例 / Bad: 
"昨日は戸田さんの会に行った。いい話だった。"

✅ 良い例 / Good:
"Last night, I attended an extraordinary gathering with Tatsuaki Toda, one of Yamanashi's most inspiring figures. His philosophy struck me deeply - he believes in the goodness of people and never turns down an opportunity. 'I want to be laughing when I die,' he said, and that resonated with something profound inside me."
```

### 実装 / Implementation
- WordPressのAPIリクエストで`"title"`, `"slug"`, `"content"`全て英語
- スラグは小文字でハイフン区切り
- 日本の固有名詞はローマ字表記
- コンテンツは魅力的な英語ストーリーに変換

## 技術実装 / Technical Implementation
```json
POST_DATA='{
    "title": "English Title",
    "slug": "english-url-slug", 
    "content": "Compelling English content with storytelling...",
    "status": "publish"
}'
```

このルールは全てのWordPress投稿に適用する。
This rule applies to all WordPress posts.