#!/usr/bin/env python3
"""
Fix Privacy Policy page - ensure it's completely in English
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
privacy_policy_id = 52

print("🔒 Fixing Privacy Policy page - converting to complete English...")

def update_page(page_id, title, content):
    """Update a WordPress page"""
    try:
        page_data = {
            "title": title,
            "content": content
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

# Complete English Privacy Policy content
privacy_policy_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🔒 Privacy Policy (I Wrote This Seriously)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I'm usually joking around, but I think seriously about privacy. Please enjoy the site with peace of mind!</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📊 What Information Do We Collect?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Automatically collected information:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>IP address (not to identify individuals)</li>
<li>Browser type (Chrome fan? Firefox fan?)</li>
<li>Access time (midnight visitors, thanks for your hard work!)</li>
<li>Which pages you viewed (blog is popular)</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Information you share with us:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Name and email when you comment</li>
<li>Contact form contents</li>
<li>Information when you message on social media</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🤔 What Do We Use This Information For?</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>To make the site more user-friendly</li>
<li>To reply to your messages</li>
<li>To prevent spam comments</li>
<li>To analyze "this page is popular"</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>What we absolutely won't do:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Sell your information to others (we won't do that!)</li>
<li>Send lots of weird ads</li>
<li>Personal prying</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🍪 About Cookies</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Not the edible cookies! Website cookies.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>We use them to make the site easier to use</li>
<li>We use Google Analytics for access analysis</li>
<li>You can disable them in your browser settings if you don't like them</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🛡️ Information Protection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We handle your information carefully:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Site protected with SSL encryption</li>
<li>Regular security checks</li>
<li>Don't store more information than necessary</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">❓ Questions or Deletion Requests</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Feel free to ask anything like "delete my information" or "what about this?"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Contact:</strong><br>
Instagram: @toriaezu_uc<br>
X(Twitter): @TORIAEZU_OU</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Last Updated:</strong> September 2025 (I update it regularly)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Thanks for reading this policy! Feel free to ask if you have any questions~</em></p>
<!-- /wp:paragraph -->'''

# Update the Privacy Policy page
success = update_page(privacy_policy_id, "Privacy Policy", privacy_policy_content)

if success:
    print(f"\n🎉 Privacy Policy fixed successfully!")
    print(f"✅ Page is now completely in English")
    print(f"✅ Maintains UC's friendly, personal tone")
    print(f"🔗 Check it at: {site_url}/privacy-policy/")
else:
    print(f"\n❌ Failed to update Privacy Policy")

print(f"\n📋 Privacy Policy now includes:")
print("• Information collection explanation")
print("• Cookie usage details") 
print("• Data protection measures")
print("• Contact information for questions")
print("• UC's friendly, approachable tone throughout")

print(f"\n🌐 All footer pages should now be completely English:")
print(f"  - Team: {site_url}/team/")
print(f"  - History: {site_url}/history/")
print(f"  - Careers: {site_url}/careers/")
print(f"  - Privacy Policy: {site_url}/privacy-policy/")
print(f"  - Terms and Conditions: {site_url}/terms-conditions/")
print(f"  - Contact Us: {site_url}/contact/")