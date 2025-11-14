#!/usr/bin/env python3
"""
WordPress UC Personal Site Builder
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
        content = f"""<!-- wp:cover {{"url":"{image_url}","id":{self.media_id},"dimRatio":30,"overlayColor":"black","isUserOverlayColor":true,"minHeight":60,"minHeightUnit":"vh","contentPosition":"center center","isDark":false,"align":"full","style":{{"spacing":{{"margin":{{"top":"0","bottom":"0"}}}}}}}} -->
<div class="wp-block-cover alignfull is-light" style="margin-top:0;margin-bottom:0;min-height:60vh"><span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-30 has-background-dim"></span><img class="wp-block-cover__image-background wp-image-{self.media_id}" alt="" src="{image_url}" data-object-fit="cover"/><div class="wp-block-cover__inner-container">
<!-- wp:group {{"layout":{{"type":"constrained","contentSize":"800px"}}}} -->
<div class="wp-block-group">
<!-- wp:heading {{"textAlign":"center","level":1,"style":{{"typography":{{"fontSize":"3.5rem","fontWeight":"700","lineHeight":"1.2"}},"elements":{{"link":{{"color":{{"text":"var:preset|color|base"}}}}}}},"textColor":"base"}} -->
<h1 class="wp-block-heading has-text-align-center has-base-color has-text-color has-link-color" style="font-size:3.5rem;font-weight:700;line-height:1.2">Hi, I'm Yūshi! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.3rem","lineHeight":"1.6"}},"elements":{{"link":{{"color":{{"text":"var:preset|color|base"}}}}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color has-text-color has-link-color" style="font-size:1.3rem;line-height:1.6">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div></div>
<!-- /wp:cover -->

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"}}}},"color":{{"background":"#fafafa"}}},"layout":{{"type":"constrained","contentSize":"1200px"}}}} -->
<div class="wp-block-group has-background" style="background-color:#fafafa;padding-top:var(--wp--preset--spacing--x-large);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--x-large);padding-left:var(--wp--preset--spacing--medium)">
<!-- wp:columns {{"verticalAlignment":"top"}} -->
<div class="wp-block-columns are-vertically-aligned-top">
<!-- wp:column {{"verticalAlignment":"top","width":"40%"}} -->
<div class="wp-block-column is-vertically-aligned-top" style="flex-basis:40%">
<!-- wp:image {{"id":{self.media_id},"width":"300px","height":"300px","scale":"cover","sizeSlug":"full","linkDestination":"none","style":{{"border":{{"radius":"50%"}}}}}} -->
<figure class="wp-block-image size-full is-resized has-custom-border"><img src="{image_url}" alt="Yushi Nakashima Profile" class="wp-image-{self.media_id}" style="border-radius:50%;object-fit:cover;width:300px;height:300px"/></figure>
<!-- /wp:image -->

<!-- wp:group {{"style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|medium"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group" style="margin-top:var(--wp--preset--spacing--medium)">
<!-- wp:heading {{"textAlign":"center","level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#2c3e50"}}}}}} -->
<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:1.5rem;font-weight:600">Connect with me!</h3>
<!-- /wp:heading -->

