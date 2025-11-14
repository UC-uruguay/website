#!/usr/bin/env python3
"""
WordPress Post Creation via REST API with JWT
Alternative approach using WordPress REST API directly
"""
import urllib.request
import urllib.parse
import json

class WordPressAPIPostCreator:
    def __init__(self, site_url, username, password):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.password = password
        self.jwt_token = None
    
    def get_jwt_token(self):
        """Get JWT token for authentication"""
        try:
            login_data = {
                'username': self.username,
                'password': self.password
            }
            
            data = json.dumps(login_data).encode('utf-8')
            request = urllib.request.Request(
                f"{self.site_url}/wp-json/jwt-auth/v1/token",
                data=data
            )
            request.add_header('Content-Type', 'application/json')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            if 'token' in result:
                self.jwt_token = result['token']
                print(f"✅ JWT Token acquired successfully")
                return True
            else:
                print(f"❌ JWT Token acquisition failed: {result}")
                return False
                
        except Exception as e:
            print(f"❌ Error getting JWT token: {e}")
            return False
    
    def create_post_content(self):
        """Generate the blog post content"""
        content = """<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎉 UC Site のホームページが開設されました！</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>この度、UCの活動や情報を発信するためのホームページを開設いたしました。このページでは、UCの紹介と今後の展望についてお知らせいたします。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">📖 このサイトの目的</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>このホームページは以下の目的で作成されました：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>UCの活動紹介</strong> - 私たちの取り組みや成果を皆様にお伝えします</li><li><strong>情報発信</strong> - 最新のお知らせやイベント情報をタイムリーに配信します</li><li><strong>技術革新の実践</strong> - 最新のAI技術を活用したサイト運営を実現します</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🤖 革新的な制作手順</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>このホームページは、従来とは異なる革新的な手順で作成されました：</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">1. Claude Code による開発</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>サイトの構築には<strong>Claude Code</strong>を使用しました。Claude Codeは、Anthropic社が開発したAIアシスタントで、直接的なコード生成やファイル操作が可能です。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">2. MCP (Model Context Protocol) の活用</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>WordPress との連携には<strong>MCP</strong>を使用し、AI とWordPress間の効率的な通信を実現しました。これにより、従来手動で行っていた作業を自動化できました。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">3. JWT認証による安全な操作</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>セキュリティを重視し、JWT (JSON Web Token) 認証を使用してWordPress API へのアクセスを管理しています。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🚀 今後の展望と完全自動更新</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>このサイトは、今後以下の方向で発展していきます：</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">完全自動更新システム</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>WordPress コア自動更新</strong> - セキュリティパッチや新機能を自動適用</li><li><strong>コンテンツ自動生成</strong> - Claude Code によるブログ記事の自動作成</li><li><strong>プラグイン・テーマ管理</strong> - 依存関係を考慮した安全な自動更新</li><li><strong>パフォーマンス最適化</strong> - サイトの表示速度やSEOの自動改善</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">AI駆動のコンテンツ管理</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><li>定期的な情報更新の自動実行</li><li>ユーザーの興味に基づくコンテンツ提案</li><li>多言語対応の自動展開</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🔧 技術的な特徴</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>このサイトで使用されている主な技術：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><li><strong>WordPress 6.8.2</strong> - 最新の安定版を使用</li><li><strong>REST API</strong> - 外部システムとの連携</li><li><strong>JWT Authentication</strong> - セキュアな認証システム</li><li><strong>Claude Code Integration</strong> - AI による直接的なサイト管理</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">📅 今後の予定</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>継続的な改善と機能追加を予定しております：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><li>週次自動更新の実装</li><li>コンテンツ品質の自動監視</li><li>ユーザーフィードバックの自動収集と反映</li><li>新機能の段階的ロールアウト</li></ul>
<!-- /wp:list -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><em>このサイトは、人工知能と人間の協働による新しい形のウェブサイト運営の実践例です。今後とも、革新的な技術を活用しながら、皆様に価値のある情報をお届けしてまいります。</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>最終更新：</strong> 2025年8月29日<br><strong>作成者：</strong> Claude Code + UC Team<br><strong>技術スタック：</strong> WordPress, Claude Code, MCP, JWT Auth</p>
<!-- /wp:paragraph -->"""
        
        title = "HP開設のお知らせ - UCサイトへようこそ"
        
        return title, content
    
    def create_post_via_api(self, title, content):
        """Create post via WordPress REST API"""
        try:
            print("🚀 Creating post via REST API...")
            
            post_data = {
                'title': title,
                'content': content,
                'status': 'publish',
                'tags': [1, 2, 3],  # Will create tags if they don't exist
                'meta': {
                    '_wp_post_author': 1
                }
            }
            
            # Try with JWT token first
            if self.jwt_token:
                print("🔐 Using JWT authentication...")
                data = json.dumps(post_data).encode('utf-8')
                request = urllib.request.Request(
                    f"{self.site_url}/wp-json/wp/v2/posts",
                    data=data
                )
                request.add_header('Content-Type', 'application/json')
                request.add_header('Authorization', f'Bearer {self.jwt_token}')
                
                try:
                    with urllib.request.urlopen(request) as response:
                        result = json.loads(response.read().decode('utf-8'))
                        print(f"✅ Post created successfully!")
                        print(f"📝 Post ID: {result.get('id')}")
                        print(f"🔗 Post URL: {result.get('link')}")
                        return True
                except urllib.error.HTTPError as e:
                    error_content = e.read().decode('utf-8')
                    print(f"❌ JWT API Error: {e.code} - {error_content}")
            
            # Try with basic auth as fallback
            print("🔐 Trying basic authentication...")
            import base64
            credentials = f"{self.username}:{self.password}"
            token = base64.b64encode(credentials.encode()).decode()
            
            data = json.dumps(post_data).encode('utf-8')
            request = urllib.request.Request(
                f"{self.site_url}/wp-json/wp/v2/posts",
                data=data
            )
            request.add_header('Content-Type', 'application/json')
            request.add_header('Authorization', f'Basic {token}')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
                print(f"✅ Post created successfully via Basic Auth!")
                print(f"📝 Post ID: {result.get('id')}")
                print(f"🔗 Post URL: {result.get('link')}")
                return True
                
        except Exception as e:
            print(f"❌ Error creating post: {e}")
            return False
    
    def create_announcement_post(self):
        """Create the HP announcement post"""
        print("🚀 Claude Code WordPress API Post Creator")
        print("=" * 50)
        
        # Step 1: Get JWT token
        print("🔐 Getting JWT token...")
        if not self.get_jwt_token():
            print("⚠️ JWT failed, will try basic auth")
        
        # Step 2: Generate content
        title, content = self.create_post_content()
        print(f"📰 Post title: {title}")
        print(f"📄 Content length: {len(content)} characters")
        
        # Step 3: Create post
        success = self.create_post_via_api(title, content)
        
        if success:
            print("\n🎉 HP開設のお知らせ記事が正常に公開されました！")
            print("🌐 https://uc.x0.com でサイトを確認してください。")
        else:
            print("\n❌ REST API経由での記事公開に失敗しました。")
            print("🔍 手動での投稿作成をお試しください。")
        
        return success

def main():
    site_url = "https://uc.x0.com"
    username = "uc-japan"
    password = "Tis30426810cd067d!"
    
    creator = WordPressAPIPostCreator(site_url, username, password)
    success = creator.create_announcement_post()
    
    return success

if __name__ == "__main__":
    main()