#!/bin/bash

# Load WordPress credentials
SITE_URL="https://uc.x0.com"
USERNAME="uc-japan"
APP_PASSWORD="jcps84OkAVZoW7NQdLcQSimC"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"

IMAGE_FILE="IMG_20250907_203732.jpg"

echo "Uploading image to WordPress..."

# Upload image to WordPress media library
UPLOAD_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Disposition: attachment; filename=\"${IMAGE_FILE}\"" \
  -H "Content-Type: image/jpeg" \
  --data-binary "@${IMAGE_FILE}" \
  "${SITE_URL}/wp-json/wp/v2/media")

echo "Upload response: $UPLOAD_RESPONSE"

# Extract media ID from response
MEDIA_ID=$(echo "$UPLOAD_RESPONSE" | grep -o '"id":[0-9]*' | cut -d':' -f2)

if [ -n "$MEDIA_ID" ]; then
    echo "Image uploaded successfully. Media ID: $MEDIA_ID"
    
    # Create post with featured image
    POST_DATA='{
        "title": "充実の一日：お茶会準備、お月見団子、そしてワインテイスティングの学び",
        "slug": "eventful-day-0907",
        "content": "今日は本当に充実した一日でした。朝から以前ブログでもお話ししたお茶会主催のための会場見学と打ち合わせを行いました。理想的な空間づくりのために、細部まで丁寧に確認させていただきました。<br><br>午後は保育園の友達の家で、季節を感じるお月見団子会を開催。昼間なので月は見えませんでしたが、子どもたちと一緒に日本の伝統行事を楽しむ素敵な時間となりました。その合間には息子の一遊と愛宕山公園へ。変形自転車で思い切り遊び、親子の時間を満喫しました。<br><br>一日中動き回っていたので、さすがに体力の限界を感じていましたが、夜はさらに学びの時間が待っていました。友達の大木さんがワイン検定の講師をされた経験をお持ちということで、ワインテイスティング会に参加させていただきました。<br><br>山梨はワインの名産地として知られており、地元に住む者として、もっと深くワインについて学びたいと常々思っていました。今夜のテイスティングでは、様々な産地や品種のワインを楽しみながら、それぞれの特徴や背景について教えていただきました。<br><br>これからも多くの人と美味しいワインを囲みながら、豊かな会話を楽しめるよう、楽しく学んでいきたいと思います。一日の終わりに、こんなに充実した時間を過ごせたことに感謝です。",
        "status": "publish",
        "featured_media": '$MEDIA_ID'
    }'
else
    echo "Failed to upload image. Creating post without featured image."
    
    # Create post without featured image
    POST_DATA='{
        "title": "充実の一日：お茶会準備、お月見団子、そしてワインテイスティングの学び",
        "slug": "eventful-day-0907",
        "content": "今日は本当に充実した一日でした。朝から以前ブログでもお話ししたお茶会主催のための会場見学と打ち合わせを行いました。理想的な空間づくりのために、細部まで丁寧に確認させていただきました。<br><br>午後は保育園の友達の家で、季節を感じるお月見団子会を開催。昼間なので月は見えませんでしたが、子どもたちと一緒に日本の伝統行事を楽しむ素敵な時間となりました。その合間には息子の一遊と愛宕山公園へ。変形自転車で思い切り遊び、親子の時間を満喫しました。<br><br>一日中動き回っていたので、さすがに体力の限界を感じていましたが、夜はさらに学びの時間が待っていました。友達の大木さんがワイン検定の講師をされた経験をお持ちということで、ワインテイスティング会に参加させていただきました。<br><br>山梨はワインの名産地として知られており、地元に住む者として、もっと深くワインについて学びたいと常々思っていました。今夜のテイスティングでは、様々な産地や品種のワインを楽しみながら、それぞれの特徴や背景について教えていただきました。<br><br>これからも多くの人と美味しいワインを囲みながら、豊かな会話を楽しめるよう、楽しく学んでいきたいと思います。一日の終わりに、こんなに充実した時間を過ごせたことに感謝です。",
        "status": "publish"
    }'
fi

echo "Creating WordPress post..."

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