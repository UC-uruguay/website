#!/bin/bash

# WordPress credentials
SITE_URL="https://uc.x0.com"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"

# Homepage ID is 11
HOMEPAGE_ID=11

echo "Updating the correct homepage sections..."

# Get the current homepage content and update the "My World" section
# I need to replace "Family Moments" with "人生最高の瞬間" and link to the new page
# I need to replace "Wine Tasting" with "プロダクト" and link to the new page  
# I need to change the grape emoji to package emoji

# Create the updated content with the correct section changes
UPDATE_DATA='{
  "content": "'"$(cat <<'EOF'
<style>
/* Fix Recent Posts thumbnail overflow */
.wp-block-latest-posts__featured-image img {
    width: 100% !important;
    height: auto !important;
    max-width: 100% !important;
    object-fit: cover !important;
    border-radius: 8px !important;
}

.wp-block-latest-posts__featured-image {
    overflow: hidden !important;
    border-radius: 8px !important;
    max-width: 150px !important;
    max-height: 120px !important;
    flex-shrink: 0 !important;
}

.wp-block-latest-posts li {
    overflow: hidden !important;
    margin-bottom: 20px !important;
    display: flex !important;
    align-items: flex-start !important;
    gap: 15px !important;
}

.wp-block-latest-posts__post-title {
    flex: 1 !important;
    margin: 0 !important;
    line-height: 1.4 !important;
}

.wp-block-latest-posts__post-excerpt {
    margin-top: 8px !important;
    color: #666 !important;
    line-height: 1.5 !important;
}

.wp-block-latest-posts__post-date {
    font-size: 0.9rem !important;
    color: #999 !important;
    margin-top: 5px !important;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .wp-block-latest-posts__featured-image {
        max-width: 120px !important;
        max-height: 100px !important;
    }
    
    .wp-block-latest-posts li {
        gap: 12px !important;
    }
}
</style>



<div class="wp-block-group alignfull hero-section has-background is-layout-flow wp-block-group-is-layout-flow" style="background-color:#f8f9fa;padding-top:80px;padding-bottom:80px;padding-left:20px;padding-right:20px">

<div class="wp-block-group is-layout-flow wp-block-group-is-layout-flow">

<h1 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(2.5rem, 5vw, 4rem);font-weight:700">Hi, I'm UC! 👋</h1>



<p class="has-text-align-center" style="color:#34495e;margin-top:20px;font-size:clamp(1.1rem, 2.5vw, 1.4rem);line-height:1.6">Creative soul from Yamanashi, Japan. I love making friends, exploring cultures, and creating meaningful connections worldwide! 🌍</p>

</div>

</div>



<div class="wp-block-group about-me-section has-background is-layout-flow wp-block-group-is-layout-flow" style="background-color:#fafafa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">

<div class="wp-block-columns is-layout-flex wp-container-core-columns-is-layout-28f84493 wp-block-columns-is-layout-flex">

<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow" style="flex-basis:40%">

<figure class="wp-block-image is-resized has-custom-border">
<img loading="lazy" decoding="async" width="719" height="719" src="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg" alt="UC Profile Photo" class="wp-image-10" style="border-radius:50%;object-fit:cover;width:280px;height:280px" srcset="https://uc.x0.com/wp-content/uploads/2025/08/uc-profile.jpg 719w, https://uc.x0.com/wp-content/uploads/2025/08/uc-profile-300x300.jpg 300w, https://uc.x0.com/wp-content/uploads/2025/08/uc-profile-150x150.jpg 150w" sizes="auto, (max-width: 719px) 100vw, 719px" />
</figure>



<h3 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(0.929rem, 0.929rem + ((1vw - 0.2rem) * 0.785), 1.4rem);font-weight:600">Connect with me!</h3>



<ul class="wp-block-social-links is-style-logos-only is-content-justification-center is-layout-flex wp-container-core-social-links-is-layout-c124d1c4 wp-block-social-links-is-layout-flex">
<li class="wp-social-link wp-social-link-instagram  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M12,4.622c2.403,0,2.688,0.009,3.637,0.052c0.877,0.04,1.354,0.187,1.671,0.31c0.42,0.163,0.72,0.358,1.035,0.673 c0.315,0.315,0.51,0.615,0.673,1.035c0.123,0.317,0.27,0.794,0.31,1.671c0.043,0.949,0.052,1.234,0.052,3.637 s-0.009,2.688-0.052,3.637c-0.04,0.877-0.187,1.354-0.31,1.671c-0.163,0.42-0.358,0.72-0.673,1.035 c-0.315,0.315-0.615,0.51-1.035,0.673c-0.317,0.123-0.794,0.27-1.671,0.31c-0.949,0.043-1.233,0.052-3.637,0.052 s-2.688-0.009-3.637-0.052c-0.877-0.04-1.354-0.187-1.671-0.31c-0.42-0.163-0.72-0.358-1.035-0.673 c-0.315-0.315-0.51-0.615-0.673-1.035c-0.123-0.317-0.27-0.794-0.31-1.671C4.631,14.688,4.622,14.403,4.622,12 s0.009-2.688,0.052-3.637c0.04-0.877,0.187-1.354,0.31-1.671c0.163-0.42,0.358-0.72,0.673-1.035 c0.315-0.315,0.615-0.51,1.035-0.673c0.317-0.123,0.794-0.27,1.671-0.31C9.312,4.631,9.597,4.622,12,4.622 M12,3 C9.556,3,9.249,3.01,8.289,3.054C7.331,3.098,6.677,3.25,6.105,3.472C5.513,3.702,5.011,4.01,4.511,4.511 c-0.5,0.5-0.808,1.002-1.038,1.594C3.25,6.677,3.098,7.331,3.054,8.289C3.01,9.249,3,9.556,3,12c0,2.444,0.01,2.751,0.054,3.711 c0.044,0.958,0.196,1.612,0.418,2.185c0.23,0.592,0.538,1.094,1.038,1.594c0.5,0.5,1.002,0.808,1.594,1.038 c0.572,0.222,1.227,0.375,2.185,0.418C9.249,20.99,9.556,21,12,21s2.751-0.01,3.711-0.054c0.958-0.044,1.612-0.196,2.185-0.418 c0.592-0.23,1.094-0.538,1.594-1.038c0.5-0.5,0.808-1.002,1.038-1.594c0.222-0.572,0.375-1.227,0.418-2.185 C20.99,14.751,21,14.444,21,12s-0.01-2.751-0.054-3.711c-0.044-0.958-0.196-1.612-0.418-2.185c-0.23-0.592-0.538-1.094-1.038-1.594 c-0.5-0.5-1.002-0.808-1.594-1.038c-0.572-0.222-1.227-0.375-2.185-0.418C14.751,3.01,14.444,3,12,3L12,3z M12,7.378 c-2.552,0-4.622,2.069-4.622,4.622S9.448,16.622,12,16.622s4.622-2.069,4.622-4.622S14.552,7.378,12,7.378z M12,15 c-1.657,0-3-1.343-3-3s1.343-3,3-3s3,1.343,3,3S13.657,15,12,15z M16.804,6.116c-0.596,0-1.08,0.484-1.08,1.08 s0.484,1.08,1.08,1.08c0.596,0,1.08-0.484,1.08-1.08S17.401,6.116,16.804,6.116z"></path></svg><span class="wp-block-social-link-label screen-reader-text">Instagram</span></a></li>

<li class="wp-social-link wp-social-link-x  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M13.982 10.622 20.54 3h-1.554l-5.693 6.618L8.745 3H3.5l6.876 10.007L3.5 21h1.554l6.012-6.989L15.868 21h5.245l-7.131-10.378Zm-2.128 2.474-.697-.997-5.543-7.93H8l4.474 6.4.697.996 5.815 8.318h-2.387l-4.745-6.787Z" /></svg><span class="wp-block-social-link-label screen-reader-text">X</span></a></li>

<li class="wp-social-link wp-social-link-facebook  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7C18.3 21.1 22 17 22 12c0-5.5-4.5-10-10-10z"></path></svg><span class="wp-block-social-link-label screen-reader-text">Facebook</span></a></li>

<li class="wp-social-link wp-social-link-tiktok  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M16.708 0.027c1.745-0.027 3.48-0.011 5.213-0.027 0.105 2.041 0.839 4.12 2.333 5.563 1.491 1.479 3.6 2.156 5.652 2.385v5.369c-1.923-0.063-3.855-0.463-5.6-1.291-0.76-0.344-1.468-0.787-2.161-1.24-0.009 3.896 0.016 7.787-0.025 11.667-0.104 1.864-0.719 3.719-1.803 5.255-1.744 2.557-4.771 4.224-7.88 4.276-1.907 0.109-3.812-0.411-5.437-1.369-2.693-1.588-4.588-4.495-4.864-7.615-0.032-0.667-0.043-1.333-0.016-1.984 0.24-2.537 1.495-4.964 3.443-6.615 2.208-1.923 5.301-2.839 8.197-2.297 0.027 1.975-0.052 3.948-0.052 5.923-1.323-0.428-2.869-0.308-4.025 0.495-0.844 0.547-1.485 1.385-1.819 2.333-0.276 0.676-0.197 1.427-0.181 2.145 0.317 2.188 2.421 4.027 4.667 3.828 1.489-0.016 2.916-0.88 3.692-2.145 0.251-0.443 0.532-0.896 0.547-1.417 0.131-2.385 0.079-4.76 0.095-7.145 0.011-5.375-0.016-10.735 0.025-16.093z" /></svg><span class="wp-block-social-link-label screen-reader-text">TikTok</span></a></li>

<li class="wp-social-link wp-social-link-linkedin  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M19.7,3H4.3C3.582,3,3,3.582,3,4.3v15.4C3,20.418,3.582,21,4.3,21h15.4c0.718,0,1.3-0.582,1.3-1.3V4.3 C21,3.582,20.418,3,19.7,3z M8.339,18.338H5.667v-8.59h2.672V18.338z M7.004,8.574c-0.857,0-1.549-0.694-1.549-1.548 c0-0.855,0.691-1.548,1.549-1.548c0.854,0,1.547,0.694,1.547,1.548C8.551,7.881,7.858,8.574,7.004,8.574z M18.339,18.338h-2.669 v-4.177c0-0.996-0.017-2.278-1.387-2.278c-1.389,0-1.601,1.086-1.601,2.206v4.249h-2.667v-8.59h2.559v1.174h0.037 c0.356-0.675,1.227-1.387,2.526-1.387c2.703,0,3.203,1.779,3.203,4.092V18.338z"></path></svg><span class="wp-block-social-link-label screen-reader-text">LinkedIn</span></a></li>
</ul>

</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow" style="flex-basis:60%">

<h2 class="wp-block-heading" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">About Me</h2>



<p style="font-size:clamp(1rem, 2.5vw, 1.1rem);line-height:1.7">Hi, I'm <strong>Yushi Nakashima</strong>, but everyone calls me <strong>UC</strong>. I live in Kōfu, Yamanashi with my wonderful wife <strong>Haruhi</strong> and our son <strong>Ichiyu</strong>.</p>



<h3 class="wp-block-heading" style="color:#34495e;font-size:clamp(1.1rem, 3vw, 1.3rem);font-weight:600">🌟 What Makes Me Happy</h3>



<ul class="wp-block-list" style="font-size:clamp(0.9rem, 2vw, 1rem);line-height:1.6">
<li><strong>Making friends</strong> worldwide 🌍</li>
<li><strong>Family time</strong> with Haruhi and Ichiyu ❤️</li>
<li><strong>Wine adventures</strong> especially Italian & Yamanashi 🍷</li>
<li><strong>Creative projects</strong> with AI and unique ideas 🎨</li>
<li><strong>Temple visits</strong> and cultural exploration 🛕</li>
</ul>



<p style="color:#7f8c8d;font-size:clamp(0.85rem, 2vw, 0.95rem);font-style:italic">"I believe in connecting through vision and empathy, creating worldwide understanding beyond boundaries!"</p>

</div>

</div>

</div>



<div class="wp-block-group recent-posts-section has-background is-layout-flow wp-block-group-is-layout-flow" style="background-color:#f0f2f5;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">

<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">📝 Recent Posts</h2>



<p class="has-text-align-center" style="color:#666666;margin-bottom:40px;font-size:clamp(0.95rem, 2vw, 1.1rem)">Latest thoughts, experiences, and creative adventures</p>


<ul class="wp-block-latest-posts__list wp-block-latest-posts"><li><div class="wp-block-latest-posts__featured-image alignleft"><a href="https://uc.x0.com/toda-tatsuaki-event/" aria-label="An Evening with Tatsuaki Toda: Living by Your Own Cool Standards"><img loading="lazy" decoding="async" width="300" height="225" src="https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-300x225.jpg" class="attachment-medium size-medium wp-post-image" alt="" style="" srcset="https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-300x225.jpg 300w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-1024x768.jpg 1024w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-768x576.jpg 768w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-1536x1152.jpg 1536w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250906_005851-2-2048x1536.jpg 2048w" sizes="auto, (max-width: 300px) 100vw, 300px" /></a></div><a class="wp-block-latest-posts__post-title" href="https://uc.x0.com/toda-tatsuaki-event/">An Evening with Tatsuaki Toda: Living by Your Own Cool Standards</a></li>
<li><div class="wp-block-latest-posts__featured-image alignleft"><a href="https://uc.x0.com/our-family-is-growing-a-wonderful-morning-surprise/" aria-label="Our Family is Growing: A Wonderful Morning Surprise!"><img loading="lazy" decoding="async" width="300" height="225" src="https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-300x225.jpg" class="attachment-medium size-medium wp-post-image" alt="" style="" srcset="https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-300x225.jpg 300w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-1024x768.jpg 1024w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-768x576.jpg 768w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-1536x1152.jpg 1536w, https://uc.x0.com/wp-content/uploads/2025/09/IMG_20250904_120804-2048x1536.jpg 2048w" sizes="auto, (max-width: 300px) 100vw, 300px" /></a></div><a class="wp-block-latest-posts__post-title" href="https://uc.x0.com/our-family-is-growing-a-wonderful-morning-surprise/">Our Family is Growing: A Wonderful Morning Surprise!</a></li>
<li><div class="wp-block-latest-posts__featured-image alignleft"><a href="https://uc.x0.com/finding-peace-and-connection-my-journey-through-temple-visits/" aria-label="Finding Peace and Connection: My Journey Through Temple Visits"><img loading="lazy" decoding="async" width="300" height="225" src="https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc-300x225.jpg" class="attachment-medium size-medium wp-post-image" alt="" style="" srcset="https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc-300x225.jpg 300w, https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc-1024x768.jpg 1024w, https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc-768x576.jpg 768w, https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc-1536x1152.jpg 1536w, https://uc.x0.com/wp-content/uploads/2025/09/temple-visit-monk-uc.jpg 2048w" sizes="auto, (max-width: 300px) 100vw, 300px" /></a></div><a class="wp-block-latest-posts__post-title" href="https://uc.x0.com/finding-peace-and-connection-my-journey-through-temple-visits/">Finding Peace and Connection: My Journey Through Temple Visits</a></li>
</ul>


<p class="has-text-align-center" style="margin-top:30px"><a href="/blog" class="wp-element-button">View All Posts →</a></p>

</div>



<div class="wp-block-group has-background is-layout-flow wp-block-group-is-layout-flow" style="background-color:#f8f9fa;padding-top:60px;padding-bottom:60px;padding-left:20px;padding-right:20px">

<h2 class="wp-block-heading has-text-align-center" style="color:#2c3e50;font-size:clamp(1.8rem, 4vw, 2.2rem);font-weight:600">🎨 My World</h2>



<div class="wp-block-columns is-layout-flex wp-container-core-columns-is-layout-349d4d0c wp-block-columns-is-layout-flex" style="margin-top:30px">

<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow">

<p class="has-text-align-center" style="font-size:clamp(1.502rem, 1.502rem + ((1vw - 0.2rem) * 1.663), 2.5rem);">📸</p>


<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="https://uc.x0.com/best-moments/">人生最高の瞬間</a></p>

</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow">

<p class="has-text-align-center" style="font-size:clamp(1.502rem, 1.502rem + ((1vw - 0.2rem) * 1.663), 2.5rem);">📦</p>


<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="https://uc.x0.com/products/">プロダクト</a></p>

</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow">

<p class="has-text-align-center" style="font-size:clamp(1.502rem, 1.502rem + ((1vw - 0.2rem) * 1.663), 2.5rem);">🛕</p>


<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="https://uc.x0.com/finding-peace-and-connection-my-journey-through-temple-visits/">Temple Visits</a></p>

</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow">

<p class="has-text-align-center" style="font-size:clamp(1.502rem, 1.502rem + ((1vw - 0.2rem) * 1.663), 2.5rem);">🎨</p>


<p class="has-text-align-center" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600"><a href="/creative-projects/">Creative Projects</a></p>

</div>

</div>

</div>



<div class="wp-block-group footer-cta has-background is-layout-flow wp-block-group-is-layout-flow" style="background-color:#2c3e50;padding-top:40px;padding-bottom:60px;padding-left:20px;padding-right:20px">

<p class="has-text-align-center has-base-color" style="font-size:clamp(1.1rem, 2.5vw, 1.3rem);line-height:1.6;font-style:italic">"Let's create worldwide understanding and build meaningful friendships together!" 🤝</p>



<p class="has-text-align-center has-base-color" style="font-size:clamp(0.9rem, 2vw, 1rem);font-weight:600;margin-top:10px">— UC from Yamanashi 🗾</p>



<ul class="wp-block-social-links is-style-logos-only is-content-justification-center is-layout-flex wp-container-core-social-links-is-layout-2aebea9a wp-block-social-links-is-layout-flex" style="margin-top:25px">
<li class="wp-social-link wp-social-link-instagram  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M12,4.622c2.403,0,2.688,0.009,3.637,0.052c0.877,0.04,1.354,0.187,1.671,0.31c0.42,0.163,0.72,0.358,1.035,0.673 c0.315,0.315,0.51,0.615,0.673,1.035c0.123,0.317,0.27,0.794,0.31,1.671c0.043,0.949,0.052,1.234,0.052,3.637 s-0.009,2.688-0.052,3.637c-0.04,0.877-0.187,1.354-0.31,1.671c-0.163,0.42-0.358,0.72-0.673,1.035 c-0.315,0.315-0.615,0.51-1.035,0.673c-0.317,0.123-0.794,0.27-1.671,0.31c-0.949,0.043-1.233,0.052-3.637,0.052 s-2.688-0.009-3.637-0.052c-0.877-0.04-1.354-0.187-1.671-0.31c-0.42-0.163-0.72-0.358-1.035-0.673 c-0.315-0.315-0.51-0.615-0.673-1.035c-0.123-0.317-0.27-0.794-0.31-1.671C4.631,14.688,4.622,14.403,4.622,12 s0.009-2.688,0.052-3.637c0.04-0.877,0.187-1.354,0.31-1.671c0.163-0.42,0.358-0.72,0.673-1.035 c0.315-0.315,0.615-0.51,1.035-0.673c0.317-0.123,0.794-0.27,1.671-0.31C9.312,4.631,9.597,4.622,12,4.622 M12,3 C9.556,3,9.249,3.01,8.289,3.054C7.331,3.098,6.677,3.25,6.105,3.472C5.513,3.702,5.011,4.01,4.511,4.511 c-0.5,0.5-0.808,1.002-1.038,1.594C3.25,6.677,3.098,7.331,3.054,8.289C3.01,9.249,3,9.556,3,12c0,2.444,0.01,2.751,0.054,3.711 c0.044,0.958,0.196,1.612,0.418,2.185c0.23,0.592,0.538,1.094,1.038,1.594c0.5,0.5,1.002,0.808,1.594,1.038 c0.572,0.222,1.227,0.375,2.185,0.418C9.249,20.99,9.556,21,12,21s2.751-0.01,3.711-0.054c0.958-0.044,1.612-0.196,2.185-0.418 c0.592-0.23,1.094-0.538,1.594-1.038c0.5-0.5,0.808-1.002,1.038-1.594c0.222-0.572,0.375-1.227,0.418-2.185 C20.99,14.751,21,14.444,21,12s-0.01-2.751-0.054-3.711c-0.044-0.958-0.196-1.612-0.418-2.185c-0.23-0.592-0.538-1.094-1.038-1.594 c-0.5-0.5-1.002-0.808-1.594-1.038c-0.572-0.222-1.227-0.375-2.185-0.418C14.751,3.01,14.444,3,12,3L12,3z M12,7.378 c-2.552,0-4.622,2.069-4.622,4.622S9.448,16.622,12,16.622s4.622-2.069,4.622-4.622S14.552,7.378,12,7.378z M12,15 c-1.657,0-3-1.343-3-3s1.343-3,3-3s3,1.343,3,3S13.657,15,12,15z M16.804,6.116c-0.596,0-1.08,0.484-1.08,1.08 s0.484,1.08,1.08,1.08c0.596,0,1.08-0.484,1.08-1.08S17.401,6.116,16.804,6.116z"></path></svg><span class="wp-block-social-link-label screen-reader-text">Instagram</span></a></li>

<li class="wp-social-link wp-social-link-x  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M13.982 10.622 20.54 3h-1.554l-5.693 6.618L8.745 3H3.5l6.876 10.007L3.5 21h1.554l6.012-6.989L15.868 21h5.245l-7.131-10.378Zm-2.128 2.474-.697-.997-5.543-7.93H8l4.474 6.4.697.996 5.815 8.318h-2.387l-4.745-6.787Z" /></svg><span class="wp-block-social-link-label screen-reader-text">X</span></a></li>

<li class="wp-social-link wp-social-link-facebook  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M12 2C6.5 2 2 6.5 2 12c0 5 3.7 9.1 8.4 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7C18.3 21.1 22 17 22 12c0-5.5-4.5-10-10-10z"></path></svg><span class="wp-block-social-link-label screen-reader-text">Facebook</span></a></li>

<li class="wp-social-link wp-social-link-tiktok  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M16.708 0.027c1.745-0.027 3.48-0.011 5.213-0.027 0.105 2.041 0.839 4.12 2.333 5.563 1.491 1.479 3.6 2.156 5.652 2.385v5.369c-1.923-0.063-3.855-0.463-5.6-1.291-0.76-0.344-1.468-0.787-2.161-1.24-0.009 3.896 0.016 7.787-0.025 11.667-0.104 1.864-0.719 3.719-1.803 5.255-1.744 2.557-4.771 4.224-7.88 4.276-1.907 0.109-3.812-0.411-5.437-1.369-2.693-1.588-4.588-4.495-4.864-7.615-0.032-0.667-0.043-1.333-0.016-1.984 0.24-2.537 1.495-4.964 3.443-6.615 2.208-1.923 5.301-2.839 8.197-2.297 0.027 1.975-0.052 3.948-0.052 5.923-1.323-0.428-2.869-0.308-4.025 0.495-0.844 0.547-1.485 1.385-1.819 2.333-0.276 0.676-0.197 1.427-0.181 2.145 0.317 2.188 2.421 4.027 4.667 3.828 1.489-0.016 2.916-0.88 3.692-2.145 0.251-0.443 0.532-0.896 0.547-1.417 0.131-2.385 0.079-4.76 0.095-7.145 0.011-5.375-0.016-10.735 0.025-16.093z" /></svg><span class="wp-block-social-link-label screen-reader-text">TikTok</span></a></li>

<li class="wp-social-link wp-social-link-linkedin  wp-block-social-link"><a rel="noopener nofollow" target="_blank" href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor"><svg width="24" height="24" viewBox="0 0 24 24" version="1.1" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M19.7,3H4.3C3.582,3,3,3.582,3,4.3v15.4C3,20.418,3.582,21,4.3,21h15.4c0.718,0,1.3-0.582,1.3-1.3V4.3 C21,3.582,20.418,3,19.7,3z M8.339,18.338H5.667v-8.59h2.672V18.338z M7.004,8.574c-0.857,0-1.549-0.694-1.549-1.548 c0-0.855,0.691-1.548,1.549-1.548c0.854,0,1.547,0.694,1.547,1.548C8.551,7.881,7.858,8.574,7.004,8.574z M18.339,18.338h-2.669 v-4.177c0-0.996-0.017-2.278-1.387-2.278c-1.389,0-1.601,1.086-1.601,2.206v4.249h-2.667v-8.59h2.559v1.174h0.037 c0.356-0.675,1.227-1.387,2.526-1.387c2.703,0,3.203,1.779,3.203,4.092V18.338z"></path></svg><span class="wp-block-social-link-label screen-reader-text">LinkedIn</span></a></li>
</ul>

</div>
EOF
)"'"
}'

echo "Updating homepage with corrected sections..."

UPDATE_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$UPDATE_DATA" \
  "${SITE_URL}/wp-json/wp/v2/pages/${HOMEPAGE_ID}")

echo "Homepage update response: $UPDATE_RESPONSE"

HOMEPAGE_URL=$(echo "$UPDATE_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

if [ -n "$HOMEPAGE_URL" ]; then
    echo ""
    echo "✅ Homepage updated successfully!"
    echo "Updated sections:"
    echo "📸 Family Moments → 人生最高の瞬間 (linked to https://uc.x0.com/best-moments/)"
    echo "🍇 Wine Tasting → 📦 プロダクト (linked to https://uc.x0.com/products/)" 
    echo ""
    echo "Homepage URL: $HOMEPAGE_URL"
else
    echo "❌ Failed to update homepage"
fi