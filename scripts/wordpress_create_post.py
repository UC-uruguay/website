#!/usr/bin/env python3
"""
WordPress Post Creation via Admin Session
Create "HP開設のお知らせ" post about UC introduction and Claude Code usage
"""
import urllib.request
import urllib.parse
import http.cookiejar
import json
import re
import html

class WordPressPostCreator:
    def __init__(self, site_url, username, password):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.password = password
        
        # Setup session with cookies
        self.cookie_jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie_jar))
        self.opener.addheaders = [('User-Agent', 'Claude-Code-WordPress-PostCreator/1.0')]
    
    def admin_login(self):
        """Login to WordPress admin panel"""
        try:
            print("🔐 Logging into WordPress admin...")
            
            # Get login page
            login_url = f"{self.site_url}/wp-login.php"
            response = self.opener.open(login_url)
            login_page = response.read().decode('utf-8')
            
            # Prepare login data
            login_data = {
                'log': self.username,
                'pwd': self.password,
                'wp-submit': 'ログイン',
                'redirect_to': f"{self.site_url}/wp-admin/",
                'testcookie': '1'
            }
            
            # Submit login
            data = urllib.parse.urlencode(login_data).encode('utf-8')
            request = urllib.request.Request(login_url, data=data)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('Referer', login_url)
            
            response = self.opener.open(request)
            
            # Check login success
            if 'wp-admin' in response.geturl() and 'wp-login' not in response.geturl():
                print("✅ Admin login successful!")
                return True
            else:
                print("❌ Admin login failed")
                return False
                
        except Exception as e:
            print(f"❌ Admin login error: {e}")
            return False
    
    def get_post_form(self):
        """Get new post form and extract nonce"""
        try:
            print("📝 Getting post creation form...")
            
            new_post_url = f"{self.site_url}/wp-admin/post-new.php"
            response = self.opener.open(new_post_url)
            page_content = response.read().decode('utf-8')
            
            # Extract nonce for post creation
            nonce_pattern = r'name="_wpnonce"[^>]*value="([^"]*)"'
            nonce_match = re.search(nonce_pattern, page_content)
            
            if not nonce_match:
                print("❌ Could not find post creation nonce")
                return None, None
                
            nonce = nonce_match.group(1)
            print(f"🔑 Found post nonce: {nonce[:10]}...")
            
            return nonce, page_content
            
        except Exception as e:
            print(f"❌ Error getting post form: {e}")
            return None, None
    
    def create_post_content(self):
        """Generate the blog post content"""
        content = """
<h2>🎉 UC Site のホームページが開設されました！</h2>

<p>この度、UCの活動や情報を発信するためのホームページを開設いたしました。このページでは、UCの紹介と今後の展望についてお知らせいたします。</p>

<h3>📖 このサイトの目的</h3>
<p>このホームページは以下の目的で作成されました：</p>
<ul>
<li><strong>UCの活動紹介</strong> - 私たちの取り組みや成果を皆様にお伝えします</li>
<li><strong>情報発信</strong> - 最新のお知らせやイベント情報をタイムリーに配信します</li>
<li><strong>技術革新の実践</strong> - 最新のAI技術を活用したサイト運営を実現します</li>
</ul>

<h3>🤖 革新的な制作手順</h3>
<p>このホームページは、従来とは異なる革新的な手順で作成されました：</p>

<h4>1. Claude Code による開発</h4>
<p>サイトの構築には<strong>Claude Code</strong>を使用しました。Claude Codeは、Anthropic社が開発したAIアシスタントで、直接的なコード生成やファイル操作が可能です。</p>

<h4>2. MCP (Model Context Protocol) の活用</h4>
<p>WordPress との連携には<strong>MCP</strong>を使用し、AI とWordPress間の効率的な通信を実現しました。これにより、従来手動で行っていた作業を自動化できました。</p>

<h4>3. JWT認証による安全な操作</h4>
<p>セキュリティを重視し、JWT (JSON Web Token) 認証を使用してWordPress API へのアクセスを管理しています。</p>

<h3>🚀 今後の展望と完全自動更新</h3>
<p>このサイトは、今後以下の方向で発展していきます：</p>

<h4>完全自動更新システム</h4>
<ul>
<li><strong>WordPress コア自動更新</strong> - セキュリティパッチや新機能を自動適用</li>
<li><strong>コンテンツ自動生成</strong> - Claude Code によるブログ記事の自動作成</li>
<li><strong>プラグイン・テーマ管理</strong> - 依存関係を考慮した安全な自動更新</li>
<li><strong>パフォーマンス最適化</strong> - サイトの表示速度やSEOの自動改善</li>
</ul>

<h4>AI駆動のコンテンツ管理</h4>
<ul>
<li>定期的な情報更新の自動実行</li>
<li>ユーザーの興味に基づくコンテンツ提案</li>
<li>多言語対応の自動展開</li>
</ul>

<h3>🔧 技術的な特徴</h3>
<p>このサイトで使用されている主な技術：</p>
<ul>
<li><strong>WordPress 6.8.2</strong> - 最新の安定版を使用</li>
<li><strong>REST API</strong> - 外部システムとの連携</li>
<li><strong>JWT Authentication</strong> - セキュアな認証システム</li>
<li><strong>Claude Code Integration</strong> - AI による直接的なサイト管理</li>
</ul>

<h3>📅 今後の予定</h3>
<p>継続的な改善と機能追加を予定しております：</p>
<ul>
<li>週次自動更新の実装</li>
<li>コンテンツ品質の自動監視</li>
<li>ユーザーフィードバックの自動収集と反映</li>
<li>新機能の段階的ロールアウト</li>
</ul>

<hr>

<p><em>このサイトは、人工知能と人間の協働による新しい形のウェブサイト運営の実践例です。今後とも、革新的な技術を活用しながら、皆様に価値のある情報をお届けしてまいります。</em></p>

<p><strong>最終更新：</strong> 2025年8月29日<br>
<strong>作成者：</strong> Claude Code + UC Team<br>
<strong>技術スタック：</strong> WordPress, Claude Code, MCP, JWT Auth</p>
"""
        
        title = "HP開設のお知らせ - UCサイトへようこそ"
        
        return title, content
    
    def publish_post(self, title, content, nonce):
        """Publish the blog post"""
        try:
            print("🚀 Publishing blog post...")
            
            # Prepare post data
            post_data = {
                'post_title': title,
                'content': content,
                'post_status': 'publish',
                'post_type': 'post',
                'comment_status': 'open',
                'ping_status': 'open',
                'post_category[]': '1',  # Uncategorized
                'tax_input[post_tag]': 'HP開設,Claude Code,MCP,自動更新,UC',
                '_wpnonce': nonce,
                '_wp_http_referer': '/wp-admin/post-new.php',
                'action': 'editpost',
                'post_ID': '0',
                'meta-box-order-nonce': nonce,
                'closedpostboxesnonce': nonce,
                'save': '公開'
            }
            
            # Submit post
            post_url = f"{self.site_url}/wp-admin/post.php"
            data = urllib.parse.urlencode(post_data, quote_via=urllib.parse.quote).encode('utf-8')
            
            request = urllib.request.Request(post_url, data=data)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8')
            request.add_header('Referer', f"{self.site_url}/wp-admin/post-new.php")
            
            response = self.opener.open(request)
            result_url = response.geturl()
            
            # Check if post was created successfully
            if 'post.php' in result_url and 'message=6' in result_url:
                print("✅ Blog post published successfully!")
                # Extract post ID from URL
                post_id_match = re.search(r'post=(\d+)', result_url)
                if post_id_match:
                    post_id = post_id_match.group(1)
                    print(f"📝 Post ID: {post_id}")
                    print(f"🔗 Post URL: {self.site_url}/?p={post_id}")
                return True
            else:
                print(f"⚠️ Post creation status unclear. Redirect URL: {result_url}")
                return False
                
        except Exception as e:
            print(f"❌ Error publishing post: {e}")
            return False
    
    def create_announcement_post(self):
        """Create the HP announcement post"""
        print("🚀 Claude Code WordPress Post Creator")
        print("=" * 50)
        
        # Step 1: Login
        if not self.admin_login():
            return False
        
        # Step 2: Get post form
        nonce, form_content = self.get_post_form()
        if not nonce:
            return False
        
        # Step 3: Generate content
        title, content = self.create_post_content()
        print(f"📰 Post title: {title}")
        print(f"📄 Content length: {len(content)} characters")
        
        # Step 4: Publish post
        success = self.publish_post(title, content, nonce)
        
        if success:
            print("\n🎉 HP開設のお知らせ記事が正常に公開されました！")
            print("🌐 サイトを確認して記事をご覧ください。")
        else:
            print("\n❌ 記事の公開に問題が発生しました。")
            print("🔍 WordPress管理画面で手動確認をお願いします。")
        
        return success

def main():
    site_url = "https://uc.x0.com"
    username = "uc-japan" 
    password = "Tis30426810cd067d!"
    
    creator = WordPressPostCreator(site_url, username, password)
    success = creator.create_announcement_post()
    
    return success

if __name__ == "__main__":
    main()