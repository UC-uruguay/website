#!/usr/bin/env python3
"""
Update all footer pages to English (permanent site rule)
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🌐 Converting all pages to English (permanent site rule)...")

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
        
        print(f"✅ Updated: {title} (ID: {page_id})")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {title}: {e}")
        return False

# Team Page (ID: 49)
team_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🏠 Team UC (Well, It's Just My Family)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Team? You might be wondering... Well, since this is my personal site, the "team" is basically just my family. But hey, we're the best team ever! 👨‍👩‍👦</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👨 UC (Yushi) - CEO (Chief Everything Officer)</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Real name: Yushi Nakashima<br>
Position: Jack of all trades<br>
Special skills: Endlessly talking about how cute my wife and son are, burying time capsules around the world<br>
Weaknesses: Can't resist wine, makes too many friends</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👩 My Wife - CFO (Chief Fun Officer)</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Position: Family sunshine<br>
Special skills: Bringing UC back to reality, keeping up with our son's energy<br>
Favorite comment: "Did you bury another time capsule?"</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👶 Ichiyu (Ichikun) - CPO (Chief Play Officer)</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Age: Young toddler<br>
Position: Chief Play Officer<br>
Special skills: Making mama and papa smile, exploring the house with endless curiosity<br>
Motto: "Why? Why? Why?"</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 Team Philosophy</h2>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote">
<p>"Connect with the world through smiles and curiosity"</p>
<cite>— From the UC Family Charter</cite>
</blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>It's small but full of love. Sometimes chaotic, but that's what makes it perfect!</p>
<!-- /wp:paragraph -->'''

# History Page (ID: 50)
history_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📚 UC's Mysterious History</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Looking back at my life, it's been quite chaotic and fun! Let me put it in chronological order.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🍼 Early Childhood (Early 1990s)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Born in Yamanashi Prefecture. Already called "a bit unusual" at this age</li>
<li>Started making friends. Activated "let's all be friends!" spirit in kindergarten</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📚 School Days (Late 1990s - Early 2010s)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Focused on making friends instead of studying</li>
<li>Developed "want to do something interesting" syndrome</li>
<li>University days: Spent youth discussing philosophy and life meaning late into the night</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💼 Social Debut (2010s)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Gradually realized "normal office work might not be for me"</li>
<li>Got hooked on traveling. Started aiming to visit all 47 prefectures</li>
<li>Fateful encounter with wine. "This enriches life!"</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💕 Fateful Encounter (Late 2010s)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Met my current wife. "This person might accept my weirdness"</li>
<li>Buried a time capsule when proposing. Romantic or weird? Hard to say</li>
<li>Got married. Wife: "You're definitely weird, but that's what's good about you"</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👶 Becoming a Dad (Early 2020s)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Ichikun was born. Full-speed ahead on the doting parent highway</li>
<li>Developed mysterious sense of mission: "I want to make the world more interesting for my son"</li>
<li>Got hooked on AI technology. "I can make educational games for my son with this!"</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌐 Present (2025)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Launched this site. Currently realizing my "want to be friends with people worldwide" desire</li>
<li>Time capsule collection: About 40 buried worldwide so far</li>
<li>Still continuing to make friends. Goal: "Make friends around the world"</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🔮 Future Ambitions</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Achieve worldwide mutual understanding beyond religion (too ambitious?)</li>
<li>The day I dig up time capsules with my son</li>
<li>Want to create a Ghibli-like café (shared dream with my wife)</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Living an unconventional life like this, but enjoying every day!</p>
<!-- /wp:paragraph -->'''

# Careers Page (ID: 51)
careers_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">💼 Want to Work Together? (Job Openings)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Job openings on a personal site? Yes, I wrote one anyway. But if someone seriously wants to do something together, I'd be thrilled!</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 Currently Recruiting</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">1. Friends (Full-time/Part-time Welcome)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Job Description:</strong><br>
• Laughing together<br>
• Planning fun things<br>
• Talking about life over wine<br>
• Occasionally going to bury time capsules</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Qualifications:</strong><br>
• People who want to enjoy life<br>
• People who find unusual ideas interesting<br>
• People who listen to kid stories and say "how cute"</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Benefits:</strong><br>
• Salary: Smiles and friendship (priceless)<br>
• Benefits: Sharing good wine information<br>
• Promotion: Can advance to best friend</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">2. Creative Partner (Contract)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Job Description:</strong><br>
• AI music production consultation<br>
• Brainstorming educational games for my son<br>
• Short film production assistance</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Qualifications:</strong><br>
• People confident in creativity<br>
• People whose catchphrase is "That sounds interesting!"<br>
• Passion over technique</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">3. Travel Companion (Irregular)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Job Description:</strong><br>
• Hot spring tour companion<br>
• Temple visit attendant<br>
• Time capsule burial witness</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Qualifications:</strong><br>
• Curious people<br>
• People OK with family trips (sometimes Ichikun comes too)<br>
• People who won't ask "Why are you burying a time capsule there?"</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📝 How to Apply</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>No resume needed! Feel free to contact me in any of these ways:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>DM on Instagram @toriaezu_uc</li>
<li>Reply on X (Twitter) @TORIAEZU_OU</li>
<li>Say "I saw the job posting" when we actually meet</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Note:</strong><br>
This is half joke, half serious. But people who really want to do something fun together are very welcome!</p>
<!-- /wp:paragraph -->'''

# Privacy Policy (ID: 52)
privacy_content = '''<!-- wp:heading {"level":1} -->
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

# Terms and Conditions (ID: 53)
terms_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📜 Terms and Conditions (Tried to Write Formally)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Well, it's a personal site so I don't think we need strict terms, but I'll write them anyway. Basically, "let's all have fun together!"</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎯 How to Use This Site</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>OK:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Reading articles and enjoying them</li>
<li>Looking at photos and thinking "nice!"</li>
<li>Sharing your thoughts in comments</li>
<li>Sharing on social media (makes me super happy!)</li>
<li>Introducing friends saying "there's an interesting site"</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Not OK:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Harassment (let's all have fun)</li>
<li>Spam comments (annoying)</li>
<li>Unauthorized content reproduction (just ask and it's OK)</li>
<li>Actions that bother others</li>
<li>Weird product advertising (no thanks)</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📝 About Comments</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Basically welcome anything! Impressions, questions, chit-chat, anything goes</li>
<li>But comments that make others feel bad are not OK</li>
<li>I might delete comments if I think "this is a bit..."</li>
<li>I try to reply but might be late (sorry)</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📷 About Photos and Videos</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Basically things I photographed or got permission for</li>
<li>Family photos are included but I'm careful about privacy</li>
<li>If there's anything like "don't use this photo," please let me know</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🔗 About Links</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Linking to this site:</strong><br>
Very welcome! No advance notice needed. Please introduce it lots!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>External links from this site:</strong><br>
Sometimes I link to interesting or helpful sites. But I can't take responsibility for the linked content.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">⚠️ Disclaimer (Writing It Just in Case)</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>I try to write information accurately, but sorry if there are mistakes</li>
<li>I can't take responsibility for any damage from site content (it's a personal site)</li>
<li>I might change content without notice</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🤝 In the End...</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Let's put aside the difficult stuff and all have fun together!</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>If you have consideration for others, it'll be fine</li>
<li>Feel free to ask if you don't understand something</li>
<li>Let's create interesting things together</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>If you have any questions:</strong><br>
Instagram: @toriaezu_uc<br>
X(Twitter): @TORIAEZU_OU</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Thanks for reading to the end! Let's make this a fun site together~</em></p>
<!-- /wp:paragraph -->'''

# Contact Us (ID: 54)
contact_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📮 Contact (Feel Free to Reach Out!)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you have something to talk about, ask, or want to do together, don't hesitate to contact me! I love meeting new people, so any kind of message makes me happy.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 Fastest Response Here</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"left"}} -->
<ul class="wp-block-social-links has-visible-labels is-style-logos-only">
<!-- wp:social-link {"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor">Instagram</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:paragraph -->
<p><strong>@toriaezu_uc</strong><br>
I post daily life photos and cute moments with my son. I'd be happy if you DM me!</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"left"}} -->
<ul class="wp-block-social-links has-visible-labels is-style-logos-only">
<!-- wp:social-link {"url":"https://x.com/TORIAEZU_OU","service":"x"} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor">X (Twitter)</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:paragraph -->
<p><strong>@TORIAEZU_OU</strong><br>
I tweet random thoughts. Looking forward to replies and DMs!</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📱 Other Social Media</h2>
<!-- /wp:heading -->

<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"layout":{"type":"flex","justifyContent":"left","flexWrap":"wrap"}} -->
<ul class="wp-block-social-links has-visible-labels">
<!-- wp:social-link {"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor">Facebook</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor">TikTok</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor">LinkedIn</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💬 These Messages Are Very Welcome</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>📝 "I read your blog!"</li>
<li>🍷 "Tell me about wine"</li>
<li>🎨 "Let's do something creative together"</li>
<li>🌏 "I'm going to your area, can you show me around?"</li>
<li>👶 "Let's talk about parenting"</li>
<li>🏛️ "Recommend some temples"</li>
<li>💭 "Let's discuss life"</li>
<li>🤝 "I want to be friends"</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">⏰ About Responses</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>I try to respond within 24 hours! But,</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Sometimes I'm late because I'm playing with my son</li>
<li>Sometimes I go to hot springs and lose signal</li>
<li>Sometimes I drink too much wine and fall asleep (sorry)</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>But I always respond eventually, so please be patient!</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎯 Special Invitation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you ever come to Yamanashi, please let me know!</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>🍇 I'll take you on a winery tour</li>
<li>♨️ I'll show you hidden hot spring spots</li>
<li>🏛️ I'll guide you to recommended temples</li>
<li>👨‍👩‍👦 If you'd like, let's meet with my family</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>Finally:</strong><br>
I'm not shy and welcome anyone regardless of age or nationality. Let's do something fun together!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>Looking forward to hearing from you~!</em> 🌟</p>
<!-- /wp:paragraph -->'''

# Update all pages
pages_to_update = [
    (49, "Team", team_content),
    (50, "History", history_content), 
    (51, "Careers", careers_content),
    (52, "Privacy Policy", privacy_content),
    (53, "Terms and Conditions", terms_content),
    (54, "Contact Us", contact_content)
]

print("🔄 Updating all pages to English...")
success_count = 0

for page_id, title, content in pages_to_update:
    if update_page(page_id, title, content):
        success_count += 1

print(f"\n🎉 Successfully updated {success_count}/{len(pages_to_update)} pages!")
print("\n📋 Updated pages:")
for page_id, title, _ in pages_to_update:
    print(f"  - {title}: https://uc.x0.com/{title.lower().replace(' ', '-').replace('&', '').replace('  ', '-')}/")

print("\n💡 All pages now follow the permanent English-only rule!")
print("✅ Age information updated to avoid frequent updates")
print("📝 Content maintains UC's fun, personal tone in English")