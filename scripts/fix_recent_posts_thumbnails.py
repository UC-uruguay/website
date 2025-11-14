#!/usr/bin/env python3
"""
Fix Recent Posts thumbnail images overflowing from their containers
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🖼️ Fixing Recent Posts thumbnail overflow issue...")

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
    
    # Add CSS to fix thumbnail overflow issues
    css_fix = '''<!-- wp:html -->
<style>
/* Fix Recent Posts thumbnail overflow */
.wp-block-latest-posts__featured-image img {
    width: 100% !important;
    height: auto !important;
    max-width: 100% !important;
    object-fit: cover !important;
    border-radius: 8px !important;
}

.wp-block-latest-posts__featured-image {
    overflow: hidden !important;
    border-radius: 8px !important;
    max-width: 150px !important;
    max-height: 120px !important;
    flex-shrink: 0 !important;
}

.wp-block-latest-posts li {
    overflow: hidden !important;
    margin-bottom: 20px !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 15px !important;
}

.wp-block-latest-posts__post-title {
    flex: 1 !important;
    margin: 0 !important;
    line-height: 1.4 !important;
}

.wp-block-latest-posts__post-excerpt {
    margin-top: 8px !important;
    color: #666 !important;
    line-height: 1.5 !important;
}

.wp-block-latest-posts__post-date {
    font-size: 0.9rem !important;
    color: #999 !important;
    margin-top: 5px !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .wp-block-latest-posts__featured-image {
        max-width: 120px !important;
        max-height: 100px !important;
    }
    
    .wp-block-latest-posts li {
        gap: 12px !important;
    }
}
</style>
<!-- /wp:html -->

'''
    
    # Add CSS at the beginning of content
    updated_content = css_fix + current_content
    
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
    
    print("\n🎉 Recent Posts thumbnail issue fixed!")
    print("✅ Added CSS to prevent image overflow")
    print("✅ Set proper image dimensions and object-fit")
    print("✅ Improved responsive design for mobile")
    print("✅ Better spacing and layout for post items")
    print(f"🔗 Check it at: {site_url}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print(f"\n📋 Applied fixes:")
print("• Thumbnail images: Fixed overflow with proper dimensions")
print("• Image sizing: Max 150px wide, 120px tall (120px/100px on mobile)")
print("• Object-fit: Cover to maintain aspect ratio")
print("• Border radius: 8px for modern look")
print("• Layout: Improved flex layout with proper gaps")
print("• Responsive: Smaller thumbnails on mobile devices")