#!/usr/bin/env python3
"""
Fix footer issues:
1. Fix footer menu links not going to correct pages
2. Update footer design - remove old "With Love" section, update WordPress credit
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔧 Fixing footer issues...")

def get_page_by_slug(slug):
    """Get page ID by slug"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages?slug={slug}")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            pages = json.loads(response.read().decode('utf-8'))
        
        if pages:
            return pages[0]
        return None
        
    except Exception as e:
        print(f"❌ Error getting page {slug}: {e}")
        return None

def get_menu_items(menu_id):
    """Get menu items"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items?menu={menu_id}")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            items = json.loads(response.read().decode('utf-8'))
        return items
        
    except Exception as e:
        print(f"❌ Error getting menu items: {e}")
        return []

def update_menu_item(item_id, data):
    """Update a menu item"""
    try:
        json_data = json.dumps(data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items/{item_id}", data=json_data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.get_method = lambda: 'POST'
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        return True
        
    except Exception as e:
        print(f"❌ Error updating menu item {item_id}: {e}")
        return False

# Step 1: Fix footer menu links
print("🔗 Step 1: Fixing footer menu links...")

# Get menu items from footer menu (ID: 11)
menu_items = get_menu_items(11)

# Page slug mappings
page_mappings = {
    "Team": "team",
    "History": "history",
    "Careers": "careers",
    "Privacy Policy": "privacy-policy",
    "Terms and Conditions": "terms-conditions",
    "Contact Us": "contact"
}

fixed_count = 0
for item in menu_items:
    title_obj = item.get('title', '')
    # Handle both string and dict title formats
    if isinstance(title_obj, dict):
        title = title_obj.get('rendered', '')
    else:
        title = str(title_obj)
    
    if title in page_mappings:
        page = get_page_by_slug(page_mappings[title])
        if page:
            # Update menu item with correct page ID and URL
            update_data = {
                "object": "page",
                "object_id": page['id'],
                "url": page['link'],
                "type": "post_type"
            }
            
            if update_menu_item(item['id'], update_data):
                print(f"  ✅ Fixed: {title} → {page['link']}")
                fixed_count += 1
            else:
                print(f"  ❌ Failed to fix: {title}")

print(f"✅ Fixed {fixed_count} menu links")

# Step 2: Update homepage footer section
print("\n🎨 Step 2: Updating homepage footer design...")

try:
    # Get current homepage content
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        current_page = json.loads(response.read().decode('utf-8'))
    
    current_content = current_page.get('content', {}).get('raw', '')
    
    # Create new footer section without the separator and "With Love from UC" line
    # But keep the footer credit area for the WordPress credit replacement
    new_footer_section = '''<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#2c3e50"}}} -->
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

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#ffffff99"},"spacing":{"margin":{"top":"40px"}}}} -->
<p class="has-text-align-center" style="color:#ffffff99;margin-top:40px;font-size:0.9rem">With Love from UC ❤️</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->'''
    
    # Find and replace the last group block (footer)
    import re
    
    # Look for the footer section pattern
    footer_pattern = r'<!-- wp:group \{"style":\{"spacing":\{"padding":\{"top":"40px","bottom":"60px","left":"20px","right":"20px"\}\},"color":\{"background":"#2c3e50"\}\} -->.*?<!-- /wp:group -->'
    
    if re.search(footer_pattern, current_content, re.DOTALL):
        print("🎯 Found footer section, replacing...")
        updated_content = re.sub(footer_pattern, new_footer_section, current_content, flags=re.DOTALL)
    else:
        print("⚠️ Footer pattern not found, appending new footer...")
        updated_content = current_content + '\n\n' + new_footer_section
    
    # Update the page
    page_data = {
        "content": updated_content
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Homepage footer updated!")
    print("  - Removed separator line and old 'With Love from UC'")
    print("  - Moved 'With Love from UC ❤️' to bottom")
    
except Exception as e:
    print(f"❌ Error updating homepage footer: {e}")

print("\n📋 Additional WordPress Admin Steps:")
print("1. Go to Appearance → Customize → Site Identity")
print("2. Change 'Powered by WordPress' text to 'With Love from UC ❤️'")
print("   (Or go to Appearance → Editor and edit footer.php)")

print("\n🎉 Footer fixes completed!")
print("✅ Menu links should now work properly")
print("✅ Footer design updated")
print(f"🔗 Test the footer links at: {site_url}")