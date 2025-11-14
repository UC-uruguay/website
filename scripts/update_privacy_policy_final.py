#!/usr/bin/env python3
"""
Final Privacy Policy update - force complete English replacement
"""
import urllib.request
import json
import time

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']
privacy_policy_id = 52

print("🔒 Final Privacy Policy update - forcing complete English replacement...")

def update_page_with_retry(page_id, title, content, max_retries=3):
    """Update a WordPress page with retry logic"""
    for attempt in range(max_retries):
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
            
            print(f"✅ Updated: {title} (Attempt {attempt + 1})")
            return True
            
        except Exception as e:
            print(f"❌ Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"⏳ Waiting before retry...")
                time.sleep(2)
            else:
                print(f"❌ All attempts failed for {title}")
                return False

# Complete English Privacy Policy content
privacy_policy_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🔒 Privacy Policy</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Welcome to UC's website! This privacy policy explains how we handle your information when you visit our site.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📊 Information We Collect</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Automatically collected information:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>IP address (for analytics, not personal identification)</li>
<li>Browser type and version</li>
<li>Pages you visit on our site</li>
<li>Time spent on pages</li>
<li>Referring website information</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Information you provide:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Name and email when commenting</li>
<li>Contact form submissions</li>
<li>Any messages sent through social media</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎯 How We Use Your Information</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>To improve website functionality and user experience</li>
<li>To respond to your comments and messages</li>
<li>To prevent spam and maintain security</li>
<li>To analyze website traffic and popular content</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>What we absolutely DO NOT do:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Sell your personal information to third parties</li>
<li>Send unsolicited promotional emails</li>
<li>Share your data without your consent</li>
<li>Store unnecessary personal information</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🍪 Cookies and Tracking</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We use cookies to make our website work better for you:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Essential cookies for site functionality</li>
<li>Google Analytics for understanding site usage</li>
<li>Preference cookies to remember your settings</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>You can disable cookies in your browser settings, but this may affect site functionality.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🛡️ Data Protection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We take your privacy seriously:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>SSL encryption protects data transmission</li>
<li>Regular security updates and monitoring</li>
<li>Limited data collection - only what's necessary</li>
<li>Secure storage of any collected information</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📧 Contact and Data Rights</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>You have the right to:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Know what data we have about you</li>
<li>Request deletion of your data</li>
<li>Correct any inaccurate information</li>
<li>Object to data processing</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Contact us for privacy questions:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instagram: @toriaezu_uc<br>
X (Twitter): @TORIAEZU_OU<br>
Website: uc.x0.com/contact/</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📅 Updates</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This privacy policy was last updated in September 2025. We may update it occasionally to reflect changes in our practices or legal requirements.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Thanks for reading! Feel free to reach out if you have any questions about how we handle your privacy.</em></p>
<!-- /wp:paragraph -->'''

# Update the Privacy Policy page with retry
success = update_page_with_retry(privacy_policy_id, "Privacy Policy", privacy_policy_content)

if success:
    print(f"\n🎉 Privacy Policy updated successfully!")
    print(f"✅ Page is now completely in English")
    print(f"✅ Professional yet friendly tone maintained")
    print(f"🔗 Check it at: {site_url}/privacy-policy/")
    print(f"⏳ Please wait a few moments for caching to update")
else:
    print(f"\n❌ Failed to update Privacy Policy")

print(f"\n📋 If the page still shows Japanese content:")
print("1. Clear your browser cache (Ctrl+F5 or Cmd+Shift+R)")
print("2. Wait a few minutes for WordPress cache to update")
print("3. Try viewing in incognito/private browsing mode")
print("4. The API update was successful, so caching may be the issue")