<!-- wp:social-links {{"iconColor":"contrast","iconColorValue":"#000000","openInNewTab":true,"showLabels":true,"className":"is-style-logos-only","layout":{{"type":"flex","justifyContent":"center","flexWrap":"wrap"}}}} -->
<ul class="wp-block-social-links has-icon-color is-style-logos-only">
<!-- wp:social-link {{"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"}} -->
<li class="wp-block-social-link wp-social-link-instagram"><a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M12,4.622c2.403,0,2.688,0.009,3.637,0.052c0.877,0.04,1.354,0.187,1.671,0.31c0.42,0.163,0.72,0.358,1.035,0.673 c0.315,0.315,0.51,0.615,0.673,1.035c0.123,0.317,0.27,0.794,0.31,1.671c0.043,0.949,0.052,1.234,0.052,3.637 s-0.009,2.688-0.052,3.637c-0.04,0.877-0.187,1.354-0.31,1.671c-0.163,0.42-0.358,0.72-0.673,1.035 c-0.315,0.315-0.615,0.51-1.035,0.673c-0.317,0.123-0.794,0.27-1.671,0.31c-0.949,0.043-1.234,0.052-3.637,0.052 s-2.688-0.009-3.637-0.052c-0.877-0.04-1.354-0.187-1.671-0.31c-0.42-0.163-0.72-0.358-1.035-0.673 c-0.315-0.315-0.51-0.615-0.673-1.035c-0.123-0.317-0.27-0.794-0.31-1.671C4.631,14.688,4.622,14.403,4.622,12 s0.009-2.688,0.052-3.637c0.04-0.877,0.187-1.354,0.31-1.671c0.163-0.42,0.358-0.72,0.673-1.035 c0.315-0.315,0.615-0.51,1.035-0.673c0.317-0.123,0.794-0.27,1.671-0.31C9.312,4.631,9.597,4.622,12,4.622 M12,3 C9.556,3,9.249,3.01,8.289,3.054C7.331,3.098,6.677,3.25,6.105,3.472C5.513,3.702,5.011,4.01,4.511,4.511 c-0.5,0.5-0.808,1.002-1.038,1.594C3.25,6.677,3.098,7.331,3.054,8.289C3.01,9.249,3,9.556,3,12c0,2.444,0.01,2.751,0.054,3.711 c0.044,0.958,0.196,1.612,0.418,2.185c0.23,0.592,0.538,1.094,1.038,1.594c0.5,0.5,1.002,0.808,1.594,1.038 c0.572,0.222,1.227,0.375,2.185,0.418C9.249,20.99,9.556,21,12,21s2.751-0.01,3.711-0.054c0.958-0.044,1.612-0.196,2.185-0.418 c0.592-0.23,1.094-0.538,1.594-1.038c0.5-0.5,0.808-1.002,1.038-1.594c0.222-0.572,0.375-1.227,0.418-2.185 C20.99,14.751,21,14.444,21,12s-0.01-2.751-0.054-3.711c-0.044-0.958-0.196-1.612-0.418-2.185c-0.23-0.592-0.538-1.094-1.038-1.594 c-0.5-0.5-1.002-0.808-1.594-1.038c-0.572-0.222-1.227-0.375-2.185-0.418C14.751,3.01,14.444,3,12,3L12,3z M12,7.378 c-2.552,0-4.622,2.069-4.622,4.622S9.448,16.622,12,16.622s4.622-2.069,4.622-4.622S14.552,7.378,12,7.378z M12,15 c-1.657,0-3-1.343-3-3s1.343-3,3-3s3,1.343,3,3S13.657,15,12,15z M16.804,6.116c-0.596,0-1.08,0.484-1.08,1.08 s0.484,1.08,1.08,1.08c0.596,0,1.08-0.484,1.08-1.08S17.401,6.116,16.804,6.116z"></path></svg><span class="wp-block-social-link-label">Instagram</span></a></li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://x.com/TORIAEZU_OU","service":"x"}} -->
<li class="wp-block-social-link wp-social-link-x"><a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M13.982 10.622 20.54 3h-1.554l-5.693 6.618L8.745 3H3.5l6.876 10.007L3.5 21h1.554l6.012-6.989L15.868 21h5.245l-7.131-10.378Zm-2.128 2.474-.697-.997-5.543-7.93H8l4.474 6.4.697.996 5.815 8.318h-2.387l-4.745-6.787Z"></path></svg><span class="wp-block-social-link-label">X</span></a></li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"}} -->
<li class="wp-block-social-link wp-social-link-tiktok"><a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M16.8075 8.2025C17.5125 8.2025 18.1725 8.0175 18.7575 7.695V10.245C18.1725 10.5675 17.5125 10.7525 16.8075 10.7525C15.3225 10.7525 14.1075 9.5375 14.1075 8.0525C14.1075 6.5675 15.3225 5.3525 16.8075 5.3525V7.9025C17.3175 7.9025 17.7675 8.3525 17.7675 8.8625V5.1075H15.2175V8.8625C15.2175 9.3725 15.6675 9.8225 16.1775 9.8225H16.8075V8.2025Z"></path></svg><span class="wp-block-social-link-label">TikTok</span></a></li>
<!-- /wp:social-link -->

