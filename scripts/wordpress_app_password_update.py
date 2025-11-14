#!/usr/bin/env python3
"""
WordPress Update using Application Passwords
"""
import urllib.request
import urllib.parse
import json
import base64

class WordPressAppPasswordUpdater:
    def __init__(self, site_url, username, app_password):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.app_password = app_password
        self.api_base = f"{self.site_url}/wp-json/wp/v2"
        
        # Create basic auth header for application password
        credentials = f"{username}:{app_password}"
        token = base64.b64encode(credentials.encode()).decode()
        self.auth_header = f'Basic {token}'
    
    def make_request(self, endpoint, method='GET', data=None):
        """Make authenticated request to WordPress REST API"""
        url = f"{self.api_base}/{endpoint}"
        
        # Prepare request
        if data:
            data = json.dumps(data).encode('utf-8')
        
        request = urllib.request.Request(url, data=data)
        request.add_header('Authorization', self.auth_header)
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda: method
        
        try:
            with urllib.request.urlopen(request) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_content = e.read().decode('utf-8')
            try:
                return json.loads(error_content)
            except:
                return {"error": f"HTTP {e.code}", "message": error_content}
    
    def get_current_user(self):
        """Get current user information"""
        return self.make_request('users/me')
    
    def check_permissions(self):
        """Check if user has admin permissions"""
        user_info = self.get_current_user()
        if 'capabilities' in user_info:
            return user_info['capabilities'].get('update_core', False)
        return False
    
    def get_wordpress_version(self):
        """Get current WordPress version from site info"""
        try:
            # Get site root info which includes WordPress version
            url = f"{self.site_url}/wp-json/"
            request = urllib.request.Request(url)
            request.add_header('Authorization', self.auth_header)
            
            with urllib.request.urlopen(request) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data.get('wordpress_version', 'Unknown')
        except Exception as e:
            return f"Error: {e}"
    
    def trigger_wp_cron(self):
        """Trigger WordPress cron to check for updates"""
        try:
            cron_url = f"{self.site_url}/wp-cron.php"
            request = urllib.request.Request(cron_url)
            urllib.request.urlopen(request)
            return True
        except:
            return False

def main():
    print("WordPress Application Password Updater")
    print("=" * 50)
    
    # Note: You need to generate an application password from WordPress admin
    site_url = "https://uc.x0.com"
    username = "uc-japan" 
    
    print("⚠️  Application Password Required")
    print("To use this method, you need to:")
    print("1. Log into WordPress admin panel")
    print("2. Go to Users → Profile")
    print("3. Generate an Application Password")
    print("4. Use that password instead of your regular password")
    print()
    
    # For now, we'll try with the regular password, but this likely won't work
    # for admin operations due to WordPress security restrictions
    app_password = "Tis30426810cd067d!"
    
    updater = WordPressAppPasswordUpdater(site_url, username, app_password)
    
    # Check current user
    print("Checking current user...")
    user_info = updater.get_current_user()
    print(f"User info: {user_info}")
    
    # Get WordPress version
    print("\nGetting WordPress version...")
    version = updater.get_wordpress_version()
    print(f"WordPress version: {version}")
    
    # Check permissions
    print("\nChecking update permissions...")
    can_update = updater.check_permissions()
    print(f"Can update core: {can_update}")
    
    # Trigger cron to check for updates
    print("\nTriggering WordPress cron...")
    cron_success = updater.trigger_wp_cron()
    print(f"Cron triggered: {cron_success}")

if __name__ == "__main__":
    main()