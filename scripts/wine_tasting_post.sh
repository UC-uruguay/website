#!/bin/bash

# Load WordPress credentials
SITE_URL="https://uc.x0.com"
USERNAME="uc-japan"
APP_PASSWORD="jcps84OkAVZoW7NQdLcQSimC"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"

echo "Creating WordPress post about wine tasting..."

# Create post with engaging English content
POST_DATA='{
    "title": "Wine Tasting: Life'\''s Perfect Moments",
    "slug": "wine-tasting-perfect-moments",
    "content": "There'\''s something almost sacred about the ritual of wine tasting - that suspended moment when time stops and your senses awaken to something extraordinary.<br><br>Each sip reveals layers of story: the sun-soaked vineyards, the patient aging, the careful craft. It'\''s not just about the wine; it'\''s about being present in a moment that demands your full attention.<br><br>These are the moments that remind us what living well truly means - when complexity meets simplicity, when tradition meets the present, and when we discover that some of life'\''s greatest pleasures come from slowing down enough to truly taste them.<br><br>Wine tasting isn'\''t just an experience; it'\''s a meditation on what makes life beautiful.",
    "status": "publish"
}'

# Create WordPress post
POST_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$POST_DATA" \
  "${SITE_URL}/wp-json/wp/v2/posts")

echo "Post creation response: $POST_RESPONSE"

# Extract post URL from response
POST_URL=$(echo "$POST_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

if [ -n "$POST_URL" ]; then
    echo ""
    echo "✅ WordPress post created successfully!"
    echo "View your post at: $POST_URL"
else
    echo ""
    echo "❌ Failed to create WordPress post"
fi