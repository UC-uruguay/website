#!/usr/bin/env python3
"""
WordPress Update Script via REST API
"""
import requests
import json
import base64
from urllib.parse import urljoin

# WordPress site configuration
WORDPRESS_URL = "https://uc.x0.com"
USERNAME = "uc-japan"
PASSWORD = "Tis30426810cd067d!"

class WordPressUpdater:
    def __init__(self, url, username, password):
        self.base_url = url.rstrip('/')
        self.username = username
        self.password = password
        self.session = requests.Session()
        
        # Create basic auth header
        credentials = f"{username}:{password}"
        token = base64.b64encode(credentials.encode()).decode()
        self.session.headers.update({
            'Authorization': f'Basic {token}',
            'Content-Type': 'application/json'
        })
    
    def get_wordpress_version(self):
        """Get current WordPress version"""
        try:
            # Try to get version from REST API
            url = urljoin(self.base_url, '/wp-json/')
            response = self.session.get(url)
            if response.status_code == 200:
                data = response.json()
                return data.get('wordpress_version', 'Unknown')
        except Exception as e:
            print(f"Error getting WordPress version: {e}")
        return None
    
    def check_updates(self):
        """Check for available updates"""
        try:
            # Check core updates
            url = urljoin(self.base_url, '/wp-json/wp/v2/updates')
            response = self.session.get(url)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error checking updates: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error checking updates: {e}")
            return None
    
    def update_wordpress_core(self):
        """Update WordPress core"""
        try:
            # This requires a plugin or custom endpoint for core updates
            # WordPress REST API doesn't have a built-in core update endpoint
            print("WordPress core update via REST API requires additional setup.")
            print("Consider using WP-CLI or WordPress admin panel for core updates.")
            return False
        except Exception as e:
            print(f"Error updating WordPress core: {e}")
            return False
    
    def get_site_info(self):
        """Get basic site information"""
        try:
            url = urljoin(self.base_url, '/wp-json/wp/v2/settings')
            response = self.session.get(url)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error getting site info: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error getting site info: {e}")
            return None

def main():
    print("WordPress Update Tool")
    print("=" * 50)
    
    updater = WordPressUpdater(WORDPRESS_URL, USERNAME, PASSWORD)
    
    # Get WordPress version
    print("Getting WordPress version...")
    version = updater.get_wordpress_version()
    if version:
        print(f"Current WordPress version: {version}")
    
    # Get site info
    print("\nGetting site information...")
    site_info = updater.get_site_info()
    if site_info:
        print(f"Site title: {site_info.get('title', 'N/A')}")
        print(f"Site URL: {site_info.get('url', 'N/A')}")
    
    # Check for updates
    print("\nChecking for updates...")
    updates = updater.check_updates()
    if updates:
        print("Updates available:", json.dumps(updates, indent=2))
    else:
        print("Could not check for updates via REST API")
    
    # For actual core updates, we need alternative methods
    print("\nFor WordPress core updates, please use:")
    print("1. WordPress admin panel (recommended)")
    print("2. WP-CLI if available on server")
    print("3. Manual update via file upload")

if __name__ == "__main__":
    main()