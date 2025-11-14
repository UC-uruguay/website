#!/usr/bin/env python3
"""
Clean navigation menu - keep only Blog link, remove SNS links
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🧹 Cleaning navigation menu - keeping only Blog...")

def get_menus():
    """Get all menus"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menus")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            menus = json.loads(response.read().decode('utf-8'))
        return menus
    except Exception as e:
        print(f"❌ Error getting menus: {e}")
        return []

def get_menu_items(menu_id):
    """Get menu items"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items?menu={menu_id}")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            items = json.loads(response.read().decode('utf-8'))
        return items
    except Exception as e:
        print(f"❌ Error getting menu items: {e}")
        return []

def delete_menu_item(item_id):
    """Delete a menu item"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items/{item_id}")
        request.add_header('Authorization', f'Basic {token}')
        request.get_method = lambda: 'DELETE'
        
        with urllib.request.urlopen(request) as response:
            response.read()
        return True
    except Exception as e:
        print(f"❌ Error deleting menu item {item_id}: {e}")
        return False

def add_menu_item(menu_id, title, url):
    """Add menu item"""
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
        return result.get('id')
    except Exception as e:
        print(f"❌ Error adding menu item {title}: {e}")
        return None

# Get all menus
menus = get_menus()
navigation_menu_id = None

# Find navigation/primary menu
for menu in menus:
    menu_name = menu.get('name', '').lower()
    if any(keyword in menu_name for keyword in ['primary', 'main', 'navigation', 'header']):
        navigation_menu_id = menu.get('id')
        print(f"📋 Found navigation menu: {menu.get('name')} (ID: {navigation_menu_id})")
        break

# If no specific navigation menu found, look for any menu that's not footer
if not navigation_menu_id:
    for menu in menus:
        menu_name = menu.get('name', '').lower()
        if 'footer' not in menu_name:
            navigation_menu_id = menu.get('id')
            print(f"📋 Using menu: {menu.get('name')} (ID: {navigation_menu_id})")
            break

if navigation_menu_id:
    # Get current menu items
    menu_items = get_menu_items(navigation_menu_id)
    
    print(f"🔍 Current menu items:")
    for item in menu_items:
        title_obj = item.get('title', '')
        if isinstance(title_obj, dict):
            title = title_obj.get('rendered', '')
        else:
            title = str(title_obj)
        url = item.get('url', '')
        print(f"  - {title}: {url}")
    
    # Delete all current menu items
    deleted_count = 0
    for item in menu_items:
        if delete_menu_item(item['id']):
            deleted_count += 1
            title_obj = item.get('title', '')
            if isinstance(title_obj, dict):
                title = title_obj.get('rendered', '')
            else:
                title = str(title_obj)
            print(f"  ✅ Deleted: {title}")
    
    print(f"✅ Deleted {deleted_count} menu items")
    
    # Add only Blog menu item
    blog_item_id = add_menu_item(navigation_menu_id, "Blog", f"{site_url}/blog/")
    if blog_item_id:
        print("✅ Added: Blog")
    
    print(f"\n🎉 Navigation menu cleaned!")
    print(f"📋 Navigation menu now contains:")
    print(f"  - Blog: {site_url}/blog/")
    
else:
    print("❌ Could not find navigation menu")
    print("\n📋 Manual Steps:")
    print("1. Go to WordPress Admin → Appearance → Menus")
    print("2. Select the Primary/Main navigation menu")
    print("3. Remove all SNS links (Facebook, Instagram, X/Twitter)")
    print("4. Keep only 'Blog' in the menu")
    print("5. Save the menu")

print(f"\n🔗 Test navigation at: {site_url}")
print("💡 The navigation should now show only 'Blog' in the top menu")
print("💡 SNS links remain in the footer as intended")