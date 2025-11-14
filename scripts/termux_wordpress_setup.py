#!/usr/bin/env python3
"""
Termux WordPress Blog Manager
Simple WordPress posting script for mobile Termux environment
"""
import urllib.request
import json
import base64
import os
import mimetypes
from pathlib import Path

class TermuxWordPressBlogger:
    def __init__(self, config_file="wp_config.json"):
        self.config_file = config_file
        self.config = self.load_config()
        
    def load_config(self):
        """Load WordPress configuration"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("❌ WordPress config file not found!")
            print("📝 Creating sample config file...")
            self.create_sample_config()
            return {}
    
    def create_sample_config(self):
        """Create sample configuration file"""
        sample_config = {
            "site_url": "https://uc.x0.com",
            "username": "your_username",
            "app_password": "your_app_password",
            "base64_token": "username:app_password encoded in base64"
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(sample_config, f, indent=2)
        
        print(f"✅ Sample config created: {self.config_file}")
        print("📝 Please edit the config file with your WordPress credentials")
    
    def setup_auth_token(self, username, app_password):
        """Setup authentication token"""
        auth_string = f"{username}:{app_password}"
        token = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        
        self.config.update({
            "username": username,
            "app_password": app_password,
            "base64_token": token
        })
        
        # Save updated config
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
        
        print("✅ Authentication token updated!")
    
    def upload_image(self, image_path):
        """Upload image to WordPress media library"""
        if not os.path.exists(image_path):
            print(f"❌ Image not found: {image_path}")
            return None, None
        
        try:
            print(f"📸 Uploading image: {image_path}")
            
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            mime_type, _ = mimetypes.guess_type(image_path)
            filename = os.path.basename(image_path)
            
            request = urllib.request.Request(f"{self.config['site_url']}/wp-json/wp/v2/media")
            request.add_header('Authorization', f'Basic {self.config["base64_token"]}')
            request.add_header('Content-Type', mime_type)
            request.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            request.data = image_data
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            media_id = result['id']
            image_url = result['source_url']
            print(f"✅ Image uploaded (ID: {media_id})")
            
            return media_id, image_url
            
        except Exception as e:
            print(f"❌ Image upload error: {e}")
            return None, None
    
    def create_post(self, title, content, image_path=None):
        """Create WordPress post"""
        try:
            print("📝 Creating WordPress post...")
            
            # Upload image if provided
            media_id, image_url = None, None
            if image_path:
                media_id, image_url = self.upload_image(image_path)
                
                if media_id and image_url:
                    # Add image to content
                    image_block = f'''<!-- wp:image {{"id":{media_id},"align":"center"}} -->
<div class="wp-block-image">
<figure class="aligncenter">
<img src="{image_url}" alt="" class="wp-image-{media_id}"/>
</figure>
</div>
<!-- /wp:image -->

'''
                    content = image_block + content
            
            post_data = {
                "title": title,
                "content": content,
                "status": "publish"
            }
            
            data = json.dumps(post_data).encode('utf-8')
            request = urllib.request.Request(f"{self.config['site_url']}/wp-json/wp/v2/posts", data=data)
            request.add_header('Authorization', f'Basic {self.config["base64_token"]}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            post_id = result['id']
            post_url = result['link']
            
            print(f"✅ Post created successfully!")
            print(f"📰 Post ID: {post_id}")
            print(f"🌐 URL: {post_url}")
            
            return result
            
        except Exception as e:
            print(f"❌ Post creation error: {e}")
            return None
    
    def interactive_post(self):
        """Interactive post creation"""
        print("📱 Termux WordPress Blogger")
        print("=" * 40)
        
        if not self.config.get('base64_token'):
            print("❌ No authentication configured!")
            print("Please run setup first or edit wp_config.json")
            return
        
        # Get post details
        title = input("📝 Post title: ")
        print("✍️ Post content (end with empty line):")
        
        content_lines = []
        while True:
            line = input()
            if line == "":
                break
            content_lines.append(line)
        
        content = "<!-- wp:paragraph -->\n<p>" + "</p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph -->\n<p>".join(content_lines) + "</p>\n<!-- /wp:paragraph -->"
        
        # Check for image
        image_path = input("📸 Image path (optional, press enter to skip): ").strip()
        if not image_path:
            image_path = None
        
        # Create post
        result = self.create_post(title, content, image_path)
        
        if result:
            print("\n🎉 Post published successfully!")
        else:
            print("\n❌ Failed to publish post")
    
    def quick_post(self, title, text, image_path=None):
        """Quick post with simple text"""
        content = f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->"
        return self.create_post(title, content, image_path)

def main():
    blogger = TermuxWordPressBlogger()
    
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "setup":
            print("🔧 WordPress Setup")
            site_url = input("Site URL: ")
            username = input("Username: ")
            app_password = input("App Password: ")
            
            blogger.config["site_url"] = site_url
            blogger.setup_auth_token(username, app_password)
            
        elif command == "post":
            blogger.interactive_post()
            
        elif command == "quick":
            if len(sys.argv) >= 4:
                title = sys.argv[2]
                text = sys.argv[3]
                image = sys.argv[4] if len(sys.argv) > 4 else None
                blogger.quick_post(title, text, image)
            else:
                print("Usage: python wp.py quick 'title' 'text' [image_path]")
    else:
        print("📱 Termux WordPress Blogger")
        print("Commands:")
        print("  setup  - Configure WordPress credentials")
        print("  post   - Interactive post creation")
        print("  quick  - Quick post: python wp.py quick 'title' 'text' [image]")

if __name__ == "__main__":
    main()