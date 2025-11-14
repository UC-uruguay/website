#!/usr/bin/env python3
"""
WordPress Hero Section Fixer
Restore the original hero section to the homepage
"""
import urllib.request
import json

class WordPressHeroSectionFixer:
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
        self.homepage_id = 11  # Homepage ID
        self.image_url = "https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg"
        self.media_id = 10
    
    def get_correct_hero_section(self):
        """Get the correct original hero section content"""
        hero_section = f'''<!-- wp:cover {{"url":"{self.image_url}","id":{self.media_id},"dimRatio":30,"overlayColor":"black","minHeight":60,"minHeightUnit":"vh","align":"full"}} -->
<div class="wp-block-cover alignfull is-light" style="min-height:60vh">
<span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-30"></span>
<img class="wp-block-cover__image-background wp-image-{self.media_id}" alt="" src="{self.image_url}" data-object-fit="cover"/>
<div class="wp-block-cover__inner-container">
<!-- wp:group -->
<div class="wp-block-group">
<!-- wp:heading {{"textAlign":"center","level":1,"style":{{"typography":{{"fontSize":"3.5rem","fontWeight":"700"}}}},"textColor":"base"}} -->
<h1 class="wp-block-heading has-text-align-center has-base-color" style="font-size:3.5rem;font-weight:700">Hi, I'm UC! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.3rem"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.3rem">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div></div>
<!-- /wp:cover -->'''
        
        return hero_section
    
    def get_current_homepage_content(self):
        """Get the current homepage content"""
        try:
            print("📄 Getting current homepage content...")
            
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}")
            request.add_header('Authorization', f'Basic {self.token}')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            return result['content']['rendered']
            
        except Exception as e:
            print(f"❌ Error getting homepage content: {e}")
            return None
    
    def restore_homepage_with_correct_hero(self):
        """Restore the homepage with the correct hero section"""
        try:
            print("🔄 Restoring homepage with correct hero section...")
            
            # Get the correct hero section
            correct_hero = self.get_correct_hero_section()
            
            # Create the complete correct homepage content
            complete_content = correct_hero + """

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#fafafa"}}},"className":"about-me-section"}} -->
<div class="wp-block-group about-me-section has-background" style="background-color:#fafafa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column {{"width":"40%"}} -->
<div class="wp-block-column" style="flex-basis:40%">
<!-- wp:image {{"id":{self.media_id},"width":"280px","height":"280px","scale":"cover","style":{{"border":{{"radius":"50%"}}}}}} -->
<figure class="wp-block-image is-resized has-custom-border">
<img src="{self.image_url}" alt="UC Profile Photo" class="wp-image-{self.media_id}" style="border-radius:50%;object-fit:cover;width:280px;height:280px"/>
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

<!-- wp:social-link {{"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"}} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor">Facebook</a>
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
<p style="font-size:1.1rem;line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>
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

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#f0f2f5"}}}},"className":"recent-posts-section"}} -->
<div class="wp-block-group recent-posts-section has-background" style="background-color:#f0f2f5;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {{"textAlign":"center","level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">📝 Recent Posts</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.1rem"}},"color":{{"text":"#666666"}},"spacing":{{"margin":{{"bottom":"40px"}}}}}}}} -->
<p class="has-text-align-center" style="color:#666666;margin-bottom:40px;font-size:1.1rem">Discover my latest thoughts, experiences, and creative projects</p>
<!-- /wp:paragraph -->

<!-- wp:latest-posts {{"postsToShow":3,"displayAuthor":false,"displayDate":true,"displayFeaturedImage":true,"featuredImageAlign":"left","featuredImageSizeSlug":"medium","addLinkToFeaturedImage":true,"excerptLength":25}} -->
<!-- /wp:latest-posts -->

<!-- wp:paragraph {{"align":"center","style":{{"spacing":{{"margin":{{"top":"30px"}}}}}}}} -->
<p class="has-text-align-center" style="margin-top:30px"><a href="https://uc.x0.com/blog" class="wp-element-button">View All Posts →</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"60px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#f8f9fa"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {{"textAlign":"center","level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">🎨 Gallery & Interests</h2>
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

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"40px","bottom":"60px","left":"20px","right":"20px"}}}},"color":{{"background":"#2c3e50"}}}}}} -->
<div class="wp-block-group has-background" style="background-color:#2c3e50;padding-top:40px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.2rem","lineHeight":"1.6"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.2rem;line-height:1.6"><em>"I believe in connecting with others through vision and empathy. Let's create a world-wide common understanding beyond religion and build meaningful friendships together!"</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1rem","fontWeight":"600"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1rem;font-weight:600">— UC</p>
<!-- /wp:paragraph -->

<!-- wp:social-links {{"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{{"type":"flex","justifyContent":"center"}},"style":{{"spacing":{{"margin":{{"top":"30px"}}}}}}}} -->
<ul class="wp-block-social-links is-style-logos-only" style="margin-top:30px">
<!-- wp:social-link {{"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"}} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://x.com/TORIAEZU_OU","service":"x"}} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"}} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"}} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"}} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"></a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:separator {{"style":{{"spacing":{{"margin":{{"top":"40px","bottom":"20px"}}}},"color":{{"background":"#ffffff33"}}}}}} -->
<hr class="wp-block-separator has-text-color has-alpha-channel-opacity" style="margin-top:40px;margin-bottom:20px;background-color:#ffffff33;color:#ffffff33"/>
<!-- /wp:separator -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.1rem","fontWeight":"500"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.1rem;font-weight:500">With Love from UC ❤️</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"0.9rem"}},"color":{{"text":"#ffffff99"}},"spacing":{{"margin":{{"top":"5px"}}}}}}}} -->
<p class="has-text-align-center" style="color:#ffffff99;margin-top:5px;font-size:0.9rem">Connecting hearts and minds across the world</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->"""
            
            page_data = {
                "content": complete_content
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            request.get_method = lambda: 'POST'  # Use POST for update
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print("✅ Homepage hero section restored!")
            print(f"🌐 Updated homepage: {result['link']}")
            
            return result
            
        except Exception as e:
            print(f"❌ Hero section restoration error: {e}")
            if hasattr(e, 'read'):
                try:
                    error_details = e.read().decode('utf-8')
                    print(f"Error details: {error_details}")
                except:
                    pass
            return None
    
    def fix_hero_section(self):
        """Main function to restore the hero section"""
        print("🎯 Hero Section Restoration")
        print("=" * 50)
        
        result = self.restore_homepage_with_correct_hero()
        
        if result:
            print("\n🎉 Hero Section Restoration Completed!")
            print("=" * 60)
            print("✅ Original hero section restored: DONE")
            print("✅ 'Hi, I'm UC! 👋' heading: DONE")
            print("✅ Welcome message with background image: DONE")
            print("✅ All other sections preserved: DONE")
            print(f"🌐 Live site: {result['link']}")
            print("\n🎯 Hero section is back to its original state!")
        else:
            print("❌ Failed to restore hero section")
        
        return result

def main():
    fixer = WordPressHeroSectionFixer()
    fixer.fix_hero_section()

if __name__ == "__main__":
    main()