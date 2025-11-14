#!/bin/bash

# WordPress credentials
SITE_URL="https://uc.x0.com"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"
POST_ID=152

echo "Updating post to English..."

# Update the existing post with English content
POST_DATA='{
    "title": "A Full Day of Learning and Tradition: Tea Ceremony Preparations, Moon Viewing Dumplings, and Wine Tasting",
    "content": "Today was truly a fulfilling day packed with diverse experiences. Starting from the morning, I conducted a venue inspection and meeting for the tea ceremony hosting that I previously mentioned in my blog. We carefully examined every detail to create the ideal atmosphere for this special event.<br><br>In the afternoon, we held a traditional moon viewing dumpling gathering at a kindergarten friend'\''s house. Although it was daytime and we couldn'\''t actually see the moon, it was a wonderful opportunity to enjoy Japanese traditional customs with the children. Between activities, I took my son Kazuyu to Atago Mountain Park, where we had a blast playing on the unique bicycles and enjoying quality father-son time.<br><br>After being active all day, I was certainly feeling the limits of my energy, but the evening had even more learning in store. My friend Oki-san, who has experience as a wine certification instructor, invited me to participate in a wine tasting session.<br><br>Yamanashi is renowned as a famous wine-producing region, and as someone living locally, I'\''ve always wanted to deepen my knowledge about wine. During tonight'\''s tasting, I had the opportunity to sample wines from various regions and grape varieties while learning about their unique characteristics and backgrounds.<br><br>I look forward to continuing this enjoyable learning journey so that I can share meaningful conversations over delicious wine with many people in the future. At the end of such a full day, I feel truly grateful for having experienced such enriching moments.",
    "status": "publish"
}'

# Update WordPress post
UPDATE_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$POST_DATA" \
  "${SITE_URL}/wp-json/wp/v2/posts/${POST_ID}")

echo "Update response: $UPDATE_RESPONSE"

# Extract post URL from response
POST_URL=$(echo "$UPDATE_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

if [ -n "$POST_URL" ]; then
    echo ""
    echo "✅ WordPress post updated to English successfully!"
    echo "View your updated post at: $POST_URL"
else
    echo ""
    echo "❌ Failed to update WordPress post"
fi