#!/usr/bin/env python3
import requests
import json
import base64

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

def get_homepage():
    """Get homepage content"""
    # First, get the front page ID
    response = requests.get(f"{site_url}/wp-json/wp/v2/pages", headers=headers)
    if response.status_code != 200:
        print(f"Failed to get pages: {response.status_code}")
        return None
    
    pages = response.json()
    homepage = None
    
    # Look for homepage (usually has slug 'home' or is set as front page)
    for page in pages:
        if page.get('slug') == 'home' or page.get('slug') == '':
            homepage = page
            break
    
    if not homepage and pages:
        homepage = pages[0]  # Fallback to first page
    
    return homepage

def update_homepage_content(page_id, new_content):
    """Update homepage content"""
    data = {
        'content': new_content
    }
    
    response = requests.post(f"{site_url}/wp-json/wp/v2/pages/{page_id}", 
                           headers=headers, 
                           data=json.dumps(data))
    
    if response.status_code == 200:
        print("Homepage updated successfully!")
        return response.json()
    else:
        print(f"Failed to update homepage: {response.status_code}")
        print(response.text)
        return None

def create_page(title, slug, content=""):
    """Create a new page"""
    data = {
        'title': title,
        'slug': slug,
        'content': content,
        'status': 'publish'
    }
    
    response = requests.post(f"{site_url}/wp-json/wp/v2/pages",
                           headers=headers,
                           data=json.dumps(data))
    
    if response.status_code == 201:
        page_data = response.json()
        print(f"Page '{title}' created successfully!")
        print(f"URL: {page_data['link']}")
        return page_data
    else:
        print(f"Failed to create page '{title}': {response.status_code}")
        print(response.text)
        return None

# Main execution
if __name__ == "__main__":
    print("Updating homepage sections...")
    
    # Get current homepage
    homepage = get_homepage()
    if not homepage:
        print("Could not find homepage")
        exit(1)
    
    print(f"Found homepage: {homepage['title']['rendered']}")
    
    # Create new pages first
    print("\nCreating new pages...")
    
    # Create 人生最高の瞬間 page
    moments_page = create_page("人生最高の瞬間", "best-moments", "<p>人生最高の瞬間のページです。内容は後で追加されます。</p>")
    
    # Create プロダクト page  
    products_page = create_page("プロダクト", "products", "<p>プロダクトページです。内容は後で追加されます。</p>")
    
    if not moments_page or not products_page:
        print("Failed to create required pages")
        exit(1)
    
    # Update homepage content to change section names and add links
    current_content = homepage['content']['raw']
    
    # Replace "Family Moments" with "人生最高の瞬間" and add link
    updated_content = current_content.replace(
        'Family Moments',
        f'<a href="{moments_page["link"]}">人生最高の瞬間</a>'
    )
    
    # Replace "Wine Tasting" with "プロダクト" and add link, also change grape icon to product icon
    updated_content = updated_content.replace(
        '🍇',
        '📦'  # Product/package icon
    )
    
    updated_content = updated_content.replace(
        'Wine Tasting',
        f'<a href="{products_page["link"]}">プロダクト</a>'
    )
    
    print(f"\nUpdating homepage content...")
    result = update_homepage_content(homepage['id'], updated_content)
    
    if result:
        print(f"\n✅ All updates completed successfully!")
        print(f"Homepage URL: {result['link']}")
        print(f"人生最高の瞬間 page: {moments_page['link']}")
        print(f"プロダクト page: {products_page['link']}")
    else:
        print("Failed to update homepage")