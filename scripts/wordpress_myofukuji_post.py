#!/usr/bin/env python3
"""
WordPress Myofukuji Temple Post Creator
Create a new post about the temple completion ceremony experience
"""
import urllib.request
import json

class WordPressMyofukujiPostCreator:
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
    
    def create_temple_post(self):
        """Create the temple completion ceremony post"""
        
        # Post content in English
        title = "🏛️ Attending Myofukuji Temple's Completion Ceremony - A Meaningful Celebration"
        
        content = '''<!-- wp:paragraph -->
<p>Just returned from an incredibly meaningful experience at Myofukuji Temple's completion ceremony (落慶式)! What a beautiful celebration of spiritual renewal and community gathering. ✨</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🙏 A Special Connection</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This event was especially significant for me because it was held at the temple of Reverend Kondo, who has always been incredibly supportive and kind to me. Since moving to Yamanashi, I've had the privilege of working with <strong>ShareWing</strong>, a company that operates temple lodging businesses through <a href="https://oterastay.com" target="_blank">oterastay.com</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Through this work in the temple hospitality industry, I had the wonderful opportunity to meet Reverend Kondo, who is actively involved in the <strong>Social Temple</strong> movement. His vision of making temples more accessible and relevant to modern communities has been truly inspiring to witness.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🏮 Temple Lodging & Cultural Preservation</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Working with ShareWing has given me deep insights into how traditional Japanese temples are adapting to serve both spiritual and cultural purposes in the 21st century. Through <strong>oterastay.com</strong>, we help connect travelers and spiritual seekers with authentic temple experiences - from meditation retreats to cultural immersion programs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It's fascinating to see how temples like Myofukuji are not just preserving ancient traditions, but actively creating new ways to share Buddhist wisdom and Japanese culture with both local communities and international visitors.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🎉 The Completion Ceremony Experience</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The ceremony itself was deeply moving - a perfect blend of solemn Buddhist rituals and joyful community celebration. The newly completed temple structures were beautiful, and you could feel the sense of accomplishment and spiritual renewal throughout the entire gathering.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What made the day even more special was the reception afterwards. I had amazing conversations with so many different people - fellow temple enthusiasts, local community members, and others involved in preserving and modernizing Japanese spiritual traditions.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
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

<!-- wp:heading {"level":3} -->
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

<!-- wp:paragraph {"style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#666666"}}} -->
<p style="color:#666666;font-size:0.9rem"><em>Have you ever experienced a Japanese temple ceremony? Or maybe you have your own funny story about mixing up belongings at a celebration? Share your experiences in the comments!</em></p>
<!-- /wp:paragraph -->'''
        
        return title, content
    
    def publish_post(self, title, content):
        """Publish the temple ceremony post"""
        try:
            print("🏛️ Creating and publishing temple ceremony post...")
            
            post_data = {
                "title": title,
                "content": content,
                "status": "publish",
                "excerpt": "Attended Myofukuji Temple's completion ceremony with Reverend Kondo, who I know through my work at ShareWing (oterastay.com). Great conversations, spiritual renewal, and a funny jacket mix-up!"
            }
            
            data = json.dumps(post_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/posts", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            post_id = result['id']
            post_url = result['link']
            
            print(f"✅ Temple ceremony post published successfully!")
            print(f"📰 Post ID: {post_id}")
            print(f"🌐 Post URL: {post_url}")
            
            return result
            
        except Exception as e:
            print(f"❌ Post publishing error: {e}")
            if hasattr(e, 'read'):
                try:
                    error_details = e.read().decode('utf-8')
                    print(f"Error details: {error_details}")
                except:
                    pass
            return None
    
    def create_and_publish_temple_post(self):
        """Main function to create the complete temple ceremony post"""
        print("🏛️ Myofukuji Temple Ceremony Post Creator")
        print("=" * 50)
        
        # Step 1: Create post content
        title, content = self.create_temple_post()
        
        # Step 2: Publish the post
        result = self.publish_post(title, content)
        
        if result:
            print("\n🎉 Temple Ceremony Post Creation Completed!")
            print("=" * 60)
            print("✅ Myofukuji temple experience: DONE")
            print("✅ Reverend Kondo & Social Temple context: DONE")
            print("✅ ShareWing & oterastay.com background: DONE") 
            print("✅ Reception & jacket mix-up story: DONE")
            print(f"🌐 Live post: {result['link']}")
            print("\n🏛️ Sharing the beauty of temple community experiences!")
        else:
            print("❌ Failed to create temple ceremony post")
        
        return result

def main():
    creator = WordPressMyofukujiPostCreator()
    creator.create_and_publish_temple_post()

if __name__ == "__main__":
    main()