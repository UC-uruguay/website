#!/usr/bin/env python3
"""
Fix homepage - change title to 'UC' and add language support info
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔄 Fixing homepage title and adding language support info...")

# Get current content first
try:
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        current_page = json.loads(response.read().decode('utf-8'))
    
    current_content = current_page.get('content', {}).get('raw', '')
    
    print(f"📄 Current title: {current_page.get('title', {}).get('rendered', 'Unknown')}")
    
    # Update both title and add language support note at the end
    language_note = '''

<!-- wp:group {"style":{"spacing":{"padding":{"top":"20px","bottom":"20px","left":"20px","right":"20px"}},"color":{"background":"#e8f4f8"}}} -->
<div class="wp-block-group has-background" style="background-color:#e8f4f8;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px">
<!-- wp:heading {"textAlign":"center","level":3,"style":{"typography":{"fontSize":"1.2rem","fontWeight":"600"},"color":{"text":"#2c3e50"}}} -->
<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:1.2rem;font-weight:600">🌐 Language Support</h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"0.95rem"},"color":{"text":"#666666"}}} -->
<p class="has-text-align-center" style="color:#666666;font-size:0.95rem">This site supports both Japanese and English. Multilingual features are being enhanced for better accessibility.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->'''
    
    # Add language note if not already present
    updated_content = current_content
    if "Language Support" not in current_content:
        updated_content = current_content + language_note
    
    # Update the page with new title and content
    page_data = {
        "title": "UC",
        "content": updated_content
    }
    
    data = json.dumps(page_data).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Homepage updated successfully!")
    print(f"🎯 New title: {result.get('title', {}).get('rendered', 'UC')}")
    print("🌐 Added language support information")
    print(f"🔗 Site URL: {result.get('link', 'https://uc.x0.com/')}")
    
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Error details: {error_body}")
except Exception as e:
    print(f"❌ Error: {e}")

# Provide manual instructions as fallback
print("\n📋 If automated update failed, manual steps:")
print("1. Go to WordPress Admin → Pages → All Pages")
print("2. Edit the homepage (ID: 11)")  
print("3. Change title from 'UC - Creative Soul from Japan' to 'UC'")
print("4. Save the page")
print("5. Go to Settings → General and update 'Site Title' to 'UC'")
print("\n🌐 For multilingual support:")
print("1. Install Polylang plugin")
print("2. Add Japanese and English languages")
print("3. Create language-specific versions of content")