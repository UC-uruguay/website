#!/usr/bin/env python3
"""
WordPress Update via Admin Session with JWT
Final working solution for Claude Code WordPress updates
"""
import urllib.request
import urllib.parse
import http.cookiejar
import json
import re
import base64

class WordPressUpdater:
    def __init__(self, site_url, username, password):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.password = password
        
        # Setup session with cookies
        self.cookie_jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie_jar))
        self.opener.addheaders = [('User-Agent', 'Claude-Code-WordPress-Updater/1.0')]
        
        # JWT token storage
        self.jwt_token = None
    
    def get_jwt_token(self):
        """Get JWT token for authentication"""
        if self.jwt_token:
            return self.jwt_token
            
        try:
            login_data = {
                'username': self.username,
                'password': self.password
            }
            
            data = json.dumps(login_data).encode('utf-8')
            request = urllib.request.Request(
                f"{self.site_url}/wp-json/jwt-auth/v1/token",
                data=data
            )
            request.add_header('Content-Type', 'application/json')
            
            response = self.opener.open(request)
            result = json.loads(response.read().decode('utf-8'))
            
            if 'token' in result:
                self.jwt_token = result['token']
                print(f"✅ JWT Token acquired successfully")
                return self.jwt_token
            else:
                print(f"❌ JWT Token acquisition failed: {result}")
                return None
                
        except Exception as e:
            print(f"❌ Error getting JWT token: {e}")
            return None
    
    def admin_login(self):
        """Login to WordPress admin panel"""
        try:
            print("🔐 Logging into WordPress admin...")
            
            # Get login page
            login_url = f"{self.site_url}/wp-login.php"
            response = self.opener.open(login_url)
            login_page = response.read().decode('utf-8')
            
            # Prepare login data
            login_data = {
                'log': self.username,
                'pwd': self.password,
                'wp-submit': 'ログイン',
                'redirect_to': f"{self.site_url}/wp-admin/",
                'testcookie': '1'
            }
            
            # Submit login
            data = urllib.parse.urlencode(login_data).encode('utf-8')
            request = urllib.request.Request(login_url, data=data)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('Referer', login_url)
            
            response = self.opener.open(request)
            
            # Check login success
            if 'wp-admin' in response.geturl() and 'wp-login' not in response.geturl():
                print("✅ Admin login successful!")
                return True
            else:
                print("❌ Admin login failed")
                return False
                
        except Exception as e:
            print(f"❌ Admin login error: {e}")
            return False
    
    def check_wordpress_version(self):
        """Check current WordPress version"""
        try:
            # Try via REST API first
            request = urllib.request.Request(f"{self.site_url}/wp-json/")
            response = self.opener.open(request)
            data = json.loads(response.read().decode('utf-8'))
            
            version = data.get('wordpress_version', 'Unknown')
            print(f"📋 Current WordPress version: {version}")
            return version
            
        except Exception as e:
            print(f"⚠️  Could not determine WordPress version: {e}")
            return 'Unknown'
    
    def force_update_check(self):
        """Force WordPress to check for updates"""
        try:
            print("🔍 Forcing WordPress update check...")
            
            # Access update-core.php to trigger update check
            update_url = f"{self.site_url}/wp-admin/update-core.php?force-check=1"
            request = urllib.request.Request(update_url)
            request.add_header('Referer', f"{self.site_url}/wp-admin/")
            
            response = self.opener.open(request)
            page_content = response.read().decode('utf-8')
            
            # Check if updates are available
            if '新しいバージョンの WordPress' in page_content or 'new version of WordPress' in page_content:
                print("✅ WordPress updates found!")
                return True, page_content
            elif '最新版の WordPress' in page_content or 'WordPress is up to date' in page_content:
                print("ℹ️  WordPress is already up to date")
                return False, page_content
            else:
                print("⚠️  Update status unclear")
                return None, page_content
                
        except Exception as e:
            print(f"❌ Error checking for updates: {e}")
            return None, None
    
    def perform_core_update(self, update_page_content):
        """Perform WordPress core update"""
        try:
            print("🚀 Starting WordPress core update...")
            
            # Extract nonce from update page
            nonce_pattern = r'_wpnonce["\']?\s*[:=]\s*["\']([^"\']+)'
            nonce_match = re.search(nonce_pattern, update_page_content)
            
            if not nonce_match:
                print("❌ Could not find update nonce")
                return False
                
            nonce = nonce_match.group(1)
            print(f"🔑 Found update nonce: {nonce[:10]}...")
            
            # Extract version information
            version_pattern = r'WordPress\s+([0-9.]+)'
            version_match = re.search(version_pattern, update_page_content)
            new_version = version_match.group(1) if version_match else ''
            
            if new_version:
                print(f"📦 Updating to WordPress version: {new_version}")
            
            # Prepare update request
            update_data = {
                'action': 'do-core-upgrade',
                '_wpnonce': nonce,
                'version': new_version,
                'locale': 'ja'
            }
            
            # Submit update request
            update_url = f"{self.site_url}/wp-admin/update-core.php"
            data = urllib.parse.urlencode(update_data).encode('utf-8')
            
            request = urllib.request.Request(update_url, data=data)
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('Referer', update_url)
            
            print("⏳ Executing WordPress core update...")
            response = self.opener.open(request)
            result_content = response.read().decode('utf-8')
            
            # Check update result
            if ('アップデートが完了しました' in result_content or 
                'Update Complete' in result_content or
                'WordPress has been updated' in result_content):
                print("✅ WordPress core update completed successfully!")
                return True
            elif 'すでに最新' in result_content or 'already up to date' in result_content:
                print("ℹ️  WordPress was already up to date")
                return True
            else:
                print("⚠️  Update status unclear - please check admin panel")
                # Save debug info
                with open('/home/uc/update_result.html', 'w', encoding='utf-8') as f:
                    f.write(result_content)
                print("📝 Update result saved to update_result.html for debugging")
                return False
                
        except Exception as e:
            print(f"❌ Update error: {e}")
            return False
    
    def run_complete_update(self):
        """Run complete WordPress update process"""
        print("🚀 Claude Code WordPress Updater")
        print("=" * 50)
        
        # Step 1: Get JWT token
        jwt_token = self.get_jwt_token()
        if jwt_token:
            print(f"🔐 JWT Authentication ready")
        
        # Step 2: Admin login
        if not self.admin_login():
            print("❌ Cannot proceed without admin access")
            return False
        
        # Step 3: Check current version
        current_version = self.check_wordpress_version()
        
        # Step 4: Check for updates
        has_updates, update_page = self.force_update_check()
        
        if has_updates is None:
            print("❌ Could not determine update status")
            return False
        elif not has_updates:
            print("✅ WordPress is already up to date!")
            return True
        
        # Step 5: Perform update
        update_success = self.perform_core_update(update_page)
        
        if update_success:
            print("\n🎉 WordPress update process completed successfully!")
            print("🔍 Please verify the update in your WordPress admin panel")
            
            # Check new version
            new_version = self.check_wordpress_version()
            if new_version != current_version:
                print(f"📈 Version updated: {current_version} → {new_version}")
        else:
            print("\n❌ WordPress update encountered issues")
            print("🔍 Please check the WordPress admin panel manually")
        
        return update_success

def main():
    site_url = "https://uc.x0.com"
    username = "uc-japan"
    password = "Tis30426810cd067d!"
    
    updater = WordPressUpdater(site_url, username, password)
    success = updater.run_complete_update()
    
    return success

if __name__ == "__main__":
    main()