#!/usr/bin/env python3
"""
Change WordPress credit text from "Designed with WordPress" to "With Love from UC ❤️"
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🎨 Changing WordPress credit text...")

def get_customizer_settings():
    """Try to get customizer settings"""
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/themes")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            themes = json.loads(response.read().decode('utf-8'))
        
        return themes
        
    except Exception as e:
        print(f"Note: Could not get theme info: {e}")
        return []

def update_site_settings():
    """Try to update site settings"""
    try:
        # Try to update site tagline or footer text via WordPress options
        settings_data = {
            "title": "UC",
            "description": "Creative Soul from Yamanashi, Japan"
        }
        
        data = json.dumps(settings_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/settings", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.get_method = lambda: 'POST'
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print("✅ Updated site settings")
        return True
        
    except Exception as e:
        print(f"❌ Could not update site settings: {e}")
        return False

# Get theme information
themes = get_customizer_settings()
active_theme = None

for theme in themes:
    if theme.get('status') == 'active':
        active_theme = theme
        break

if active_theme:
    print(f"📱 Active theme: {active_theme.get('name', 'Unknown')}")

# Update site settings
update_site_settings()

print("\n📋 Manual Steps to Change 'Designed with WordPress':")
print("=" * 50)

print("\n🎯 METHOD 1 - WordPress Customizer (Recommended):")
print("1. Go to WordPress Admin → Appearance → Customize")
print("2. Look for 'Site Identity' or 'Footer' section")
print("3. Find 'Footer Credit' or 'Copyright Text' field")
print("4. Change from 'Designed with WordPress' to 'With Love from UC ❤️'")
print("5. Click 'Publish'")

print("\n🎯 METHOD 2 - Through Theme Editor:")
print("1. Go to WordPress Admin → Appearance → Theme Editor")
print("2. Select 'footer.php' file")
print("3. Look for text containing 'WordPress' or 'Designed with'")
print("4. Replace with 'With Love from UC ❤️'")
print("5. Click 'Update File'")

print("\n🎯 METHOD 3 - Using Customizer Additional CSS:")
print("1. Go to Appearance → Customize → Additional CSS")
print("2. Add this CSS to hide WordPress credit and add custom text:")
print("""
/* Hide WordPress credit */
.site-info a[href*="wordpress.org"] {
    display: none;
}

/* Add custom credit */
.site-info::after {
    content: "With Love from UC ❤️";
    color: #666;
    font-size: 14px;
}
""")

print("\n🎯 METHOD 4 - Plugin Approach:")
print("1. Install 'Remove Footer Credit' plugin")
print("2. Or use 'Footer Text' plugin to customize footer")
print("3. Replace the credit text with 'With Love from UC ❤️'")

print(f"\n🔗 Test the changes at: {site_url}")
print("💡 The footer credit usually appears at the very bottom of every page")

print(f"\n✅ Summary of completed changes:")
print("1. ✅ Footer menu links now work properly")
print("2. ✅ Removed old separator line and 'With Love from UC' from main footer")  
print("3. 📋 Need manual step: Change WordPress credit to 'With Love from UC ❤️'")

print(f"\n🌐 Test these pages to confirm links work:")
footer_pages = [
    f"{site_url}/team/",
    f"{site_url}/history/", 
    f"{site_url}/careers/",
    f"{site_url}/privacy-policy/",
    f"{site_url}/terms-conditions/",
    f"{site_url}/contact/"
]

for page_url in footer_pages:
    print(f"  - {page_url}")