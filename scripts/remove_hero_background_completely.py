#!/usr/bin/env python3
"""
Completely remove background image from hero section and replace with solid color
"""
import urllib.request
import json
import re

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔄 Completely removing hero background image and changing text colors...")

try:
    # Get current content
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        current_page = json.loads(response.read().decode('utf-8'))
    
    current_content = current_page.get('content', {}).get('raw', '')
    print("📄 Got current content, processing...")
    
    # Create new hero section with NO background image, only solid background color
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
    
    # Find and replace the cover block (which contains the background image)
    # Look for the wp:cover block pattern
    cover_pattern = r'<!-- wp:cover.*?<!-- /wp:cover -->'
    
    if re.search(cover_pattern, current_content, re.DOTALL):
        print("📸 Found cover block with background image, replacing...")
        updated_content = re.sub(cover_pattern, new_hero_section, current_content, flags=re.DOTALL)
        print("✅ Cover block replaced with solid background group")
    else:
        print("❓ Cover block not found, trying alternative approach...")
        # Alternative: look for the first div with alignfull and replace it
        if 'alignfull' in current_content:
            # Find the first alignfull block and replace it
            lines = current_content.split('\n')
            new_lines = []
            in_hero_section = False
            hero_replaced = False
            div_count = 0
            
            for line in lines:
                if not hero_replaced and 'alignfull' in line and 'wp-block-cover' in line:
                    in_hero_section = True
                    new_lines.append(new_hero_section)
                    continue
                elif in_hero_section and '</div>' in line:
                    div_count += 1
                    if div_count >= 2:  # End of cover block
                        in_hero_section = False
                        hero_replaced = True
                    continue
                elif not in_hero_section:
                    new_lines.append(line)
            
            updated_content = '\n'.join(new_lines)
        else:
            # Fallback: prepend new hero section
            updated_content = new_hero_section + '\n\n' + current_content
    
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
    
    print("✅ Hero section updated successfully!")
    print("📸 Background image completely removed")
    print("🎨 Solid light gray background (#f8f9fa) applied")
    print("✨ Text colors changed to dark (#2c3e50 and #34495e)")
    print(f"🔗 Updated site: {result.get('link', 'https://uc.x0.com/')}")
    
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Error details: {error_body}")
    
    print("\n📋 Manual WordPress Editor Steps:")
    print("1. WordPress Admin → Pages → Edit Homepage")
    print("2. Click on the hero section (the big 'Hi, I'm UC!' area)")
    print("3. In the block settings (right sidebar), look for 'Background'")
    print("4. Remove the background image by clicking 'Remove image'")
    print("5. Change background color to light gray (#f8f9fa)")
    print("6. Select the heading text and change color to dark gray (#2c3e50)")
    print("7. Select the paragraph text and change color to medium gray (#34495e)")
    print("8. Save the page")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n📋 Manual WordPress Editor Steps:")
    print("1. WordPress Admin → Pages → Edit Homepage")
    print("2. Click on the hero section (the big 'Hi, I'm UC!' area)")
    print("3. In the block settings (right sidebar), look for 'Background'")
    print("4. Remove the background image by clicking 'Remove image'")
    print("5. Change background color to light gray (#f8f9fa)")
    print("6. Select the heading text and change color to dark gray (#2c3e50)")
    print("7. Select the paragraph text and change color to medium gray (#34495e)")
    print("8. Save the page")