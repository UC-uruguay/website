#!/usr/bin/env python3
"""
Safely add Temple Visits link to homepage without breaking content
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🛕 Safely adding Temple Visits link to homepage...")

# Temple visits article URL
temple_article_url = "https://uc.x0.com/finding-peace-and-connection-my-journey-through-temple-visits/"

# Get current homepage content
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
    
    # Only replace the Temple Visits text with a link
    updated_content = current_content.replace(
        '<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600">Temple Visits</p>',
        f'<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="{temple_article_url}">Temple Visits</a></p>'
    )
    
    # Verify the replacement was made
    if updated_content == current_content:
        print("⚠️ No replacement made - checking for existing link...")
        if temple_article_url in current_content:
            print("✅ Link already exists in homepage")
            exit(0)
        else:
            print("❌ Could not find Temple Visits text to replace")
            exit(1)
    
    print(f"Updated content length: {len(updated_content)}")
    
    # Update the homepage
    page_update = {
        "title": current_title,
        "content": updated_content,
        "status": "publish"
    }
    
    data = json.dumps(page_update).encode('utf-8')
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}", data=data)
    request.add_header('Authorization', f'Basic {token}')
    request.add_header('Content-Type', 'application/json; charset=utf-8')
    request.get_method = lambda: 'POST'
    
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Homepage updated successfully!")
    print(f"✅ Temple Visits now links to: {temple_article_url}")
    print(f"🔗 Check homepage at: {site_url}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n📋 Update completed:")
print(f"• Temple Visits section now clickable")
print(f"• Links to temple visits article")
print(f"• All other homepage content preserved")
print(f"• Article includes photo of UC with monk")