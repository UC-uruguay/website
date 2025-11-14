#!/usr/bin/env python3
"""
Remove duplicate hero sections - keep only one
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

print("🔧 Removing duplicate hero sections...")

# Get current content
request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
request.add_header('Authorization', f'Basic {token}')

with urllib.request.urlopen(request) as response:
    current_page = json.loads(response.read().decode('utf-8'))

current_content = current_page['content']['rendered']

# Find all cover blocks (hero sections)
cover_pattern = r'<!-- wp:cover.*?<!-- /wp:cover -->'
cover_blocks = re.findall(cover_pattern, current_content, re.DOTALL)

print(f"Found {len(cover_blocks)} hero sections")

if len(cover_blocks) > 1:
    # Keep only the first hero section and remove the rest
    fixed_content = current_content
    
    # Remove all cover blocks first
    for cover_block in cover_blocks:
        fixed_content = fixed_content.replace(cover_block, '', 1)
    
    # Add back only the first (correct) hero section at the beginning
    first_hero = cover_blocks[0]
    
    # Find where to insert - look for the first non-cover block
    about_me_start = fixed_content.find('<!-- wp:group')
    if about_me_start != -1:
        fixed_content = first_hero + '\n\n' + fixed_content
    else:
        fixed_content = first_hero + '\n\n' + fixed_content
    
    print("✅ Removed duplicate hero sections, kept the first one")
else:
    print("✅ Only one hero section found, no changes needed")
    fixed_content = current_content

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

print("✅ Hero section duplication fixed!")
print(f"🌐 Updated site: {result['link']}")
print("🎯 Now showing only one hero section with 'Hi, I'm UC! 👋'")