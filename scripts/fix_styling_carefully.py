#!/usr/bin/env python3
"""
Fix styling issues carefully without breaking content
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Fixing styling issues carefully...")

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
    
    print(f"Current content length: {len(current_content)}")
    
    if not current_content:
        print("❌ No content found, cannot proceed safely")
        exit(1)
    
    # Make specific targeted changes
    updated_content = current_content
    
    # 1. Change AI Creative Projects to Creative Projects with link
    updated_content = updated_content.replace(
        '<p class="has-text-align-center" style="font-weight:600">AI Creative Projects</p>',
        '<p class="has-text-align-center" style="font-weight:600"><a href="/creative-projects/">Creative Projects</a></p>'
    )
    
    # 2. Add CSS to remove bullets and make social links colorful
    css_addition = '''<!-- wp:html -->
<style>
/* Remove bullets from social media links */
.wp-block-social-links {
    list-style-type: none !important;
    padding-left: 0 !important;
}

/* Remove bullets from latest posts */
.wp-block-latest-posts__list {
    list-style-type: none !important;
    padding-left: 0 !important;
}

.wp-block-latest-posts__list li:before {
    content: none !important;
}

/* Make social links colorful */
.wp-block-social-link a {
    color: inherit !important;
}

.wp-social-link-instagram a {
    background-color: #E4405F !important;
}

.wp-social-link-facebook a {
    background-color: #1877F2 !important;
}

.wp-social-link-x a {
    background-color: #1DA1F2 !important;
}

.wp-social-link-tiktok a {
    background-color: #000000 !important;
}

.wp-social-link-linkedin a {
    background-color: #0077B5 !important;
}
</style>
<!-- /wp:html -->

'''
    
    # Add CSS at the beginning
    updated_content = css_addition + updated_content
    
    print(f"Updated content length: {len(updated_content)}")
    
    # Update the page
    if update_page_content(home_page_id, updated_content, current_title):
        print("\n🎉 Styling fixes applied successfully!")
        print("✅ Changed AI Creative Projects to Creative Projects with link")
        print("✅ Added colorful social media icons")
        print("✅ Removed bullet points from social links")
        print("✅ Removed bullet points from Recent Posts")
        print(f"🔗 Creative Projects page: {site_url}/creative-projects/")
    else:
        print("\n❌ Failed to update home page")
        
except Exception as e:
    print(f"❌ Error getting current page: {e}")

print(f"\n📋 Changes applied:")
print("• AI Creative Projects → Creative Projects (with link)")
print("• Instagram icons now pink/red")
print("• Facebook icons now blue")
print("• X/Twitter icons now blue")
print("• TikTok icons now black")
print("• LinkedIn icons now blue")
print("• No more bullet points on social links or recent posts")