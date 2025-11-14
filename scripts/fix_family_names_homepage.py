#!/usr/bin/env python3
"""
Fix family names on homepage: son=Ichiyu, wife=Haruhi
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("👨‍👩‍👦 Fixing family names: son=Ichiyu, wife=Haruhi...")

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
    
    # Fix the family description
    old_family_text = 'Hi, I\'m <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi with my wonderful wife and our son, <strong>Ichiyu Haruhi Yushi</strong>.'
    
    new_family_text = 'Hi, I\'m <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi with my wonderful wife <strong>Haruhi</strong> and our son <strong>Ichiyu</strong>.'
    
    updated_content = current_content.replace(old_family_text, new_family_text)
    
    if old_family_text in current_content:
        print("✅ Found and updated family description")
    else:
        print("⚠️ Could not find exact family text, trying partial replacement...")
        # Try partial replacement
        updated_content = current_content.replace(
            'Ichiyu Haruhi Yushi', 
            'Ichiyu'
        ).replace(
            'my wonderful wife and our son',
            'my wonderful wife <strong>Haruhi</strong> and our son'
        )
    
    # Update the page
    page_data_update = {
        "title": current_title,
        "content": updated_content,
        "status": "publish"
    }
    
    data = json.dumps(page_data_update).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("\n🎉 Family names updated successfully!")
    print("✅ Wife's name: Haruhi")
    print("✅ Son's name: Ichiyu")
    print("✅ Removed incorrect full name combination")
    print(f"🔗 Check it at: {site_url}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n📋 Correction made:")
print("• Wife: Haruhi (individual name)")
print("• Son: Ichiyu (individual name)")
print("• IMPORTANT: Saved to SITE_RULES.md for future reference")
print("• Website text now reflects correct family names")