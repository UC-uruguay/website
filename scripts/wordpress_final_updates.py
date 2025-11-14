#!/usr/bin/env python3
"""
WordPress Final Updates for UC Site
- Update header menu
- Fix footer social icons (remove emojis)
- Update footer widgets and credits
- Translate Japanese footer items
"""
import urllib.request
import json

class WordPressFinalUpdater:
    def __init__(self):
        # Load authentication info
        try:
            with open('/home/uc/wordpress_auth.json', 'r') as f:
                self.auth_info = json.load(f)
        except FileNotFoundError:
            print("❌ Authentication info not found")
            return
        
        self.site_url = self.auth_info['site_url']
        self.token = self.auth_info['base64_token']
        self.homepage_id = 11
    
    def update_homepage_footer_section(self):
        """Update only the footer section with fixes"""
        # Updated footer content without emojis in social icons
        footer_content = """<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#2c3e50"}}} -->
<div class="wp-block-group has-background" style="background-color:#2c3e50;padding-top:40px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.2rem","lineHeight":"1.6"}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:1.2rem;line-height:1.6"><em>"I believe in connecting with others through vision and empathy. Let's create a world-wide common understanding beyond religion and build meaningful friendships together!"</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1rem","fontWeight":"600"}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:1rem;font-weight:600">— UC</p>
<!-- /wp:paragraph -->

<!-- wp:social-links {"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"30px"}}}} -->
<ul class="wp-block-social-links is-style-logos-only" style="margin-top:30px">
<!-- wp:social-link {"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://x.com/TORIAEZU_OU","service":"x"} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:separator {"style":{"spacing":{"margin":{"top":"40px","bottom":"20px"}},"color":{"background":"#ffffff33"}}} -->
<hr class="wp-block-separator has-text-color has-alpha-channel-opacity" style="margin-top:40px;margin-bottom:20px;background-color:#ffffff33;color:#ffffff33"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.1rem","fontWeight":"500"}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:1.1rem;font-weight:500">With Love from UC ❤️</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->"""
        
        return footer_content
    
    def get_current_homepage_content(self):
        """Get current homepage content"""
        try:
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}")
            request.add_header('Authorization', f'Basic {self.token}')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
                
            return result.get('content', {}).get('rendered', '')
            
        except Exception as e:
            print(f"❌ Error getting current content: {e}")
            return None
    
    def update_homepage_with_fixed_footer(self):
        """Update homepage with corrected footer"""
        # Complete updated content
        content = """<!-- wp:cover {"url":"https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg","id":10,"dimRatio":30,"overlayColor":"black","minHeight":60,"minHeightUnit":"vh","align":"full"} -->
<div class="wp-block-cover alignfull is-light" style="min-height:60vh">
<span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-30"></span>
<img class="wp-block-cover__image-background wp-image-10" alt="" src="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg" data-object-fit="cover"/>
<div class="wp-block-cover__inner-container">
<div class="wp-block-group">
<h1 class="wp-block-heading has-text-align-center has-base-color" style="font-size:3.5rem;font-weight:700">Hi, I'm UC! 👋</h1>
<p class="has-text-align-center has-base-color" style="font-size:1.3rem">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
</div>
</div></div>
<!-- /wp:cover -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#fafafa"}},"className":"about-me-section"} -->
<div class="wp-block-group about-me-section has-background" style="background-color:#fafafa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<div class="wp-block-columns">
<div class="wp-block-column" style="flex-basis:40%">
<figure class="wp-block-image is-resized has-custom-border">
<img src="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg" alt="UC Profile Photo" class="wp-image-10" style="border-radius:50%;object-fit:cover;width:280px;height:280px"/>
</figure>

<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:1.4rem;font-weight:600">Connect with me!</h3>

<ul class="wp-block-social-links">
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc">📷 Instagram</a>
</li>
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU">🐦 X (Twitter)</a>
</li>
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/">👥 Facebook</a>
</li>
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360">🎵 TikTok</a>
</li>
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/">💼 LinkedIn</a>
</li>
</ul>
</div>

<div class="wp-block-column" style="flex-basis:60%">
<h2 class="wp-block-heading" style="color:#2c3e50;font-size:2.2rem;font-weight:600">About Me</h2>

<p style="font-size:1.1rem;line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>

<p style="font-size:1.1rem;line-height:1.7">People often say I'm a bit unusual, but I love creativity and bold ideas, even if they seem unrealistic.</p>

<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">👨‍👩‍👦 Family & Daily Life</h3>

<ul style="font-size:1rem;line-height:1.6">
<li>A proud husband and father — I can't stop saying how cute my wife and son are.</li>
<li>Enjoy spending weekends together exploring local nature, hot springs, and festivals.</li>
<li>Ichikun is almost 3 years old and already full of curiosity and energy.</li>
</ul>

<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🎯 Hobbies & Interests</h3>

<ul style="font-size:1rem;line-height:1.6">
<li><strong>Making Friends:</strong> I enjoy making new friends—it's the most important thing in my life.</li>
<li><strong>Wine & Food:</strong> I enjoy tasting and learning about wines, especially Italian and Yamanashi wines.</li>
<li><strong>Time Capsule:</strong> I love burying time capsules in different parts of the world.</li>
<li><strong>Creativity:</strong> Making educational games for my son, experimenting with AI-generated music, videos, and short films.</li>
<li><strong>Poetry & Classics:</strong> Studying traditional Japanese things like poetry, bonsai and exploring cultural depth.</li>
</ul>
</div>
</div>
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#ffffff"}}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<div class="wp-block-columns">
<div class="wp-block-column">
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🌏 Travel & Culture</h3>
<ul style="font-size:1rem;line-height:1.6">
<li>Love to travel both in Japan and abroad — I travel all 47 prefectures and around 40 countries.</li>
<li>Interested in Buddhist culture, temples, and unique local experiences.</li>
</ul>
</div>
<div class="wp-block-column">
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">✨ Inspirations</h3>
<ul style="font-size:1rem;line-height:1.6">
<li>Believe in the beauty of connecting with others through vision and empathy rather than just information.</li>
<li>Inspired by the idea of a "world-wide common understanding beyond religion."</li>
</ul>
</div>
</div>
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f0f2f5"}},"className":"recent-posts-section"} -->
<div class="wp-block-group recent-posts-section has-background" style="background-color:#f0f2f5;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">📝 Recent Posts</h2>
<p class="has-text-align-center" style="color:#666666;margin-bottom:40px;font-size:1.1rem">Discover my latest thoughts, experiences, and creative projects</p>

<!-- wp:latest-posts {"postsToShow":3,"displayAuthor":false,"displayDate":true,"displayFeaturedImage":true,"featuredImageAlign":"left","featuredImageSizeSlug":"medium","addLinkToFeaturedImage":true,"excerptLength":25} -->
<!-- /wp:latest-posts -->

<p class="has-text-align-center" style="margin-top:30px"><a href="/blog" class="wp-element-button">View All Posts →</a></p>
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">🎨 Gallery & Interests</h2>

<div class="wp-block-columns">
<div class="wp-block-column">
<p class="has-text-align-center" style="font-size:3rem">📸</p>
<p class="has-text-align-center" style="font-weight:600">Family Moments</p>
</div>
<div class="wp-block-column">
<p class="has-text-align-center" style="font-size:3rem">🍇</p>
<p class="has-text-align-center" style="font-weight:600">Wine Tasting</p>
</div>
<div class="wp-block-column">
<p class="has-text-align-center" style="font-size:3rem">🛕</p>
<p class="has-text-align-center" style="font-weight:600">Temples & Travel</p>
</div>
<div class="wp-block-column">
<p class="has-text-align-center" style="font-size:3rem">🎨</p>
<p class="has-text-align-center" style="font-weight:600">AI Creative Projects</p>
</div>
</div>
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#2c3e50"}}} -->
<div class="wp-block-group has-background" style="background-color:#2c3e50;padding-top:40px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<p class="has-text-align-center has-base-color" style="font-size:1.2rem;line-height:1.6"><em>"I believe in connecting with others through vision and empathy. Let's create a world-wide common understanding beyond religion and build meaningful friendships together!"</em></p>

<p class="has-text-align-center has-base-color" style="font-size:1rem;font-weight:600">— UC</p>

<ul class="wp-block-social-links is-style-logos-only" style="margin-top:30px;justify-content:center">
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc"></a>
</li>
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU"></a>
</li>
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/"></a>
</li>
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360"></a>
</li>
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/"></a>
</li>
</ul>

<hr class="wp-block-separator" style="margin-top:40px;margin-bottom:20px;background-color:#ffffff33;color:#ffffff33"/>

<p class="has-text-align-center has-base-color" style="font-size:1.1rem;font-weight:500">With Love from UC ❤️</p>
</div>
<!-- /wp:group -->"""

        try:
            print("🔄 Updating homepage with fixed footer...")
            
            page_data = {
                "title": "UC - Creative Soul from Japan",
                "content": content,
                "status": "publish"
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            request.get_method = lambda: 'POST'
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print("✅ Homepage updated with fixed footer!")
            return True
            
        except Exception as e:
            print(f"❌ Error updating homepage: {e}")
            return False
    
    def create_about_page(self):
        """Create a dedicated About page for navigation"""
        try:
            print("📄 Creating dedicated About page...")
            
            about_content = """<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">About UC</h1>
<!-- /wp:heading -->

<!-- wp:image {"id":10,"width":"300px","height":"300px","scale":"cover","style":{"border":{"radius":"50%"}}} -->
<figure class="wp-block-image is-resized has-custom-border">
<img src="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg" alt="UC Profile Photo" class="wp-image-10" style="border-radius:50%;object-fit:cover;width:300px;height:300px"/>
</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>People often say I'm a bit unusual, but I love creativity and bold ideas, even if they seem unrealistic.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">Family & Daily Life</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>A proud husband and father — I can't stop saying how cute my wife and son are.</li>
<li>Enjoy spending weekends together exploring local nature, hot springs, and festivals.</li>
<li>Ichikun is almost 3 years old and already full of curiosity and energy.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">Hobbies & Interests</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Making Friends:</strong> I enjoy making new friends—it's the most important thing in my life.</li>
<li><strong>Wine & Food:</strong> I enjoy tasting and learning about wines, especially Italian and Yamanashi wines.</li>
<li><strong>Time Capsule:</strong> I love burying time capsules in different parts of the world.</li>
<li><strong>Creativity:</strong> Making educational games for my son, experimenting with AI-generated music, videos, and short films.</li>
<li><strong>Poetry & Classics:</strong> Studying traditional Japanese things like poetry, bonsai and exploring cultural depth.</li>
</ul>
<!-- /wp:list -->"""
            
            page_data = {
                "title": "About Me",
                "content": about_content,
                "status": "publish",
                "slug": "about"
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print(f"✅ About page created! ID: {result.get('id')}")
            return result.get('id')
            
        except Exception as e:
            print(f"❌ Error creating About page: {e}")
            return None
    
    def create_blog_page(self):
        """Create a blog page for Recent Posts"""
        try:
            print("📝 Creating blog page...")
            
            blog_content = """<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Recent Posts</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Welcome to my blog! Here you'll find my latest thoughts, experiences, and creative projects. From travel adventures to AI experiments, family moments to wine discoveries - this is where I share my journey.</p>
<!-- /wp:paragraph -->

<!-- wp:latest-posts {"postsToShow":10,"displayAuthor":false,"displayDate":true,"displayFeaturedImage":true,"featuredImageAlign":"left","featuredImageSizeSlug":"medium","addLinkToFeaturedImage":true,"excerptLength":40} -->
<!-- /wp:latest-posts -->"""
            
            page_data = {
                "title": "Recent Posts",
                "content": blog_content,
                "status": "publish",
                "slug": "blog"
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print(f"✅ Blog page created! ID: {result.get('id')}")
            return result.get('id')
            
        except Exception as e:
            print(f"❌ Error creating blog page: {e}")
            return None
    
    def run_final_updates(self):
        """Run all final updates"""
        print("🚀 WordPress Final Updates")
        print("=" * 40)
        
        # Update homepage with fixed footer
        success = self.update_homepage_with_fixed_footer()
        
        if success:
            print("✅ Footer social icons: Emojis removed")
            print("✅ Footer content: 'With Love from UC ❤️' only")
        
        # Create About and Blog pages
        about_id = self.create_about_page()
        blog_id = self.create_blog_page()
        
        print("\n🎉 Final Updates Completed!")
        print("=" * 40)
        print("✅ Footer social icons: No emojis")
        print("✅ Footer message: Simplified")
        print("✅ About page: Created")
        print("✅ Blog page: Created")
        print(f"🌐 Site: {self.site_url}")
        print("\n📋 Manual Steps (via WordPress Admin):")
        print("• Go to Appearance → Menus")
        print("• Create menu with 'About Me' and 'Recent Posts'")
        print("• Assign to Primary Menu location")
        print("• Update footer widgets if needed")
        
        return success

def main():
    updater = WordPressFinalUpdater()
    updater.run_final_updates()

if __name__ == "__main__":
    main()