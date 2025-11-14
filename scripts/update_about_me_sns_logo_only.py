#!/usr/bin/env python3
"""
Update About Me section SNS icons to logo-only (no text labels)
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Updating About Me SNS icons to logo-only...")

# Read the original homepage content from the restore file
with open('/home/uc/restore_original_homepage.py', 'r') as f:
    restore_content = f.read()

# Extract the original_content variable
start_marker = "original_content = '''"
end_marker = "'''"

start_pos = restore_content.find(start_marker) + len(start_marker)
end_pos = restore_content.find(end_marker, start_pos)

if start_pos > len(start_marker) - 1 and end_pos > start_pos:
    original_content = restore_content[start_pos:end_pos]
    print(f"✅ Loaded original content ({len(original_content)} characters)")
    
    # Make the specific change: About Me SNS icons to logo-only
    updated_content = original_content.replace(
        '<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->',
        '<!-- wp:social-links {"openInNewTab":true,"showLabels":false,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} -->'
    )
    
    # Remove text labels from social link anchors in About Me section
    sns_replacements = [
        ('<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor">Instagram</a>', 
         '<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"></a>'),
        ('<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor">X (Twitter)</a>', 
         '<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"></a>'),
        ('<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor">Facebook</a>', 
         '<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor"></a>'),
        ('<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor">TikTok</a>', 
         '<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"></a>'),
        ('<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor">LinkedIn</a>', 
         '<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"></a>')
    ]
    
    # Apply replacements only to the first occurrence (About Me section)
    for old_text, new_text in sns_replacements:
        if old_text in updated_content:
            # Only replace the first occurrence to avoid changing footer SNS
            updated_content = updated_content.replace(old_text, new_text, 1)
            print(f"✅ Updated: {old_text.split('>')[1].split('<')[0]} to logo-only")
    
    # Also change "AI Creative Projects" to "Creative Projects" with link
    updated_content = updated_content.replace(
        '<p class="has-text-align-center" style="font-weight:600">AI Creative Projects</p>',
        '<p class="has-text-align-center" style="font-weight:600"><a href="/creative-projects/">Creative Projects</a></p>'
    )
    
    print(f"✅ Updated AI Creative Projects to Creative Projects with link")
    
    # Update the page
    try:
        page_data = {
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
        
        print("\n🎉 Homepage updated successfully!")
        print("✅ About Me SNS icons now show logos only (no text)")
        print("✅ Footer SNS icons remain logos only")
        print("✅ AI Creative Projects changed to Creative Projects with link")
        print(f"🔗 Check it at: {site_url}")
        
    except Exception as e:
        print(f"❌ Error updating page: {e}")
        import traceback
        traceback.print_exc()

else:
    print("❌ Could not extract original content from restore file")

print(f"\n📋 Changes made:")
print("• About Me section: SNS icons now show logos only")
print("• Instagram, X, Facebook, TikTok, LinkedIn - all logo-only")
print("• Footer section: Already was logo-only (unchanged)")
print("• Gallery: AI Creative Projects → Creative Projects (with link)")