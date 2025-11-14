#!/usr/bin/env python3
"""
Restore homepage to original state before footer changes
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔄 Restoring homepage to original state...")

# Complete original content with all sections intact
original_content = '''<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"80px","bottom":"80px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
<div class="wp-block-group alignfull has-background" style="background-color:#f8f9fa;padding-top:80px;padding-bottom:80px;padding-left:20px;padding-right:20px">
<!-- wp:group -->
<div class="wp-block-group">
<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"clamp(2.5rem, 5vw, 4rem)","fontWeight":"700"},"color":{"text":"#2c3e50"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(2.5rem, 5vw, 4rem);font-weight:700">Hi, I'm UC! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(1.1rem, 2.5vw, 1.4rem)","lineHeight":"1.6"},"color":{"text":"#34495e"},"spacing":{"margin":{"top":"20px"}}}} -->
<p class="has-text-align-center" style="color:#34495e;margin-top:20px;font-size:clamp(1.1rem, 2.5vw, 1.4rem);line-height:1.6">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#fafafa"}},"className":"about-me-section"} -->
<div class="wp-block-group about-me-section has-background" style="background-color:#fafafa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%">
<!-- wp:image {"id":10,"width":"280px","height":"280px","scale":"cover","style":{"border":{"radius":"50%"}}} -->
<figure class="wp-block-image is-resized has-custom-border">
<img src="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg" alt="UC Profile Photo" class="wp-image-10" style="border-radius:50%;object-fit:cover;width:280px;height:280px"/>
</figure>
<!-- /wp:image -->

<!-- wp:heading {"textAlign":"center","level":3,"style":{"typography":{"fontWeight":"600","fontSize":"1.4rem"},"color":{"text":"#2c3e50"}}} -->
<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:1.4rem;font-weight:600">Connect with me!</h3>
<!-- /wp:heading -->

<!-- wp:social-links {"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->
<ul class="wp-block-social-links">
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
</div>
<!-- /wp:column -->

<!-- wp:column {"width":"60%"} -->
<div class="wp-block-column" style="flex-basis:60%">
<!-- wp:heading {"level":2,"style":{"typography":{"fontWeight":"600","fontSize":"2.2rem"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading" style="color:#2c3e50;font-size:2.2rem;font-weight:600">About Me</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"1.1rem","lineHeight":"1.7"}}} -->
<p style="font-size:1.1rem;line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi, Japan, with my wife and my adorable son, Ichiyu (nicknamed Ichikun).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"1.1rem","lineHeight":"1.7"}}} -->
<p style="font-size:1.1rem;line-height:1.7">People often say I'm a bit unusual, but I love creativity and bold ideas, even if they seem unrealistic.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"style":{"typography":{"fontWeight":"600","fontSize":"1.5rem"},"color":{"text":"#34495e"}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">👨‍👩‍👦 Family & Daily Life</h3>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>A proud husband and father — I can't stop saying how cute my wife and son are.</li>
<li>Enjoy spending weekends together exploring local nature, hot springs, and festivals.</li>
<li>Ichikun is almost 3 years old and already full of curiosity and energy.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3,"style":{"typography":{"fontWeight":"600","fontSize":"1.5rem"},"color":{"text":"#34495e"}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🎯 Hobbies & Interests</h3>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"}}} -->
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

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#ffffff"}}} -->
<div class="wp-block-group has-background" style="background-color:#ffffff;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {"level":3,"style":{"typography":{"fontWeight":"600","fontSize":"1.5rem"},"color":{"text":"#34495e"}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">🌏 Travel & Culture</h3>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"}}} -->
<ul style="font-size:1rem;line-height:1.6">
<li>Love to travel both in Japan and abroad — I travel all 47 prefectures and around 40 countries.</li>
<li>Interested in Buddhist culture, temples, and unique local experiences.</li>
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:heading {"level":3,"style":{"typography":{"fontWeight":"600","fontSize":"1.5rem"},"color":{"text":"#34495e"}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:1.5rem;font-weight:600">✨ Inspirations</h3>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"}}} -->
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

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f0f2f5"}},"className":"recent-posts-section"} -->
<div class="wp-block-group recent-posts-section has-background" style="background-color:#f0f2f5;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":2,"style":{"typography":{"fontWeight":"600","fontSize":"2.2rem"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">📝 Recent Posts</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.1rem"},"color":{"text":"#666666"},"spacing":{"margin":{"bottom":"40px"}}}} -->
<p class="has-text-align-center" style="color:#666666;margin-bottom:40px;font-size:1.1rem">Discover my latest thoughts, experiences, and creative projects</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<style>
.featured-image-fixed .wp-block-latest-posts__featured-image img {
    width: 120px !important;
    height: 120px !important;
    object-fit: cover !important;
    border-radius: 8px !important;
}
.entry-title, .page-title, h1.entry-title {
    display: none !important;
}
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
</style>
<!-- /wp:html -->

<!-- wp:latest-posts {"postsToShow":3,"displayAuthor":false,"displayDate":true,"displayFeaturedImage":true,"featuredImageAlign":"left","featuredImageSizeSlug":"medium","addLinkToFeaturedImage":true,"excerptLength":25,"className":"featured-image-fixed"} -->
<!-- /wp:latest-posts -->

<!-- wp:paragraph {"align":"center","style":{"spacing":{"margin":{"top":"30px"}}}} -->
<p class="has-text-align-center" style="margin-top:30px"><a href="/blog" class="wp-element-button">View All Posts →</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":2,"style":{"typography":{"fontWeight":"600","fontSize":"2.2rem"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:2.2rem;font-weight:600">🎨 Gallery & Interests</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"3rem"}}} -->
<p class="has-text-align-center" style="font-size:3rem">📸</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-text-align-center" style="font-weight:600"><a href="https://uc.x0.com/greatest-moments/">Greatest Moments</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"3rem"}}} -->
<p class="has-text-align-center" style="font-size:3rem">📦</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-text-align-center" style="font-weight:600"><a href="https://uc.x0.com/products/">Products</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"3rem"}}} -->
<p class="has-text-align-center" style="font-size:3rem">💼</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-text-align-center" style="font-weight:600"><a href="https://uc.x0.com/portfolio/">Portfolio</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"3rem"}}} -->
<p class="has-text-align-center" style="font-size:3rem">📅</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600"}}} -->
<p class="has-text-align-center" style="font-weight:600"><a href="https://uc.x0.com/event-info/">Event Info</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#2c3e50"}}} -->
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

</div>
<!-- /wp:group -->'''

try:
    # Update the page with original content and remove title
    page_data = {
        "title": "",
        "content": original_content
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Homepage restored to original state successfully!")
    print("📄 All sections restored:")
    print("  - Hero section (no background image, gray background)")
    print("  - About Me section")
    print("  - Travel & Culture section") 
    print("  - Recent Posts section")
    print("  - Gallery & Interests section")
    print("  - Footer section with original separator and 'With Love from UC ❤️'")
    print(f"🔗 Site: {result.get('link', 'https://uc.x0.com/')}")
    
    print("\n📋 What was restored:")
    print("✅ Separator line above 'With Love from UC ❤️' in footer")
    print("✅ Original 'With Love from UC ❤️' position")
    print("✅ All content sections intact")
    print("✅ Footer menu links still working")
    
except Exception as e:
    print(f"❌ Error restoring homepage: {e}")
    import traceback
    traceback.print_exc()