#!/usr/bin/env python3
"""
WordPress UC Personal Site Builder - Fixed Version
Transform the site into UC's personal introduction page
"""
import urllib.request
import json
import base64
import os
import mimetypes

class UCPersonalSiteBuilder:
    def __init__(self):
        # Load authentication info
        try:
            with open('/home/uc/wordpress_auth.json', 'r') as f:
                self.auth_info = json.load(f)
        except FileNotFoundError:
            print("❌ 認証情報が見つかりません")
            return
        
        self.site_url = self.auth_info['site_url']
        self.token = self.auth_info['base64_token']
        self.media_id = None
    
    def upload_profile_image(self):
        """Upload UC's profile image to WordPress media library"""
        try:
            print("📸 プロフィール画像をアップロード中...")
            
            # Read the image file
            with open('/home/uc/uc.jpg', 'rb') as f:
                image_data = f.read()
            
            # Create media upload request
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/media")
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'image/jpeg')
            request.add_header('Content-Disposition', 'attachment; filename="uc-profile.jpg"')
            request.data = image_data
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            self.media_id = result.get('id')
            print(f"✅ プロフィール画像アップロード成功! (ID: {self.media_id})")
            print(f"🔗 画像URL: {result.get('source_url')}")
            
            return result.get('source_url')
            
        except Exception as e:
            print(f"❌ 画像アップロードエラー: {e}")
            return None
    
    def create_personal_page_content(self, image_url):
        """Create UC's personal introduction page content"""
        # Use regular string concatenation to avoid f-string issues
        content = f"""<!-- wp:cover {{"url":"{image_url}","id":{self.media_id},"dimRatio":30,"overlayColor":"black","minHeight":60,"minHeightUnit":"vh","align":"full"}} -->
<div class="wp-block-cover alignfull is-light" style="min-height:60vh">
<span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-30"></span>
<img class="wp-block-cover__image-background wp-image-{self.media_id}" alt="" src="{image_url}" data-object-fit="cover"/>
<div class="wp-block-cover__inner-container">
<!-- wp:group -->
<div class="wp-block-group">
<!-- wp:heading {{"textAlign":"center","level":1,"style":{{"typography":{{"fontSize":"3.5rem","fontWeight":"700"}}}},"textColor":"base"}} -->
<h1 class="wp-block-heading has-text-align-center has-base-color" style="font-size:3.5rem;font-weight:700">Hi, I'm Yūshi! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.3rem"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.3rem">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div></div>
<!-- /wp:cover -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#fafafa"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#fafafa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column {{"width":"40%"}} -->
<div class="wp-block-column" style="flex-basis:40%">
<!-- wp:image {{"id":{self.media_id},"width":"280px","height":"280px","scale":"cover","style":{{"border":{{"radius":"50%"}}}}}} -->
<figure class="wp-block-image is-resized has-custom-border">
<img src="{image_url}" alt="Yushi Nakashima Profile" class="wp-image-{self.media_id}" style="border-radius:50%;object-fit:cover;width:280px;height:280px"/>
</figure>
<!-- /wp:image -->

<!-- wp:heading {{"textAlign":"center","level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.4rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:1.4rem;font-weight:600">Connect with me!</h3>
<!-- /wp:heading -->

<!-- wp:social-links {{"openInNewTab":true,"showLabels":true,"layout":{{"type":"flex","justifyContent":"center","flexWrap":"wrap"}}}} -->
<ul class="wp-block-social-links">
<!-- wp:social-link {{"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"}} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor">Instagram</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://x.com/TORIAEZU_OU","service":"x"}} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor">X (Twitter)</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"}} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor">TikTok</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"}} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor">LinkedIn</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"width":"60%"}} -->
<div class="wp-block-column" style="flex-basis:60%">
<!-- wp:heading {{"level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h2 class="wp-block-heading" style="color:#2c3e50;font-size:2.2rem;font-weight:600">About Me</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"1.1rem","lineHeight":"1.7"}}}}}} -->
<p style="font-size:1.1rem;line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>Yūshi (ゆーし)</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"1.1rem","lineHeight":"1.7"}}}}}} -->
<p style="font-size:1.1rem;line-height:1.7">People often say I'm a bit unusual, but I love creativity and bold ideas, even if they seem unrealistic.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">👨‍👩‍👦 Family & Daily Life</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}}}}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>A proud husband and father — I can't stop saying how cute my wife and son are.</li>
<li>Enjoy spending weekends together exploring local nature, hot springs, and festivals.</li>
<li>Ichikun is almost 3 years old and already full of curiosity and energy.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🎯 Hobbies & Interests</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}}}}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li><strong>Making Friends:</strong> I enjoy making new friends—it's the most important thing in my life.</li>
<li><strong>Wine & Food:</strong> I enjoy tasting and learning about wines, especially Italian and Yamanashi wines.</li>
<li><strong>Time Capsule:</strong> I love burying time capsules in different parts of the world.</li>
<li><strong>Creativity:</strong> Making educational games for my son, experimenting with AI-generated music, videos, and short films.</li>
<li><strong>Poetry & Classics:</strong> Studying traditional Japanese things like poetry, bonsai and exploring cultural depth.</li>
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#ffffff"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🌏 Travel & Culture</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}}}}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>Love to travel both in Japan and abroad — I travel all 47 prefectures and around 40 countries.</li>
<li>Interested in Buddhist culture, temples, and unique local experiences.</li>
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">✨ Inspirations</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}}}}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>Believe in the beauty of connecting with others through vision and empathy rather than just information.</li>
<li>Inspired by the idea of a "world-wide common understanding beyond religion."</li>
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#f8f9fa"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {{"textAlign":"center","level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">📱 Gallery & Interests</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}}}}}} -->
<p class="has-text-align-center" style="font-size:3rem">📸</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Family Moments</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}}}}}} -->
<p class="has-text-align-center" style="font-size:3rem">🍇</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Wine Tasting</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}}}}}} -->
<p class="has-text-align-center" style="font-size:3rem">🛕</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Temples & Travel</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}}}}}} -->
<p class="has-text-align-center" style="font-size:3rem">🎨</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">AI Creative Projects</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"40px","bottom":"40px","left":"20px","right":"20px"}}}},"color":{{"background":"#2c3e50"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#2c3e50;padding-top:40px;padding-bottom:40px;padding-left:20px;padding-right:20px">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.2rem","lineHeight":"1.6"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.2rem;line-height:1.6"><em>"I believe in connecting with others through vision and empathy. Let's create a world-wide common understanding beyond religion and build meaningful friendships together!"</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1rem","fontWeight":"600"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1rem;font-weight:600">— Yūshi Nakashima</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->"""

        return "UC Personal Introduction", content
    
    def create_homepage(self, title, content):
        """Create UC's homepage as a static page"""
        try:
            print("🏠 個人紹介ホームページを作成中...")
            
            # Create the page
            page_data = {
                "title": title,
                "content": content,
                "status": "publish",
                "type": "page",
                "slug": "home",
                "template": "",
                "meta": {
                    "created_by": "Claude Code",
                    "page_type": "personal_introduction"
                }
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print(f"✅ ホームページ作成成功!")
            print(f"📝 ページID: {result.get('id')}")
            print(f"🔗 ページURL: {result.get('link')}")
            
            return result
            
        except Exception as e:
            print(f"❌ ホームページ作成エラー: {e}")
            return None
    
    def set_homepage_as_front_page(self, page_id):
        """Set the created page as the front page"""
        try:
            print("⚙️ フロントページ設定中...")
            
            # Update WordPress settings
            settings_data = {
                "show_on_front": "page",
                "page_on_front": page_id,
                "title": "Yūshi Nakashima - Personal Site",
                "description": "Welcome to Yūshi's world! A creative soul from Yamanashi, Japan, passionate about connecting people and exploring cultures."
            }
            
            data = json.dumps(settings_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/settings", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print("✅ フロントページ設定完了!")
            print(f"📰 サイトタイトル: {result.get('title')}")
            print(f"📄 サイト説明: {result.get('description')}")
            
            return True
            
        except Exception as e:
            print(f"❌ フロントページ設定エラー: {e}")
            return False
    
    def build_uc_personal_site(self):
        """Main function to build UC's personal site"""
        print("🚀 UC Personal Site Builder")
        print("=" * 50)
        
        # Step 1: Upload profile image
        image_url = self.upload_profile_image()
        if not image_url:
            print("❌ プロフィール画像のアップロードに失敗しました")
            return False
        
        # Step 2: Create page content
        title, content = self.create_personal_page_content(image_url)
        
        # Step 3: Create homepage
        homepage_result = self.create_homepage(title, content)
        if not homepage_result:
            return False
        
        # Step 4: Set as front page
        success = self.set_homepage_as_front_page(homepage_result.get('id'))
        
        if success:
            print("\n🎉 UC個人紹介サイトの構築が完了しました!")
            print("=" * 60)
            print(f"🌐 サイトURL: {self.site_url}")
            print(f"✏️ 管理画面: {self.site_url}/wp-admin/")
            print(f"📱 レスポンシブデザイン: 対応済み")
            print(f"🎨 プロフィール画像: 配置済み")
            print(f"📝 SNSリンク: 設定済み")
            print("\n👀 ブラウザでサイトをご確認ください!")
        
        return success

def main():
    builder = UCPersonalSiteBuilder()
    builder.build_uc_personal_site()

if __name__ == "__main__":
    main()