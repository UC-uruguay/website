#!/usr/bin/env python3
import urllib.request
import json

class HomepageTitleUpdater:
    def __init__(self):
        # Load authentication info
        try:
            with open('/home/uc/wordpress_auth.json', 'r') as f:
                self.auth_info = json.load(f)
        except FileNotFoundError:
            print("❌ Authentication info not found")
            return
        
        self.site_url = self.auth_info['site_url']
        self.token = self.auth_info['base64_token']
        self.homepage_id = 11
    
    def update_homepage_title(self):
        """Update homepage title to remove 'Creative Soul from Japan'"""
        try:
            print("🔄 Updating homepage title...")
            
            page_data = {
                "title": "UC"
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            request.get_method = lambda: 'POST'
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print(f"✅ Homepage title updated to: {result.get('title', {}).get('rendered', 'UC')}")
            return True
            
        except Exception as e:
            print(f"❌ Error updating homepage title: {e}")
            return False
    
    def add_multilingual_support(self):
        """Add language switching functionality"""
        try:
            print("🌐 Adding multilingual support...")
            
            # Simple language switcher content to add to the site
            language_switcher_content = """
            <!-- Language Switcher -->
            <div class="language-switcher" style="position: fixed; top: 20px; right: 20px; background: #ffffff; padding: 10px; border-radius: 5px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); z-index: 1000;">
                <a href="/" style="text-decoration: none; margin-right: 10px; padding: 5px 10px; background: #2c3e50; color: white; border-radius: 3px; font-size: 12px;">🇯🇵 日本語</a>
                <a href="/en" style="text-decoration: none; padding: 5px 10px; background: #3498db; color: white; border-radius: 3px; font-size: 12px;">🇺🇸 English</a>
            </div>
            """
            
            print("📝 Language switcher HTML prepared")
            print("💡 To add multilingual support:")
            print("   1. Install a WordPress multilingual plugin like WPML or Polylang")
            print("   2. Or add the language switcher HTML to your theme's header.php")
            print("   3. Create English translations of your content")
            
            return True
            
        except Exception as e:
            print(f"❌ Error adding multilingual support: {e}")
            return False

def main():
    updater = HomepageTitleUpdater()
    
    print("🚀 Homepage Title Update & Multilingual Support")
    print("=" * 50)
    
    # Update homepage title
    title_updated = updater.update_homepage_title()
    
    # Add multilingual support info
    multilingual_added = updater.add_multilingual_support()
    
    print("\n🎉 Updates Completed!")
    print("=" * 50)
    if title_updated:
        print("✅ Homepage title: Changed from 'UC - Creative Soul from Japan' to 'UC'")
    if multilingual_added:
        print("✅ Multilingual support: Instructions provided")
    
    print(f"\n🌐 Site: https://uc.x0.com")

if __name__ == "__main__":
    main()