#!/bin/bash

JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# Upload image first
echo "Uploading pool image..."
upload_response=$(curl -X POST \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Disposition: attachment; filename=\"pool_day_0906.jpg\"" \
  -H "Content-Type: image/jpeg" \
  --data-binary @"/home/uc/0906.jpg" \
  "https://uc.x0.com/wp-json/wp/v2/media")

echo "Upload response: $upload_response"

# Extract media ID
media_id=$(echo "$upload_response" | jq -r '.id')
echo "Image uploaded successfully. Media ID: $media_id"

# Create the post content
title="Fun-Filled Pool Day at Fumot: Adventures and Aching Necks"

content="Today was an adventure-packed day at Fumot, the impressive outdoor pool facility attached to Costco in the Southern Alps! Despite the hefty price tag, I was fortunate enough to score tickets for what turned out to be an unforgettable family outing.<br><br>The facility is absolutely incredible - featuring around 10 different pools and slides that cater to every age and thrill level. My son and I had a blast exploring the various attractions, from the gentler family-friendly pools to the more exciting water features.<br><br>But here's where my day took an unexpected turn: I decided to challenge myself with the giant slide reserved exclusively for adults. Let me tell you - that decision came with consequences! The thrill was intense, but so was the whiplash. My neck is still protesting from the adventure, serving as a not-so-gentle reminder that sometimes age comes with wisdom (and more fragile joints).<br><br>The day's activities left us all pleasantly exhausted, so we decided to cap off our pool adventure with a relaxing visit to a hot spring in the evening. The warm, therapeutic waters were exactly what our tired bodies needed - though I have to admit, my neck is still giving me grief despite the soothing soak.<br><br>Sometimes the best family memories come with a few battle scars. Today was definitely one of those days - worth every ache and pain for the smiles and laughter we shared."

echo "Creating WordPress post about pool day..."

# Create the post
post_response=$(curl -X POST \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"$title\",
    \"content\": \"$content\",
    \"status\": \"publish\",
    \"featured_media\": $media_id,
    \"categories\": [8]
  }" \
  "https://uc.x0.com/wp-json/wp/v2/posts")

echo "Post creation response: $post_response"

# Extract the post URL
post_url=$(echo "$post_response" | jq -r '.link')
echo ""
echo "✅ Pool day article created successfully!"
echo "View your post at: $post_url"