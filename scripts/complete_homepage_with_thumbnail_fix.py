#!/usr/bin/env python3
"""
Complete homepage with thumbnail overflow fix included
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Creating complete homepage with thumbnail fixes...")

# Complete homepage content with CSS fixes for thumbnails
complete_content = '''<!-- wp:html -->
<style>
/* Fix Recent Posts thumbnail overflow */
.wp-block-latest-posts__featured-image img {
    width: 100% !important;
    height: auto !important;
    max-width: 100% !important;
    object-fit: cover !important;
    border-radius: 8px !important;
}

.wp-block-latest-posts__featured-image {
    overflow: hidden !important;
    border-radius: 8px !important;
    max-width: 150px !important;
    max-height: 120px !important;
    flex-shrink: 0 !important;
}

.wp-block-latest-posts li {
    overflow: hidden !important;
    margin-bottom: 20px !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 15px !important;
}

.wp-block-latest-posts__post-title {
    flex: 1 !important;
    margin: 0 !important;
    line-height: 1.4 !important;
}

.wp-block-latest-posts__post-excerpt {
    margin-top: 8px !important;
    color: #666 !important;
    line-height: 1.5 !important;
}

.wp-block-latest-posts__post-date {
    font-size: 0.9rem !important;
    color: #999 !important;
    margin-top: 5px !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .wp-block-latest-posts__featured-image {
        max-width: 120px !important;
        max-height: 100px !important;
    }
    
    .wp-block-latest-posts li {
        gap: 12px !important;
    }
}
</style>
<!-- /wp:html -->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"80px","bottom":"80px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}},"className":"hero-section"} -->
<div class="wp-block-group alignfull hero-section has-background" style="background-color:#f8f9fa;padding-top:80px;padding-bottom:80px;padding-left:20px;padding-right:20px">
<!-- wp:group -->
<div class="wp-block-group">
<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"clamp(2.5rem, 5vw, 4rem)","fontWeight":"700"},"color":{"text":"#2c3e50"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(2.5rem, 5vw, 4rem);font-weight:700">Hi, I'm UC! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(1.1rem, 2.5vw, 1.4rem)","lineHeight":"1.6"},"color":{"text":"#34495e"},"spacing":{"margin":{"top":"20px"}}}} -->
<p class="has-text-align-center" style="color:#34495e;margin-top:20px;font-size:clamp(1.1rem, 2.5vw, 1.4rem);line-height:1.6">Creative soul from Yamanashi, Japan. I love making friends, exploring cultures, and creating meaningful connections worldwide! 🌍</p>
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
<ul class="wp-block-social-links is-style-logos-only">
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
<!-- wp:heading {"level":2,"style":{"typography":{"fontWeight":"600","fontSize":"clamp(1.8rem, 4vw, 2.2rem)"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">About Me</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"clamp(1rem, 2.5vw, 1.1rem)","lineHeight":"1.7"}}} -->
<p style="font-size:clamp(1rem, 2.5vw, 1.1rem);line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi with my wonderful wife <strong>Haruhi</strong> and our son <strong>Ichiyu</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"style":{"typography":{"fontWeight":"600","fontSize":"clamp(1.1rem, 3vw, 1.3rem)"},"color":{"text":"#34495e"}}} -->
<h3 class="wp-block-heading" style="color:#34495e;font-size:clamp(1.1rem, 3vw, 1.3rem);font-weight:600">🌟 What Makes Me Happy</h3>
<!-- /wp:heading -->

<!-- wp:list {"style":{"typography":{"fontSize":"clamp(0.9rem, 2vw, 1rem)","lineHeight":"1.6"}}} -->
<ul style="font-size:clamp(0.9rem, 2vw, 1rem);line-height:1.6">
<li><strong>Making friends</strong> worldwide 🌍</li>
<li><strong>Family time</strong> with Haruhi and Ichiyu ❤️</li>
<li><strong>Wine adventures</strong> especially Italian & Yamanashi 🍷</li>
<li><strong>Creative projects</strong> with AI and unique ideas 🎨</li>
<li><strong>Temple visits</strong> and cultural exploration 🛕</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"clamp(0.85rem, 2vw, 0.95rem)","fontStyle":"italic"},"color":{"text":"#7f8c8d"}}} -->
<p style="color:#7f8c8d;font-size:clamp(0.85rem, 2vw, 0.95rem);font-style:italic">"I believe in connecting through vision and empathy, creating worldwide understanding beyond boundaries!"</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f0f2f5"}},"className":"recent-posts-section"} -->
<div class="wp-block-group recent-posts-section has-background" style="background-color:#f0f2f5;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":2,"style":{"typography":{"fontWeight":"600","fontSize":"clamp(1.8rem, 4vw, 2.2rem)"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">📝 Recent Posts</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(0.95rem, 2vw, 1.1rem)"},"color":{"text":"#666666"},"spacing":{"margin":{"bottom":"40px"}}}} -->
<p class="has-text-align-center" style="color:#666666;margin-bottom:40px;font-size:clamp(0.95rem, 2vw, 1.1rem)">Latest thoughts, experiences, and creative adventures</p>
<!-- /wp:paragraph -->

<!-- wp:latest-posts {"postsToShow":3,"displayAuthor":false,"displayDate":true,"displayFeaturedImage":true,"featuredImageAlign":"left","featuredImageSizeSlug":"medium","addLinkToFeaturedImage":true,"excerptLength":20} -->
<!-- /wp:latest-posts -->

<!-- wp:paragraph {"align":"center","style":{"spacing":{"margin":{"top":"30px"}}}} -->
<p class="has-text-align-center" style="margin-top:30px"><a href="/blog" class="wp-element-button">View All Posts →</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":2,"style":{"typography":{"fontWeight":"600","fontSize":"clamp(1.8rem, 4vw, 2.2rem)"},"color":{"text":"#2c3e50"}}} -->
<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">🎨 My World</h2>
<!-- /wp:heading -->

<!-- wp:columns {"style":{"spacing":{"margin":{"top":"30px"}}}} -->
<div class="wp-block-columns" style="margin-top:30px">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"2.5rem"}}} -->
<p class="has-text-align-center" style="font-size:2.5rem">📸</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600","fontSize":"clamp(0.9rem, 2vw, 1rem)"}}} -->
<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600">Family Moments</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"2.5rem"}}} -->
<p class="has-text-align-center" style="font-size:2.5rem">🍇</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600","fontSize":"clamp(0.9rem, 2vw, 1rem)"}}} -->
<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600">Wine Tasting</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"2.5rem"}}} -->
<p class="has-text-align-center" style="font-size:2.5rem">🛕</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600","fontSize":"clamp(0.9rem, 2vw, 1rem)"}}} -->
<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600">Temple Visits</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"2.5rem"}}} -->
<p class="has-text-align-center" style="font-size:2.5rem">🎨</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontWeight":"600","fontSize":"clamp(0.9rem, 2vw, 1rem)"}}} -->
<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="/creative-projects/">Creative Projects</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#2c3e50"}},"className":"footer-cta"} -->
<div class="wp-block-group footer-cta has-background" style="background-color:#2c3e50;padding-top:40px;padding-bottom:60px;padding-left:20px;padding-right:20px">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(1.1rem, 2.5vw, 1.3rem)","lineHeight":"1.6","fontStyle":"italic"}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:clamp(1.1rem, 2.5vw, 1.3rem);line-height:1.6;font-style:italic">"Let's create worldwide understanding and build meaningful friendships together!" 🤝</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(0.9rem, 2vw, 1rem)","fontWeight":"600"},"spacing":{"margin":{"top":"10px"}}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600;margin-top:10px">— UC from Yamanashi 🗾</p>
<!-- /wp:paragraph -->

<!-- wp:social-links {"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"center"},"style":{"spacing":{"margin":{"top":"25px"}}}} -->
<ul class="wp-block-social-links is-style-logos-only" style="margin-top:25px">
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

<!-- wp:separator {"style":{"spacing":{"margin":{"top":"35px","bottom":"20px"}},"color":{"background":"#ffffff33"}}} -->
<hr class="wp-block-separator has-text-color has-alpha-channel-opacity" style="margin-top:35px;margin-bottom:20px;background-color:#ffffff33;color:#ffffff33"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(1rem, 2vw, 1.1rem)","fontWeight":"500"}},"textColor":"base"} -->
<p class="has-text-align-center has-base-color" style="font-size:clamp(1rem, 2vw, 1.1rem);font-weight:500">With Love from UC ❤️</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->'''

try:
    # Update the page with thumbnail fixes included
    page_data = {
        "content": complete_content,
        "status": "publish"
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("\n🎉 Complete homepage with thumbnail fixes deployed!")
    print("✅ Fixed Recent Posts thumbnail overflow")
    print("✅ Proper image dimensions and object-fit")
    print("✅ Improved layout and spacing")
    print("✅ Mobile responsive design")
    print("✅ All previous content maintained")
    print(f"🔗 Check it at: {site_url}")
    
except Exception as e:
    print(f"❌ Error updating page: {e}")
    import traceback
    traceback.print_exc()

print(f"\n📋 Thumbnail fixes applied:")
print("• Max size: 150px wide × 120px tall (desktop)")
print("• Mobile: 120px wide × 100px tall")
print("• Object-fit: Cover (maintains aspect ratio)")
print("• Border radius: 8px for modern appearance")
print("• Proper flex layout with 15px gaps")
print("• Overflow: Hidden to prevent image spillout")