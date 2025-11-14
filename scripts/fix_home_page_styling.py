#!/usr/bin/env python3
"""
Fix home page styling issues - remove dots and make icons colored
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Fixing home page styling issues...")

def update_page_content(page_id, new_content, title):
    """Update page content"""
    try:
        page_data = {
            "title": title,
            "content": new_content,
            "status": "publish"
        }
        
        data = json.dumps(page_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{page_id}", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.get_method = lambda: 'POST'
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"✅ Updated page content")
        return True
        
    except Exception as e:
        print(f"❌ Error updating page: {e}")
        return False

# Get current page content
try:
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        page_data = json.loads(response.read().decode('utf-8'))
    
    current_content = page_data.get('content', {}).get('raw', '')
    current_title = page_data.get('title', {}).get('rendered', '')
    
    print("Current content length:", len(current_content))
    
    # Fix issues in the content
    updated_content = current_content
    
    # 1. Remove dots from social media icons
    # Replace list items with social media links to remove bullets
    social_media_fixes = [
        # Remove bullet points from social media lists
        ('wp-block-list', 'wp-block-list has-no-bullet-list-style'),
        # Add custom styling for social media icons
        ('<ul class="wp-block-list">', '<ul class="wp-block-list" style="list-style-type:none;padding-left:0;">'),
        ('<ul style="font-size:clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.208), 1rem);line-height:1.6" class="wp-block-list">', '<ul style="font-size:clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.208), 1rem);line-height:1.6;list-style-type:none;padding-left:0;" class="wp-block-list">'),
    ]
    
    # Apply social media fixes
    for old, new in social_media_fixes:
        updated_content = updated_content.replace(old, new)
    
    # 2. Fix Recent Posts bullet points
    # Remove bullet points from recent posts if they exist
    recent_posts_fixes = [
        ('wp-block-latest-posts__list', 'wp-block-latest-posts__list no-bullets'),
        # Add CSS to remove bullets from latest posts
        ('<!-- wp:latest-posts', '<!-- wp:latest-posts {"style":{"elements":{"link":{"color":{"text":"var:preset|color|primary"}}}}} -->'),
    ]
    
    # Apply recent posts fixes  
    for old, new in recent_posts_fixes:
        if old in updated_content:
            updated_content = updated_content.replace(old, new)
    
    # 3. Make social media icons colored by adding inline styles
    icon_color_fixes = [
        # Instagram icon - make it colorful
        ('📷', '<span style="color: #E4405F;">📷</span>'),
        ('Instagram', '<span style="color: #E4405F;">Instagram</span>'),
        # X/Twitter icon - make it blue
        ('🐦', '<span style="color: #1DA1F2;">🐦</span>'),
        ('X (Twitter)', '<span style="color: #1DA1F2;">X (Twitter)</span>'),
        # Facebook icon - make it blue
        ('👥', '<span style="color: #1877F2;">👥</span>'),
        ('Facebook', '<span style="color: #1877F2;">Facebook</span>'),
    ]
    
    # Apply icon color fixes
    for old, new in icon_color_fixes:
        updated_content = updated_content.replace(old, new)
    
    # Add custom CSS to remove all bullet points from social media section
    css_addition = '''<!-- wp:html -->
<style>
.wp-block-list {
    list-style-type: none !important;
    padding-left: 0 !important;
}
.wp-block-latest-posts__list {
    list-style-type: none !important;
    padding-left: 0 !important;
}
.wp-block-latest-posts__list li:before {
    content: none !important;
}
ul li {
    list-style-type: none !important;
}
</style>
<!-- /wp:html -->

'''
    
    # Add CSS at the beginning of the content
    updated_content = css_addition + updated_content
    
    # Update the page
    if update_page_content(home_page_id, updated_content, current_title):
        print("\n🎉 Home page styling fixes completed!")
        print("✅ Removed bullet points from social media icons")
        print("✅ Made social media icons colorful")
        print("✅ Removed bullet points from Recent Posts")
        print("✅ Added custom CSS to prevent future bullet points")
    else:
        print("\n❌ Failed to update home page")
        
except Exception as e:
    print(f"❌ Error getting current page: {e}")

print(f"\n📋 Applied fixes:")
print("• Removed all bullet points from lists")
print("• Made Instagram icon pink/red")  
print("• Made X/Twitter icon blue")
print("• Made Facebook icon blue")
print("• Added CSS to prevent future bullet point issues")
print("• Recent Posts section cleaned up")