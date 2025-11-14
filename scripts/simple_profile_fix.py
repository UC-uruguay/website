#!/usr/bin/env python3
"""
Simple UC Profile Photo Fix
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
homepage_id = 11
image_url = "https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg"
media_id = 10

print("🔧 Fixing UC profile photo...")

# Get current content
request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
request.add_header('Authorization', f'Basic {token}')

with urllib.request.urlopen(request) as response:
    current_page = json.loads(response.read().decode('utf-8'))

current_content = current_page['content']['rendered']

# Fix the profile photo references
fixed_content = current_content.replace('{self.image_url}', image_url)
fixed_content = fixed_content.replace('{self.media_id}', str(media_id))

# Update the page
page_data = {
    "content": fixed_content
}

data = json.dumps(page_data).encode('utf-8')
request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}", data=data)
request.add_header('Authorization', f'Basic {token}')
request.add_header('Content-Type', 'application/json; charset=utf-8')
request.get_method = lambda: 'POST'

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode('utf-8'))

print("✅ UC profile photo fixed!")
print(f"🌐 Updated site: {result['link']}")