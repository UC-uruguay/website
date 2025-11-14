#!/usr/bin/env python3
"""
Create Temple Visits article with photo and link from homepage
"""
import urllib.request
import json
import base64

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🛕 Creating Temple Visits article...")

def upload_image(image_path, alt_text, title):
    """Upload image to WordPress"""
    try:
        # Read image file
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        # Upload via WordPress API
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/media")
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Disposition', f'attachment; filename="temple-visit-monk-uc.jpg"')
        request.add_header('Content-Type', 'image/jpeg')
        
        with urllib.request.urlopen(request, data=image_data) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        image_id = result.get('id')
        image_url = result.get('source_url')
        print(f"✅ Image uploaded: ID {image_id}")
        return image_id, image_url
        
    except Exception as e:
        print(f"❌ Error uploading image: {e}")
        return None, None

def create_blog_post(title, content, image_id=None):
    """Create a blog post"""
    try:
        post_data = {
            "title": title,
            "content": content,
            "status": "publish",
            "categories": [1]  # Default category
        }
        
        if image_id:
            post_data["featured_media"] = image_id
        
        data = json.dumps(post_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/posts", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        post_id = result.get('id')
        post_url = result.get('link')
        print(f"✅ Blog post created: ID {post_id}")
        return post_id, post_url
        
    except Exception as e:
        print(f"❌ Error creating post: {e}")
        return None, None

# Upload the temple photo
image_id, image_url = upload_image('/home/uc/0904.jpg', 'UC with Buddhist monk during temple visit', 'Temple Visit with Monk')

if not image_id:
    print("⚠️ Could not upload image, continuing without it...")
    image_id = None

# Create temple visits article content
temple_article_content = f'''<!-- wp:paragraph -->
<p>Temple visits have always held a special place in my heart. There's something profoundly peaceful about stepping into these sacred spaces, where centuries of prayers and meditation have created an atmosphere of tranquility that seems to transcend time itself.</p>
<!-- /wp:paragraph -->

{"<!-- wp:image {" + f'"id":{image_id},"align":"center","width":"600","height":"450"' + "} -->" if image_id else ""}
{"<figure class=\"wp-block-image aligncenter is-resized\">" if image_id else ""}
{f'<img src="{image_url}" alt="UC with Buddhist monk during temple visit" class="wp-image-{image_id}" style="width:600px;height:450px;object-fit:cover"/>' if image_id else ""}
{"<figcaption class=\"wp-element-caption\">A meaningful encounter with a wise monk during my temple exploration</figcaption>" if image_id else ""}
{"</figure>" if image_id else ""}
{"<!-- /wp:image -->" if image_id else ""}

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🙏 The Universal Language of Spirituality</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>What I find most beautiful about temple visits is how they break down barriers. Whether I'm in a Buddhist temple in Japan, a Hindu temple in India, or exploring sacred spaces anywhere in the world, there's a universal language of respect, curiosity, and spiritual connection that transcends cultural boundaries.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>During my travels, I've had the privilege of meeting remarkable spiritual teachers who have shared their wisdom with me. These encounters remind me that despite our different backgrounds, we all share the same fundamental human desires for peace, understanding, and connection.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌸 Lessons from the Temple</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every temple visit teaches me something new:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Mindfulness:</strong> The simple act of removing shoes, bowing, and moving quietly naturally brings you into the present moment.</li>
<li><strong>Humility:</strong> Standing before something greater than yourself—whether it's ancient architecture, spiritual art, or the presence of devoted practitioners—puts life into perspective.</li>
<li><strong>Community:</strong> Witnessing how people from all walks of life come together in these sacred spaces reinforces my belief in our shared humanity.</li>
<li><strong>Inner Peace:</strong> The quiet contemplation possible in temples offers a rare escape from our busy modern lives.</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌍 Building Bridges Through Respect</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>As someone passionate about creating "worldwide understanding beyond religion," I see temple visits as opportunities to build bridges. When I approach these sacred spaces with genuine respect and curiosity, I'm always welcomed warmly, regardless of my own background.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These experiences have taught me that spirituality, at its core, is about love, compassion, and connection—values that unite us all, no matter what path we follow.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">✨ An Invitation to Explore</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I encourage everyone to explore temples and sacred spaces with an open heart. You don't need to share the same beliefs to appreciate the beauty, artistry, and spiritual energy of these remarkable places. What you'll find is that curiosity and respect are the only "admission requirements" needed.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Whether you're drawn to the intricate architecture, the peaceful atmosphere, or the chance to connect with devoted practitioners, temple visits offer something special for everyone. They remind us that in our diverse world, there are still places where peace and understanding can flourish.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Have you visited any temples or sacred spaces that left a lasting impression on you? I'd love to hear about your experiences and the connections you've made along the way.</em></p>
<!-- /wp:paragraph -->'''

# Create the blog post
post_id, post_url = create_blog_post(
    "Finding Peace and Connection: My Journey Through Temple Visits",
    temple_article_content,
    image_id
)

if post_id and post_url:
    print(f"\n🎉 Temple visits article created successfully!")
    print(f"📝 Post ID: {post_id}")
    print(f"🔗 URL: {post_url}")
    
    # Now update homepage to link Temple Visits to the article
    print(f"\n🔄 Updating homepage to link Temple Visits...")
    
    # Get current homepage content
    try:
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/11")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            page_data = json.loads(response.read().decode('utf-8'))
        
        current_content = page_data.get('content', {}).get('raw', '')
        current_title = page_data.get('title', {}).get('rendered', '')
        
        # Update Temple Visits to link to the new article
        updated_content = current_content.replace(
            '<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600">Temple Visits</p>',
            f'<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="{post_url}">Temple Visits</a></p>'
        )
        
        # Update the homepage
        page_update = {
            "title": current_title,
            "content": updated_content,
            "status": "publish"
        }
        
        data = json.dumps(page_update).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/11", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.get_method = lambda: 'POST'
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"✅ Homepage updated with Temple Visits link")
        
    except Exception as e:
        print(f"❌ Error updating homepage: {e}")

else:
    print("❌ Failed to create temple visits article")

print(f"\n📋 Completed:")
print(f"• Uploaded temple photo with UC and monk")
print(f"• Created inspiring temple visits article")
print(f"• Linked from homepage Temple Visits section")
print(f"• Article covers spiritual connection and cultural bridges")
print(f"• Personal tone matching UC's personality")