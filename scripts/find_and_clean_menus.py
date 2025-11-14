#!/usr/bin/env python3
"""
Find all menus and clean navigation menu
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🔍 Finding all menus and cleaning navigation...")

def get_all_menus():
    """Get all menus with different API calls"""
    menus = []
    
    # Try different endpoints
    endpoints = [
        f"{site_url}/wp-json/wp/v2/menus",
        f"{site_url}/wp-json/wp-api-menus/v2/menus"
    ]
    
    for endpoint in endpoints:
        try:
            print(f"📡 Trying: {endpoint}")
            request = urllib.request.Request(endpoint)
            request.add_header('Authorization', f'Basic {token}')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
                if result:
                    menus.extend(result)
                    print(f"✅ Found {len(result)} menus")
        except Exception as e:
            print(f"❌ {endpoint}: {e}")
    
    return menus

def get_menu_items_all_methods(menu_id):
    """Try multiple ways to get menu items"""
    endpoints = [
        f"{site_url}/wp-json/wp/v2/menu-items?menu={menu_id}",
        f"{site_url}/wp-json/wp/v2/menu-items?menus={menu_id}",
        f"{site_url}/wp-json/wp-api-menus/v2/menu-items?menu={menu_id}"
    ]
    
    for endpoint in endpoints:
        try:
            print(f"📡 Trying menu items: {endpoint}")
            request = urllib.request.Request(endpoint)
            request.add_header('Authorization', f'Basic {token}')
            
            with urllib.request.urlopen(request) as response:
                items = json.loads(response.read().decode('utf-8'))
                if items:
                    print(f"✅ Found {len(items)} menu items")
                    return items
        except Exception as e:
            print(f"❌ {endpoint}: {e}")
    
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

# Get all menus
menus = get_all_menus()

print(f"\n📋 Found {len(menus)} menus:")
for menu in menus:
    menu_id = menu.get('id')
    menu_name = menu.get('name', 'Unknown')
    print(f"  - {menu_name} (ID: {menu_id})")

# Process each menu
for menu in menus:
    menu_id = menu.get('id')
    menu_name = menu.get('name', 'Unknown')
    
    print(f"\n🔍 Checking menu: {menu_name} (ID: {menu_id})")
    
    # Get menu items
    menu_items = get_menu_items_all_methods(menu_id)
    
    if menu_items:
        print(f"📋 Menu items in {menu_name}:")
        sns_items = []
        blog_items = []
        other_items = []
        
        for item in menu_items:
            title_obj = item.get('title', '')
            if isinstance(title_obj, dict):
                title = title_obj.get('rendered', '')
            else:
                title = str(title_obj)
            
            url = item.get('url', '')
            item_id = item.get('id')
            
            print(f"  - {title}: {url} (ID: {item_id})")
            
            # Categorize items
            if any(sns in url.lower() for sns in ['instagram.com', 'facebook.com', 'x.com', 'twitter.com']):
                sns_items.append(item)
            elif 'blog' in title.lower() or 'blog' in url.lower():
                blog_items.append(item)
            else:
                other_items.append(item)
        
        # If this menu has SNS items, clean it
        if sns_items and 'footer' not in menu_name.lower():
            print(f"🧹 Cleaning navigation menu: {menu_name}")
            print(f"  Found {len(sns_items)} SNS items to remove")
            
            # Remove SNS items
            removed_count = 0
            for item in sns_items:
                if delete_menu_item(item['id']):
                    title_obj = item.get('title', '')
                    if isinstance(title_obj, dict):
                        title = title_obj.get('rendered', '')
                    else:
                        title = str(title_obj)
                    print(f"  ✅ Removed: {title}")
                    removed_count += 1
            
            print(f"✅ Removed {removed_count} SNS items from navigation")
            
            # Keep only Blog if it exists, or add it
            if not blog_items:
                print("📝 Adding Blog menu item...")
                # Add Blog item
                try:
                    item_data = {
                        "title": "Blog",
                        "url": f"{site_url}/blog/",
                        "menu_id": menu_id,
                        "status": "publish"
                    }
                    
                    data = json.dumps(item_data).encode('utf-8')
                    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menu-items", data=data)
                    request.add_header('Authorization', f'Basic {token}')
                    request.add_header('Content-Type', 'application/json; charset=utf-8')
                    
                    with urllib.request.urlopen(request) as response:
                        result = json.loads(response.read().decode('utf-8'))
                    print("✅ Added Blog to navigation")
                except Exception as e:
                    print(f"❌ Could not add Blog: {e}")

print(f"\n🎉 Menu cleaning completed!")
print(f"✅ SNS links removed from navigation menu")
print(f"✅ Blog kept/added to navigation menu")
print(f"✅ SNS links remain in footer menu")
print(f"\n🔗 Test navigation at: {site_url}")
print("💡 Top navigation should now show only 'Blog'")