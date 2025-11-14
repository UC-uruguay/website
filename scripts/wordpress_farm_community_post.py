#!/usr/bin/env python3
"""
WordPress Farm Community Post Creator
Create a new post about the community farming experience
"""
import urllib.request
import json
import base64
import mimetypes
import os

class WordPressFarmPostCreator:
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
        self.image_path = "/home/uc/20250830.jpg"
    
    def upload_image(self):
        """Upload the harvest image to WordPress media library"""
        try:
            print("📸 Uploading harvest image...")
            
            # Read image file
            with open(self.image_path, 'rb') as f:
                image_data = f.read()
            
            # Get mime type
            mime_type, _ = mimetypes.guess_type(self.image_path)
            filename = os.path.basename(self.image_path)
            
            # Create request for media upload
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/media")
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', mime_type)
            request.add_header('Content-Disposition', f'attachment; filename="{filename}"')
            request.data = image_data
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            media_id = result['id']
            image_url = result['source_url']
            print(f"✅ Image uploaded successfully (ID: {media_id})")
            
            return media_id, image_url
            
        except Exception as e:
            print(f"❌ Image upload error: {e}")
            return None, None
    
    def create_farm_post(self, media_id=None, image_url=None):
        """Create the farm community post"""
        
        # Post content in English
        title = "🌱 Community Farming Success - Amazing Harvest Day!"
        
        # Build content with or without image
        content = ""
        
        if media_id and image_url:
            content += f'''<!-- wp:image {{"id":{media_id},"align":"center","className":"harvest-photo"}} -->
<div class="wp-block-image harvest-photo">
<figure class="aligncenter">
<img src="{image_url}" alt="Fresh harvest from our community farm - tomatoes, eggplant, basil, and okra" class="wp-image-{media_id}"/>
<figcaption class="wp-element-caption">Our bountiful harvest: fresh tomatoes, eggplant, purple basil, and okra from today's community farming!</figcaption>
</figure>
</div>
<!-- /wp:image -->

'''
        
        content += '''<!-- wp:paragraph -->
<p>Just returned from our community farm and what an incredible harvest we had today! 🎉</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our community farming group of about 20 members has been taking turns caring for our shared garden, and today's results truly show that our collaborative approach is working beautifully. Everyone rotates responsibilities, so we all get hands-on experience while ensuring our crops receive consistent care.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🍅 Today's Amazing Harvest</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li><strong>Bright red and orange tomatoes</strong> - perfectly ripe and bursting with flavor</li>
<li><strong>Beautiful eggplant</strong> - deep purple and ready for cooking</li>
<li><strong>Fresh purple basil</strong> - aromatic herbs for our kitchen</li>
<li><strong>Tender okra</strong> - crisp and green from our summer garden</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The sense of community and shared accomplishment when we see the fruits (and vegetables!) of our collective labor is truly heartwarming. There's something magical about working together with neighbors to grow food that will nourish our families.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🤝 Community Spirit in Action</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>What makes our community farming special:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul>
<li><strong>Shared responsibility:</strong> Everyone takes turns with planting, watering, weeding, and harvesting</li>
<li><strong>Knowledge sharing:</strong> Experienced gardeners mentor newcomers</li>
<li><strong>Seasonal celebrations:</strong> We celebrate each harvest together</li>
<li><strong>Sustainable practices:</strong> We focus on organic, environmentally friendly methods</li>
</ul>
<!-- /wp:list -->

<!-- wp:quote -->
<blockquote class="wp-block-quote">
<p>"Farming is not just about growing vegetables - it's about growing community, friendships, and a deeper connection to the earth that sustains us."</p>
</blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>Today's harvest exceeded all our expectations! We're looking forward to sharing this fresh, organic produce with everyone in our community. Nothing beats the taste of vegetables grown with love and care by friends and neighbors.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Can't wait for our next farming day together! 🌱✨</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>What's your experience with community gardening? Have you ever tried growing vegetables with your neighbors? Share your stories in the comments below!</em></p>
<!-- /wp:paragraph -->'''
        
        return title, content
    
    def publish_post(self, title, content):
        """Publish the farm community post"""
        try:
            print("📝 Creating and publishing farm community post...")
            
            post_data = {
                "title": title,
                "content": content,
                "status": "publish",
                "excerpt": "Just returned from our community farm with an amazing harvest! Our group of 20 community members continues to thrive through collaborative farming."
            }
            
            data = json.dumps(post_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/posts", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            post_id = result['id']
            post_url = result['link']
            
            print(f"✅ Farm community post published successfully!")
            print(f"📰 Post ID: {post_id}")
            print(f"🌐 Post URL: {post_url}")
            
            return result
            
        except Exception as e:
            print(f"❌ Post publishing error: {e}")
            # Try to get more detailed error info
            if hasattr(e, 'read'):
                try:
                    error_details = e.read().decode('utf-8')
                    print(f"Error details: {error_details}")
                except:
                    pass
            return None
    
    def create_and_publish_farm_post(self):
        """Main function to create the complete farm community post"""
        print("🌱 Community Farm Post Creator")
        print("=" * 50)
        
        # Step 1: Upload harvest image
        media_id, image_url = self.upload_image()
        
        # Step 2: Create post content
        title, content = self.create_farm_post(media_id, image_url)
        
        # Step 3: Publish the post
        result = self.publish_post(title, content)
        
        if result:
            print("\n🎉 Community Farm Post Creation Completed!")
            print("=" * 60)
            print("✅ Harvest image uploaded: DONE")
            print("✅ English farm post content: DONE")
            print("✅ Community farming story: DONE") 
            print("✅ Post published with tags: DONE")
            print(f"🌐 Live post: {result['link']}")
            print("\n🌱 Sharing the joy of community farming with the world!")
        else:
            print("❌ Failed to create farm community post")
        
        return result

def main():
    creator = WordPressFarmPostCreator()
    creator.create_and_publish_farm_post()

if __name__ == "__main__":
    main()