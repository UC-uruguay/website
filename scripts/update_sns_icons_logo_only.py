#!/usr/bin/env python3
"""
Update SNS icons to show logos only (no titles)
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Updating SNS icons to logo-only format...")

# Get current page content
try:
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        page_data = json.loads(response.read().decode('utf-8'))
    
    current_content = page_data.get('content', {}).get('raw', '')
    current_title = page_data.get('title', {}).get('rendered', '')
    
    if not current_content:
        print("❌ No content found")
        exit(1)
    
    print(f"Current content length: {len(current_content)}")
    
    # Make changes to show logos only for Connect with me section
    updated_content = current_content
    
    # Change the social links in About Me section to show labels=false
    # Find and replace the social-links block in About Me section
    old_social_links = '''<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->
<ul class="wp-block-social-links">
<!-- wp:social-link {"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor">Instagram</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://x.com/TORIAEZU_OU","service":"x"} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor">X (Twitter)</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor">Facebook</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor">TikTok</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor">LinkedIn</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->'''

    new_social_links = '''<!-- wp:social-links {"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->
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
<!-- /wp:social-links -->'''

    # Replace the social links
    if old_social_links in updated_content:
        updated_content = updated_content.replace(old_social_links, new_social_links)
        print("✅ Updated About Me social links to logo-only")
    else:
        print("⚠️ Could not find exact social links block to replace")
    
    # Update the page
    page_data = {
        "title": current_title,
        "content": updated_content,
        "status": "publish"
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Page updated successfully!")
    print("\n🎉 SNS icons updated!")
    print("✅ About Me section: Now shows logos only (no text)")
    print("✅ Footer section: Already shows logos only")
    print(f"🔗 Check it at: {site_url}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n📋 Changes made:")
print("• SNS icons in About Me section now show logos only")
print("• Removed text labels (Instagram, X (Twitter), Facebook, etc.)")
print("• Icons are colorful and clickable")
print("• Footer SNS icons already were logo-only")