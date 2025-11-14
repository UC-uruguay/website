#!/usr/bin/env python3
"""
WordPress Update Temple Post with Image
Add the temple photo to the existing Myofukuji post
"""
import urllib.request
import json
import mimetypes
import os

class WordPressTemplePostUpdater:
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
        self.image_path = "/home/uc/20250831.jpg"
        self.post_id = 22  # The post ID from the previous creation
    
    def upload_temple_image(self):
        """Upload the temple image to WordPress media library"""
        try:
            print("🏛️ Uploading temple building image...")
            
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
            print(f"✅ Temple image uploaded successfully (ID: {media_id})")
            
            return media_id, image_url
            
        except Exception as e:
            print(f"❌ Image upload error: {e}")
            return None, None
    
    def update_post_with_image(self, media_id, image_url):
        """Update the existing post to include the temple image"""
        
        # Updated content with image at the top
        updated_content = f'''<!-- wp:image {{"id":{media_id},"align":"center","className":"temple-photo"}} -->
<div class="wp-block-image temple-photo">
<figure class="aligncenter">
<img src="{image_url}" alt="Beautiful newly completed Myofukuji Temple building with modern architecture and traditional elements" class="wp-image-{media_id}"/>
<figcaption class="wp-element-caption">The beautiful newly completed Myofukuji Temple - a perfect blend of modern design and traditional Japanese temple architecture</figcaption>
</figure>
</div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Just returned from an incredibly meaningful experience at Myofukuji Temple's completion ceremony (落慶式)! What a beautiful celebration of spiritual renewal and community gathering. ✨</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">🙏 A Special Connection</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This event was especially significant for me because it was held at the temple of Reverend Kondo, who has always been incredibly supportive and kind to me. Since moving to Yamanashi, I've had the privilege of working with <strong>ShareWing</strong>, a company that operates temple lodging businesses through <a href="https://oterastay.com" target="_blank">oterastay.com</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Through this work in the temple hospitality industry, I had the wonderful opportunity to meet Reverend Kondo, who is actively involved in the <strong>Social Temple</strong> movement. His vision of making temples more accessible and relevant to modern communities has been truly inspiring to witness.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">🏮 Temple Lodging & Cultural Preservation</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Working with ShareWing has given me deep insights into how traditional Japanese temples are adapting to serve both spiritual and cultural purposes in the 21st century. Through <strong>oterastay.com</strong>, we help connect travelers and spiritual seekers with authentic temple experiences - from meditation retreats to cultural immersion programs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's fascinating to see how temples like Myofukuji are not just preserving ancient traditions, but actively creating new ways to share Buddhist wisdom and Japanese culture with both local communities and international visitors.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">🎉 The Completion Ceremony Experience</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The ceremony itself was deeply moving - a perfect blend of solemn Buddhist rituals and joyful community celebration. The newly completed temple structures were beautiful, and you could feel the sense of accomplishment and spiritual renewal throughout the entire gathering.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What made the day even more special was the reception afterwards. I had amazing conversations with so many different people - fellow temple enthusiasts, local community members, and others involved in preserving and modernizing Japanese spiritual traditions.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">😅 A Funny Ending to a Perfect Day</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I have to share this amusing ending to what was otherwise a perfectly meaningful day: I may have gotten a bit too enthusiastic during the reception celebrations, and somehow managed to accidentally take home someone else's jacket! 🧥</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's a classic case of having such a wonderful time connecting with everyone that I lost track of the small details. I'm definitely going to return it, but it's a funny reminder of how genuinely enjoyable the whole experience was!</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote">
<p>"In the spirit of community and connection that temples foster, sometimes we accidentally take a piece of that warmth home with us - even if it's in the form of the wrong jacket!"</p>
</blockquote>
<!-- /wp:quote -->

<!-- wp:heading {{"level":3}} -->
<h3 class="wp-block-heading">🌸 Gratitude & Reflection</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This experience reinforced my appreciation for the work we do at ShareWing and the vision that leaders like Reverend Kondo bring to modernizing temple communities. The combination of preserving sacred traditions while creating meaningful connections in contemporary society is truly special.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Events like Myofukuji's completion ceremony show how temples continue to serve as vital community centers - places where people can gather, reflect, celebrate, and build lasting friendships across all walks of life.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Thank you, Reverend Kondo, for your continued kindness and for creating such beautiful opportunities for connection and growth. And sorry about the jacket mix-up! 😊</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {{"style":{{"typography":{{"fontSize":"0.9rem"}},"color":{{"text":"#666666"}}}}}} -->
<p style="color:#666666;font-size:0.9rem"><em>Have you ever experienced a Japanese temple ceremony? Or maybe you have your own funny story about mixing up belongings at a celebration? Share your experiences in the comments!</em></p>
<!-- /wp:paragraph -->'''
        
        return updated_content
    
    def update_existing_post(self, updated_content):
        """Update the existing WordPress post"""
        try:
            print("📝 Updating temple post with image...")
            
            post_data = {
                "content": updated_content
            }
            
            data = json.dumps(post_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/posts/{self.post_id}", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            request.get_method = lambda: 'POST'  # Use POST for update
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            post_url = result['link']
            print(f"✅ Temple post updated successfully!")
            print(f"🌐 Updated post URL: {post_url}")
            
            return result
            
        except Exception as e:
            print(f"❌ Post update error: {e}")
            if hasattr(e, 'read'):
                try:
                    error_details = e.read().decode('utf-8')
                    print(f"Error details: {error_details}")
                except:
                    pass
            return None
    
    def add_image_to_temple_post(self):
        """Main function to add image to the temple post"""
        print("🏛️ Temple Post Image Updater")
        print("=" * 50)
        
        # Step 1: Upload temple image
        media_id, image_url = self.upload_temple_image()
        
        if not media_id:
            print("❌ Failed to upload image")
            return False
        
        # Step 2: Create updated content with image
        updated_content = self.update_post_with_image(media_id, image_url)
        
        # Step 3: Update the existing post
        result = self.update_existing_post(updated_content)
        
        if result:
            print("\n🎉 Temple Post Image Update Completed!")
            print("=" * 60)
            print("✅ Temple building image uploaded: DONE")
            print("✅ Post content updated with image: DONE")
            print(f"🌐 Updated post: {result['link']}")
            print("\n🏛️ Beautiful temple photo now featured in the post!")
        else:
            print("❌ Failed to update temple post with image")
        
        return result

def main():
    updater = WordPressTemplePostUpdater()
    updater.add_image_to_temple_post()

if __name__ == "__main__":
    main()