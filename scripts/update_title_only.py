#!/usr/bin/env python3
"""
Update homepage title to remove 'Creative Soul from Japan'
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11

print("🔄 Updating homepage title to 'UC'...")

# Update only the title
page_data = {
    "title": "UC"
}

data = json.dumps(page_data).encode('utf-8')
request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
request.add_header('Authorization', f'Basic {token}')
request.add_header('Content-Type', 'application/json; charset=utf-8')
request.get_method = lambda: 'POST'

try:
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode('utf-8'))
    
    print("✅ Homepage title updated successfully!")
    print(f"🌐 New title: {result.get('title', {}).get('rendered', 'UC')}")
    print(f"🌐 Site URL: {result.get('link', 'https://uc.x0.com/')}")
    
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"❌ HTTP Error {e.code}: {e.reason}")
    print(f"Error details: {error_body}")
except Exception as e:
    print(f"❌ Error updating title: {e}")