#!/usr/bin/env python3
"""
Simple Hero Section Fix - restore the correct hero section
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

print("🎯 Fixing hero section...")

# Get current content
request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{homepage_id}")
request.add_header('Authorization', f'Basic {token}')

with urllib.request.urlopen(request) as response:
    current_page = json.loads(response.read().decode('utf-8'))

current_content = current_page['content']['rendered']

# The correct hero section
correct_hero = f'''<!-- wp:cover {{"url":"{image_url}","id":{media_id},"dimRatio":30,"overlayColor":"black","minHeight":60,"minHeightUnit":"vh","align":"full"}} -->
<div class="wp-block-cover alignfull is-light" style="min-height:60vh">
<span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim-30"></span>
<img class="wp-block-cover__image-background wp-image-{media_id}" alt="" src="{image_url}" data-object-fit="cover"/>
<div class="wp-block-cover__inner-container">
<!-- wp:group -->
<div class="wp-block-group">
<!-- wp:heading {{"textAlign":"center","level":1,"style":{{"typography":{{"fontSize":"3.5rem","fontWeight":"700"}}}},"textColor":"base"}} -->
<h1 class="wp-block-heading has-text-align-center has-base-color" style="font-size:3.5rem;font-weight:700">Hi, I'm UC! 👋</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"align":"center","style":{{"typography":{{"fontSize":"1.3rem"}}}},"textColor":"base"}} -->
<p class="has-text-align-center has-base-color" style="font-size:1.3rem">Welcome to my world! I'm a creative soul from Yamanashi, Japan, passionate about connecting with people, exploring cultures, and creating meaningful experiences.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div></div>
<!-- /wp:cover -->'''

# Find the first cover block (hero section) and replace it
import re

# Find the pattern of the hero section and replace it
hero_pattern = r'<!-- wp:cover.*?<!-- /wp:cover -->'
if re.search(hero_pattern, current_content, re.DOTALL):
    fixed_content = re.sub(hero_pattern, correct_hero, current_content, count=1, flags=re.DOTALL)
else:
    # If pattern not found, replace from start until first group after cover
    about_me_start = current_content.find('<!-- wp:group')
    if about_me_start != -1:
        fixed_content = correct_hero + '\n\n' + current_content[about_me_start:]
    else:
        fixed_content = correct_hero + '\n\n' + current_content

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

print("✅ Hero section fixed!")
print(f"🌐 Updated site: {result['link']}")
print("🎯 Hero section now shows: 'Hi, I'm UC! 👋' with background image")