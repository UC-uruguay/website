#!/usr/bin/env python3
"""
Remove photo from hero section and update text colors
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔄 Updating hero section - removing photo and changing text colors...")

# New hero section without photo and with dark text
new_hero_section = '''<!-- wp:group {"style":{"spacing":{"padding":{"top":"80px","bottom":"80px","left":"20px","right":"20px"}},"color":{"background":"#f8f9fa"}}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:80px;padding-bottom:80px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"clamp(2.5rem, 5vw, 4rem)","fontWeight":"700"},"color":{"text":"#2c3e50"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(2.5rem, 5vw, 4rem);font-weight:700">Hi, I'm UC! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"clamp(1.1rem, 2.5vw, 1.4rem)","lineHeight":"1.6"},"color":{"text":"#34495e"},"spacing":{"margin":{"top":"20px"}}}} -->
<p class="has-text-align-center" style="color:#34495e;margin-top:20px;font-size:clamp(1.1rem, 2.5vw, 1.4rem);line-height:1.6">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->'''

try:
    # Get current content
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        current_page = json.loads(response.read().decode('utf-8'))
    
    current_content = current_page.get('content', {}).get('raw', '')
    
    # Replace the hero section (everything before the first about-me-section)
    if 'about-me-section' in current_content:
        # Find where the about section starts
        about_section_start = current_content.find('<!-- wp:group {"style":{"spacing":{"padding":{"top":"60px","bottom":"60px","left":"20px","right":"20px"}},"color":{"background":"#fafafa"}},"className":"about-me-section"')
        
        if about_section_start != -1:
            # Keep everything from the about section onwards
            remaining_content = current_content[about_section_start:]
            
            # Combine new hero with existing content
            updated_content = new_hero_section + '\n\n' + remaining_content
        else:
            # Fallback - just replace the first cover block
            updated_content = current_content.replace(
                current_content.split('<!-- /wp:cover -->')[0] + '<!-- /wp:cover -->',
                new_hero_section
            )
    else:
        # Fallback approach
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
    print("📸 Photo removed from hero section")
    print("🎨 Text colors changed to dark (#2c3e50 and #34495e)")
    print("🎨 Background changed to light gray (#f8f9fa)")
    print(f"🔗 Site URL: {result.get('link', 'https://uc.x0.com/')}")
    
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Error details: {error_body}")
    print("\n📋 Manual steps to remove hero photo:")
    print("1. WordPress Admin → Pages → Edit homepage")
    print("2. In the hero section, remove the cover block with your photo")
    print("3. Replace with a simple group block with light background")
    print("4. Change text colors to dark colors like #2c3e50")
    print("5. Save the page")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n📋 Manual steps to remove hero photo:")
    print("1. WordPress Admin → Pages → Edit homepage")
    print("2. In the hero section, remove the cover block with your photo") 
    print("3. Replace with a simple group block with light background")
    print("4. Change text colors to dark colors like #2c3e50")
    print("5. Save the page")