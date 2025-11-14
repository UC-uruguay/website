#!/usr/bin/env python3
"""
Create a clean navigation menu with only Blog
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🗂️ Creating clean navigation menu with only Blog...")

def create_menu(name, slug):
    """Create a new menu"""
    try:
        menu_data = {
            "name": name,
            "slug": slug
        }
        
        data = json.dumps(menu_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menus", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"✅ Created menu: {name} (ID: {result.get('id')})")
        return result.get('id')
        
    except Exception as e:
        print(f"❌ Error creating menu {name}: {e}")
        return None

def add_menu_item(menu_id, title, url):
    """Add item to menu"""
    try:
        item_data = {
            "title": title,
            "url": url,
            "menu_id": menu_id,
            "status": "publish"
        }
        
        data = json.dumps(item_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"  ✅ Added: {title}")
        return result.get('id')
        
    except Exception as e:
        print(f"  ❌ Error adding {title}: {e}")
        return None

def get_page_by_slug(slug):
    """Get page by slug"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages?slug={slug}")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            pages = json.loads(response.read().decode('utf-8'))
        
        if pages:
            return pages[0]
        return None
        
    except Exception as e:
        print(f"❌ Error getting page {slug}: {e}")
        return None

# Create primary navigation menu
primary_menu_id = create_menu("Primary Navigation", "primary-navigation")

if primary_menu_id:
    print(f"📝 Adding Blog to primary menu (ID: {primary_menu_id})...")
    
    # Get blog page
    blog_page = get_page_by_slug("blog")
    
    if blog_page:
        # Add blog page to menu
        blog_url = blog_page.get('link', f"{site_url}/blog/")
    else:
        blog_url = f"{site_url}/blog/"
    
    blog_item_id = add_menu_item(primary_menu_id, "Blog", blog_url)
    
    if blog_item_id:
        print(f"✅ Primary navigation menu created successfully!")
        print(f"📋 Menu contains: Blog → {blog_url}")
        
        print(f"\n📋 Manual Steps (WordPress Admin):")
        print("1. Go to Appearance → Menus")
        print(f"2. Select 'Primary Navigation' menu (ID: {primary_menu_id})")
        print("3. In Menu Settings, assign it to 'Primary' or 'Header' location")
        print("4. Save the menu")
        print("5. Check that no other menus are assigned to the primary location")
        
    else:
        print("❌ Failed to add Blog to menu")
else:
    print("❌ Failed to create primary menu")

print(f"\n📋 Alternative Manual Steps:")
print("1. WordPress Admin → Appearance → Menus")
print("2. Click 'Create a new menu'")
print("3. Name it 'Primary Navigation'") 
print("4. Add only the 'Blog' page to this menu")
print("5. In Menu Settings → Display Location, check 'Primary Menu' or 'Header'")
print("6. Save the menu")
print("7. Make sure no SNS links are in this primary menu")

print(f"\n🔗 Test navigation at: {site_url}")
print("💡 The top navigation should show only 'Blog'")
print("💡 Footer navigation remains with all the footer pages")
print("💡 SNS icons remain in the footer content area")