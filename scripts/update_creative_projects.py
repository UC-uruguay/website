#!/usr/bin/env python3
"""
Update AI Creative Projects to Creative Projects and create NFT project page
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
home_page_id = 11

print("🎨 Updating AI Creative Projects to Creative Projects...")

def update_page(page_id, title, content):
    """Update a WordPress page"""
    try:
        page_data = {
            "title": title,
            "content": content,
            "status": "publish"
        }
        
        data = json.dumps(page_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{page_id}", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.get_method = lambda: 'POST'
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"✅ Updated: {title}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {title}: {e}")
        return False

def create_page(title, content, slug):
    """Create a new WordPress page"""
    try:
        page_data = {
            "title": title,
            "content": content,
            "slug": slug,
            "status": "publish"
        }
        
        data = json.dumps(page_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        page_id = result.get('id')
        print(f"✅ Created: {title} (ID: {page_id})")
        return page_id
        
    except Exception as e:
        print(f"❌ Error creating {title}: {e}")
        return None

# First get current home page content
try:
    request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages/{home_page_id}")
    request.add_header('Authorization', f'Basic {token}')
    
    with urllib.request.urlopen(request) as response:
        home_data = json.loads(response.read().decode('utf-8'))
    
    current_content = home_data.get('content', {}).get('rendered', '')
    current_title = home_data.get('title', {}).get('rendered', '')
    
    # Replace AI Creative Projects with Creative Projects and add link
    updated_content = current_content.replace(
        'AI Creative Projects', 
        '<a href="/creative-projects/">Creative Projects</a>'
    )
    
    # Update home page
    if update_page(home_page_id, current_title, updated_content):
        print("✅ Home page updated - AI Creative Projects changed to Creative Projects with link")
    
except Exception as e:
    print(f"❌ Error getting home page: {e}")

# Create Creative Projects page content
creative_projects_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🎨 Creative Projects</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Welcome to my creative world! Here are some unique projects I've been working on.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💩 Kawaii Poops NFT Collection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>An unusual but fascinating 30-day experiment that turned into an NFT collection!</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🔍 The Project</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For 30 consecutive days, I observed and documented my daily "output" with scientific precision. Each poop was evaluated like a Pokemon card, rating various attributes:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li><strong>Firmness Level</strong> - From soft serve to concrete</li>
<li><strong>Aroma Intensity</strong> - Scientific smell assessment</li>
<li><strong>Color Variation</strong> - The full spectrum analysis</li>
<li><strong>Shape & Form</strong> - Artistic composition evaluation</li>
<li><strong>Overall Rating</strong> - The comprehensive poop score</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🎴 NFT Collection</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Each day's observation became a unique NFT card with cute kawaii-style artwork. The collection features 30 unique poops, each with their own personality and stats!</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons">
<div class="wp-block-button">
<a class="wp-block-button__link wp-element-button" href="https://opensea.io/collection/kawaii-poops" target="_blank" rel="noopener">🌊 View on OpenSea</a>
</div>
</div>
<!-- /wp:buttons -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">📚 The Observation Diary</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The complete 30-day journey is documented in my Kindle book - a detailed diary of this unique experiment with daily observations, scientific analysis, and plenty of humor!</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons">
<div class="wp-block-button">
<a class="wp-block-button__link wp-element-button" href="https://amzn.asia/d/hGdV7rG" target="_blank" rel="noopener">📖 Read the Kindle Book</a>
</div>
</div>
<!-- /wp:buttons -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">🤔 Why This Project?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Sometimes the most mundane daily activities can become art when observed with curiosity and documented with care. This project explores:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>The intersection of art and daily life</li>
<li>Scientific observation of personal health</li>
<li>Transforming taboo topics into kawaii art</li>
<li>The potential of NFTs for unconventional content</li>
<li>Humor as a bridge to serious topics</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><em>Warning: This project contains mature themes presented in a lighthearted, artistic way. Not suitable for those easily offended by bathroom humor!</em></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🚀 More Projects Coming Soon</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Stay tuned for more creative experiments and unconventional projects. Art is everywhere if you know where to look!</p>
<!-- /wp:paragraph -->'''

# Create the Creative Projects page
creative_page_id = create_page("Creative Projects", creative_projects_content, "creative-projects")

if creative_page_id:
    print(f"\n🎉 Creative Projects setup completed!")
    print(f"✅ Changed 'AI Creative Projects' to 'Creative Projects' on home page")
    print(f"✅ Created new Creative Projects page with NFT collection info")
    print(f"✅ Added links to OpenSea collection and Kindle book")
    print(f"🔗 New page: {site_url}/creative-projects/")
    print(f"🔗 NFT Collection: https://opensea.io/collection/kawaii-poops")
    print(f"🔗 Kindle Book: https://amzn.asia/d/hGdV7rG")
else:
    print("\n❌ Failed to create Creative Projects page")

print(f"\n📋 Project Features:")
print("• 30-day poop observation experiment")
print("• Pokemon card-style rating system")
print("• Kawaii NFT artwork collection")
print("• Detailed observation diary in Kindle format")
print("• Links to both OpenSea and Amazon")