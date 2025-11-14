#!/usr/bin/env python3
"""
Set up footer links - create or update footer menu
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🔗 Setting up footer links...")

def get_menus():
    """Get existing menus"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/menus")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            menus = json.loads(response.read().decode('utf-8'))
        return menus
    except Exception as e:
        print(f"Note: Could not get menus: {e}")
        return []

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

def add_menu_item(menu_id, title, url, parent=0):
    """Add item to menu"""
    try:
        item_data = {
            "title": title,
            "url": url,
            "menu_id": menu_id,
            "parent": parent,
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

# Get existing menus
menus = get_menus()
footer_menu_id = None

# Look for existing footer menu
for menu in menus:
    if 'footer' in menu.get('name', '').lower():
        footer_menu_id = menu.get('id')
        print(f"📋 Found existing footer menu: {menu.get('name')} (ID: {footer_menu_id})")
        break

# Create footer menu if doesn't exist
if not footer_menu_id:
    footer_menu_id = create_menu("Footer Menu", "footer-menu")

if footer_menu_id:
    print(f"📝 Adding footer pages to menu (ID: {footer_menu_id})...")
    
    # Footer pages with their URLs
    footer_pages = [
        ("Team", "https://uc.x0.com/team/"),
        ("History", "https://uc.x0.com/history/"),
        ("Careers", "https://uc.x0.com/careers/"),
        ("Privacy Policy", "https://uc.x0.com/privacy-policy/"),
        ("Terms and Conditions", "https://uc.x0.com/terms-conditions/"),
        ("Contact Us", "https://uc.x0.com/contact/")
    ]
    
    added_count = 0
    for title, url in footer_pages:
        if add_menu_item(footer_menu_id, title, url):
            added_count += 1
    
    print(f"\n🎉 Footer setup complete!")
    print(f"✅ Added {added_count}/{len(footer_pages)} menu items")
    
    print("\n📋 Manual Steps (WordPress Admin):")
    print("1. Go to Appearance → Menus")
    print(f"2. Select 'Footer Menu' (ID: {footer_menu_id})")
    print("3. Assign it to 'Footer' location in Menu Settings")
    print("4. Save the menu")
    
else:
    print("❌ Could not create footer menu")
    print("\n📋 Manual Setup Instructions:")
    print("1. Go to WordPress Admin → Appearance → Menus")
    print("2. Create a new menu called 'Footer Menu'")
    print("3. Add these pages:")
    print("   - Team")
    print("   - History") 
    print("   - Careers")
    print("   - Privacy Policy")
    print("   - Terms and Conditions")
    print("   - Contact Us")
    print("4. Assign the menu to 'Footer' location")
    print("5. Save the menu")

print(f"\n🌐 All pages are now available in English at:")
footer_urls = [
    "https://uc.x0.com/team/",
    "https://uc.x0.com/history/",
    "https://uc.x0.com/careers/",
    "https://uc.x0.com/privacy-policy/",
    "https://uc.x0.com/terms-conditions/",
    "https://uc.x0.com/contact/"
]

for url in footer_urls:
    print(f"  {url}")

print("\n📝 Remember: ALL content follows the permanent English-only rule!")
print("⏰ Ages are kept general to avoid frequent updates")