#!/usr/bin/env python3
import requests
import json
import base64
import os
from datetime import datetime

# Load WordPress credentials
with open('wordpress_auth.json', 'r') as f:
    auth_data = json.load(f)

site_url = auth_data['site_url']
username = auth_data['username']
app_password = auth_data['app_password']

# Create authentication header
auth_string = f"{username}:{app_password}"
auth_bytes = auth_string.encode('ascii')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

headers = {
    'Authorization': f'Basic {auth_b64}',
    'Content-Type': 'application/json'
}

def upload_image(image_path):
    """Upload image to WordPress media library"""
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        return None
    
    # Get file info
    filename = os.path.basename(image_path)
    
    # Read image file
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Upload to WordPress media library
    upload_headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Content-Type': 'image/jpeg'
    }
    
    upload_url = f"{site_url}/wp-json/wp/v2/media"
    
    print(f"Uploading image: {filename}")
    response = requests.post(upload_url, headers=upload_headers, data=image_data)
    
    if response.status_code == 201:
        media_data = response.json()
        print(f"Image uploaded successfully. Media ID: {media_data['id']}")
        return media_data
    else:
        print(f"Failed to upload image: {response.status_code}")
        print(response.text)
        return None

def create_post(title, content, featured_image_id=None):
    """Create a new WordPress post"""
    
    post_data = {
        'title': title,
        'content': content,
        'status': 'publish',  # or 'draft' if you want to review first
        'date': datetime.now().isoformat()
    }
    
    if featured_image_id:
        post_data['featured_media'] = featured_image_id
    
    url = f"{site_url}/wp-json/wp/v2/posts"
    
    print("Creating WordPress post...")
    response = requests.post(url, headers=headers, data=json.dumps(post_data))
    
    if response.status_code == 201:
        post_data = response.json()
        print(f"Post created successfully!")
        print(f"Post ID: {post_data['id']}")
        print(f"Post URL: {post_data['link']}")
        return post_data
    else:
        print(f"Failed to create post: {response.status_code}")
        print(response.text)
        return None

# Main execution
if __name__ == "__main__":
    # Image file path
    image_path = "IMG_20250906_005851.jpg"
    
    # Post content
    title = "戸田達昭さんの会"
    content = """昨日は山梨を代表する、戸田達昭さんの会に行ってきた。

戸田さんは性善説で、オファーは断らない。死ぬときに笑っていたいんだと。

カッコイイと思う自分に合わせて生きているので、頑張っちゃうって話を聴いて、ストイックで僕にはできていないけど、僕もそうなりたいと思えた。

帰りはみんなでコンビニカップラーメンで乾杯。学生みたいな終わり方だった。たまにはよい。"""
    
    # Upload image first
    media_data = upload_image(image_path)
    
    if media_data:
        # Create post with featured image
        post_data = create_post(title, content, media_data['id'])
    else:
        # Create post without image
        print("Proceeding without image...")
        post_data = create_post(title, content)
    
    if post_data:
        print("\n✅ WordPress post created successfully!")
        print(f"View your post at: {post_data['link']}")
    else:
        print("\n❌ Failed to create WordPress post")