<!-- wp:social-link {{"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"}} -->
<li class="wp-block-social-link wp-social-link-linkedin"><a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M19.7,3H4.3C3.582,3,3,3.582,3,4.3v15.4C3,20.418,3.582,21,4.3,21h15.4c0.718,0,1.3-0.582,1.3-1.3V4.3 C21,3.582,20.418,3,19.7,3z M8.339,18.338H5.667v-8.59h2.672V18.338z M7.004,8.574c-0.857,0-1.549-0.694-1.549-1.548 c0-0.855,0.691-1.548,1.549-1.548c0.854,0,1.548,0.693,1.548,1.548C8.551,7.881,7.858,8.574,7.004,8.574z M18.339,18.338h-2.669 v-4.177c0-0.996-0.018-2.277-1.388-2.277c-1.39,0-1.604,1.086-1.604,2.206v4.248h-2.667v-8.59h2.56v1.174h0.037 c0.356-0.675,1.227-1.387,2.524-1.387c2.704,0,3.203,1.778,3.203,4.092L18.339,18.338z"></path></svg><span class="wp-block-social-link-label">LinkedIn</span></a></li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"top","width":"60%"}} -->
<div class="wp-block-column is-vertically-aligned-top" style="flex-basis:60%">
<!-- wp:heading {{"level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|medium"}}}}}}}} -->
<h2 class="wp-block-heading" style="color:#2c3e50;margin-bottom:var(--wp--preset--spacing--medium);font-size:2.2rem;font-weight:600">About Me</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"1.1rem","lineHeight":"1.7"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|medium"}}}}}}}} -->
<p style="margin-bottom:var(--wp--preset--spacing--medium);font-size:1.1rem;line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>Yūshi (ゆーし)</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"1.1rem","lineHeight":"1.7"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|large"}}}}}}}} -->
<p style="margin-bottom:var(--wp--preset--spacing--large);font-size:1.1rem;line-height:1.7">People often say I'm a bit unusual, but I love creativity and bold ideas, even if they seem unrealistic.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}},"spacing":{{"margin":{{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|small"}}}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;margin-top:var(--wp--preset--spacing--large);margin-bottom:var(--wp--preset--spacing--small);font-size:1.5rem;font-weight:600">👨‍👩‍👦 Family & Daily Life</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|medium"}}}}}}}} -->
<ul style="margin-bottom:var(--wp--preset--spacing--medium);font-size:1rem;line-height:1.6">
<li>A proud husband and father — I can't stop saying how cute my wife and son are.</li>
<li>Enjoy spending weekends together exploring local nature, hot springs, and festivals.</li>
<li>Ichikun is almost 3 years old and already full of curiosity and energy.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}},"spacing":{{"margin":{{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|small"}}}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;margin-top:var(--wp--preset--spacing--large);margin-bottom:var(--wp--preset--spacing--small);font-size:1.5rem;font-weight:600">🎯 Hobbies & Interests</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|medium"}}}}}}}} -->
<ul style="margin-bottom:var(--wp--preset--spacing--medium);font-size:1rem;line-height:1.6">
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

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"}}}},"color":{{"background":"#ffffff"}}},"layout":{{"type":"constrained","contentSize":"1200px"}}}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:var(--wp--preset--spacing--x-large);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--x-large);padding-left:var(--wp--preset--spacing--medium)">
<!-- wp:columns {{"verticalAlignment":"top"}} -->
<div class="wp-block-columns are-vertically-aligned-top">
<!-- wp:column {{"verticalAlignment":"top"}} -->
<div class="wp-block-column is-vertically-aligned-top">
<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;margin-bottom:var(--wp--preset--spacing--small);font-size:1.5rem;font-weight:600">🌏 Travel & Culture</h3>
<!-- /wp:heading -->

<!-- wp:list {{"style":{{"typography":{{"fontSize":"1rem","lineHeight":"1.6"}}}}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>Love to travel both in Japan and abroad — I travel all 47 prefectures and around 40 countries.</li>
<li>Interested in Buddhist culture, temples, and unique local experiences.</li>
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"top"}} -->
<div class="wp-block-column is-vertically-aligned-top">
<!-- wp:heading {{"level":3,"style":{{"typography":{{"fontWeight":"600","fontSize":"1.5rem"}},"color":{{"text":"#34495e"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<h3 class="wp-block-heading" style="color:#34495e;margin-bottom:var(--wp--preset--spacing--small);font-size:1.5rem;font-weight:600">✨ Inspirations</h3>
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

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|x-large","bottom":"var:preset|spacing|x-large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"}}}},"color":{{"background":"#f8f9fa"}}},"layout":{{"type":"constrained","contentSize":"1200px"}}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:var(--wp--preset--spacing--x-large);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--x-large);padding-left:var(--wp--preset--spacing--medium)">
<!-- wp:heading {{"textAlign":"center","level":2,"style":{{"typography":{{"fontWeight":"600","fontSize":"2.2rem"}},"color":{{"text":"#2c3e50"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|large"}}}}}}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;margin-bottom:var(--wp--preset--spacing--large);font-size:2.2rem;font-weight:600">📱 Gallery & Interests</h2>
<!-- /wp:heading -->

<!-- wp:columns {{"verticalAlignment":"center"}} -->
<div class="wp-block-columns are-vertically-aligned-center">
<!-- wp:column {{"verticalAlignment":"center"}} -->
<div class="wp-block-column is-vertically-aligned-center">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--small);font-size:3rem">📸</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Family Moments</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"center"}} -->
<div class="wp-block-column is-vertically-aligned-center">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--small);font-size:3rem">🍇</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Wine Tasting</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"center"}} -->
<div class="wp-block-column is-vertically-aligned-center">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--small);font-size:3rem">🛕</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontWeight":"600"}}}}}} -->
<p class="has-text-align-center" style="font-weight:600">Temples & Travel</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column {{"verticalAlignment":"center"}} -->
<div class="wp-block-column is-vertically-aligned-center">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"3rem"}},"spacing":{{"margin":{{"bottom":"var:preset|spacing|small"}}}}}}}} -->
<p class="has-text-align-center" style="margin-bottom:var(--wp--preset--spacing--small);font-size:3rem">🎨</p>
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

<!-- wp:group {{"style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|large","bottom":"var:preset|spacing|large","left":"var:preset|spacing|medium","right":"var:preset|spacing|medium"}}}},"color":{{"background":"#2c3e50"}}},"layout":{{"type":"constrained","contentSize":"800px"}}}} -->
<div class="wp-block-group has-background" style="background-color:#2c3e50;padding-top:var(--wp--preset--spacing--large);padding-right:var(--wp--preset--spacing--medium);padding-bottom:var(--wp--preset--spacing--large);padding-left:var(--wp--preset--spacing--medium)">
<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.2rem","lineHeight":"1.6"}},"elements":{{"link":{{"color":{{"text":"var:preset|color|base"}}}}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color has-text-color has-link-color" style="font-size:1.2rem;line-height:1.6"><em>"I believe in connecting with others through vision and empathy. Let's create a world-wide common understanding beyond religion and build meaningful friendships together!"</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1rem","fontWeight":"600"}},"elements":{{"link":{{"color":{{"text":"var:preset|color|base"}}}}},"spacing":{{"margin":{{"top":"var:preset|spacing|medium"}}}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color has-text-color has-link-color" style="margin-top:var(--wp--preset--spacing--medium);font-size:1rem;font-weight:600">— Yūshi Nakashima</p>
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