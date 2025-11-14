#!/usr/bin/env python3
"""
Fix hero section with new authentication - remove background image and fix colors
"""
import urllib.request
import json
import base64

# New authentication
username = "uc-japan"
app_password = "jcps84OkAVZoW7NQdLcQSimC"
site_url = "https://uc.x0.com"
homepage_id = 11

# Create base64 token
credentials = f"{username}:{app_password}"
base64_token = base64.b64encode(credentials.encode()).decode()

print("🔄 Fixing hero section with new authentication...")
print(f"🔐 Using credentials: {username}")

try:
    # Get current content
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
    request.add_header('Authorization', f'Basic {base64_token}')
    
    with urllib.request.urlopen(request) as response:
        current_page = json.loads(response.read().decode('utf-8'))
    
    current_content = current_page.get('content', {}).get('raw', '')
    print("📄 Successfully retrieved current page content")
    
    # Create new hero section without background image
    new_hero_section = '''<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"80px","bottom":"80px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
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
<!-- /wp:group -->'''
    
    # Replace the cover block (background image section)
    import re
    
    # Look for cover block pattern
    cover_pattern = r'<!-- wp:cover.*?<!-- /wp:cover -->'
    match = re.search(cover_pattern, current_content, re.DOTALL)
    
    if match:
        print("📸 Found cover block with background image")
        updated_content = re.sub(cover_pattern, new_hero_section, current_content, flags=re.DOTALL)
        print("✅ Replaced cover block with solid background group")
    else:
        print("❓ Cover block not found, checking for other patterns...")
        # Look for alignfull pattern
        if 'alignfull' in current_content and 'wp-block-cover' in current_content:
            # Split content and replace first alignfull block
            parts = current_content.split('<!-- wp:group', 1)
            if len(parts) > 1:
                # Find the end of the first group block
                remaining = parts[1]
                group_count = 1
                pos = 0
                while group_count > 0 and pos < len(remaining):
                    if remaining[pos:].startswith('<!-- wp:group'):
                        group_count += 1
                        pos += 13
                    elif remaining[pos:].startswith('<!-- /wp:group -->'):
                        group_count -= 1
                        if group_count == 0:
                            pos += 18
                            break
                        pos += 18
                    else:
                        pos += 1
                
                if group_count == 0:
                    updated_content = new_hero_section + '\n\n<!-- wp:group' + remaining[pos:]
                    print("✅ Replaced first group block")
                else:
                    updated_content = new_hero_section + '\n\n' + current_content
                    print("⚠️ Prepended new hero section")
            else:
                updated_content = new_hero_section + '\n\n' + current_content
                print("⚠️ Prepended new hero section")
        else:
            updated_content = new_hero_section + '\n\n' + current_content
            print("⚠️ Prepended new hero section")
    
    # Update the page
    page_data = {
        "content": updated_content
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
    request.add_header('Authorization', f'Basic {base64_token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("🎉 Hero section updated successfully!")
    print("📸 Background image removed")
    print("🎨 Background color: Light gray (#f8f9fa)")
    print("✨ Text colors: Dark gray (#2c3e50, #34495e)")
    print(f"🔗 Updated site: {result.get('link', 'https://uc.x0.com/')}")
    
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Error details: {error_body}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()