# WordPress 完全自動化設定手順

## 🎯 目標
Claude CodeによるWordPressの完全自動管理を実現する

## 📋 現在の状況
- ✅ JWT認証プラグイン設定済み
- ✅ WordPressへのログイン・更新確認が可能
- ⚠️ REST API投稿権限に制限あり

## 🔧 完全自動化に必要な設定

### 1. Application Passwords の設定

**手順:**
1. WordPress管理画面にログイン (`https://uc.x0.com/wp-admin/`)
2. `ユーザー` → `プロフィール` をクリック
3. 画面下部の `Application Passwords` セクションを見つける
4. 新しいアプリケーション名: `Claude-Code-Automation` を入力
5. `新しいアプリケーションパスワードを追加` をクリック
6. 生成されたパスワードを安全に保存

**設定後の利点:**
- REST API経由での投稿作成が可能
- より安全な認証方式
- 通常パスワードとは独立した管理

### 2. ユーザー権限の確認

**確認項目:**
- 現在のユーザー (`uc-japan`) が `管理者` 権限を持っているか
- `publish_posts` 権限があるか
- `edit_posts` 権限があるか

**確認方法:**
```bash
curl -X GET "https://uc.x0.com/wp-json/wp/v2/users/me" \
-H "Authorization: Basic [base64_encoded_app_password]"
```

### 3. プラグインの権限設定確認

**JWT Authentication for WP REST API の設定:**
- プラグイン設定で REST API アクセス権限を確認
- 必要に応じて権限レベルを調整

### 4. WordPress設定の最適化

**wp-config.php に追加すべき設定:**
```php
// 自動更新の有効化
define('WP_AUTO_UPDATE_CORE', true);

// REST API の有効化（必要な場合）
define('WP_REST_API_ENABLED', true);

// ファイル編集の許可
define('DISALLOW_FILE_EDIT', false);
```

## 🚀 完全自動化の実装段階

### Phase 1: 基本自動化 (完了済み)
- ✅ WordPress更新チェック
- ✅ JWT認証システム
- ✅ 管理画面への自動ログイン

### Phase 2: コンテンツ自動化 (次のステップ)
- 📝 REST API経由での投稿作成
- 🏷️ 自動タグ付け・カテゴリー分類
- 📸 画像アップロード・最適化

### Phase 3: 高度な自動化
- 📊 SEO最適化の自動実行
- 🔄 定期的なコンテンツ更新
- 📈 パフォーマンス監視・改善
- 🛡️ セキュリティ監査の自動化

### Phase 4: AI駆動管理
- 🧠 コンテンツ品質の自動評価
- 📝 ユーザー行動に基づく記事生成
- 🎨 デザインの自動最適化
- 🌍 多言語コンテンツの自動展開

## 🛠️ 技術スタック

### 現在使用中
- **WordPress**: 6.8.2 (最新)
- **Claude Code**: Anthropic AI Assistant
- **JWT Auth Plugin**: JSON Web Token 認証
- **MCP Protocol**: Model Context Protocol

### 今後導入予定
- **Application Passwords**: より安全なAPI認証
- **Cron Jobs**: 定期実行タスク
- **Webhook Integration**: リアルタイム更新通知
- **Performance Monitoring**: サイト速度・稼働監視

## 📋 次回実行時のチェックリスト

### 事前確認
- [ ] Application Password が設定済みか
- [ ] ユーザー権限が適切か
- [ ] プラグインが最新版か
- [ ] バックアップが取得済みか

### 実行項目
- [ ] WordPress コア更新
- [ ] プラグイン更新
- [ ] テーマ更新
- [ ] 新規記事の投稿
- [ ] SEOチェック
- [ ] パフォーマンステスト

### 事後確認
- [ ] サイトが正常に表示されるか
- [ ] すべての機能が動作するか
- [ ] エラーログに問題がないか
- [ ] バックアップが正常に作成されたか

## 🎯 完全自動化の最終目標

**理想的な自動化フロー:**
1. 定期的（週次）にClaude Codeが自動実行
2. WordPress・プラグイン・テーマの更新チェック
3. 必要に応じて自動更新実行
4. 新しいコンテンツの自動生成・投稿
5. サイトの健全性チェック
6. パフォーマンス最適化
7. レポート生成・通知

これにより、**人の手を一切介さない完全自動運用**を実現します。