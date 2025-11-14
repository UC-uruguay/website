#!/bin/bash

# WordPress credentials
SITE_URL="https://uc.x0.com"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"

echo "Creating new pages..."

# Create 人生最高の瞬間 page
echo "Creating 人生最高の瞬間 page..."
MOMENTS_DATA='{
    "title": "人生最高の瞬間",
    "slug": "best-moments",
    "content": "<p>人生最高の瞬間のページです。内容は後で追加されます。</p>",
    "status": "publish"
}'

MOMENTS_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$MOMENTS_DATA" \
  "${SITE_URL}/wp-json/wp/v2/pages")

echo "Moments page response: $MOMENTS_RESPONSE"
MOMENTS_URL=$(echo "$MOMENTS_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

# Create プロダクト page
echo "Creating プロダクト page..."
PRODUCTS_DATA='{
    "title": "プロダクト",
    "slug": "products", 
    "content": "<p>プロダクトページです。内容は後で追加されます。</p>",
    "status": "publish"
}'

PRODUCTS_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$PRODUCTS_DATA" \
  "${SITE_URL}/wp-json/wp/v2/pages")

echo "Products page response: $PRODUCTS_RESPONSE"
PRODUCTS_URL=$(echo "$PRODUCTS_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

echo ""
echo "Pages created:"
echo "人生最高の瞬間: $MOMENTS_URL"
echo "プロダクト: $PRODUCTS_URL"

# Get homepage to find its ID
echo ""
echo "Getting homepage information..."
PAGES_RESPONSE=$(curl -s -H "Authorization: Basic ${BASE64_TOKEN}" "${SITE_URL}/wp-json/wp/v2/pages")

# Extract homepage ID (assuming it's the first page or has slug 'home')
HOMEPAGE_ID=$(echo "$PAGES_RESPONSE" | grep -o '"id":[0-9]*' | head -1 | cut -d':' -f2)

if [ -n "$HOMEPAGE_ID" ]; then
    echo "Found homepage ID: $HOMEPAGE_ID"
    
    # Get current homepage content
    HOMEPAGE_RESPONSE=$(curl -s -H "Authorization: Basic ${BASE64_TOKEN}" "${SITE_URL}/wp-json/wp/v2/pages/${HOMEPAGE_ID}")
    
    # For now, let's create a simple update to change the section names
    # We'll need to manually construct the updated content
    UPDATE_DATA='{
        "content": "<!-- wp:heading --><h2>Welcome to UC Creative Soul</h2><!-- /wp:heading --><!-- wp:columns --><div class=\"wp-block-columns\"><!-- wp:column --><div class=\"wp-block-column\"><!-- wp:heading {\"level\":3,\"textAlign\":\"center\"} --><h3 class=\"has-text-align-center\">👥</h3><!-- /wp:heading --><!-- wp:heading {\"level\":3,\"textAlign\":\"center\"} --><h3 class=\"has-text-align-center\"><a href=\"'$MOMENTS_URL'\">人生最高の瞬間</a></h3><!-- /wp:heading --><!-- wp:paragraph {\"align\":\"center\"} --><p class=\"has-text-align-center\">Life'\''s greatest moments captured and shared</p><!-- /wp:paragraph --></div><!-- /wp:column --><!-- wp:column --><div class=\"wp-block-column\"><!-- wp:heading {\"level\":3,\"textAlign\":\"center\"} --><h3 class=\"has-text-align-center\">📦</h3><!-- /wp:heading --><!-- wp:heading {\"level\":3,\"textAlign\":\"center\"} --><h3 class=\"has-text-align-center\"><a href=\"'$PRODUCTS_URL'\">プロダクト</a></h3><!-- /wp:heading --><!-- wp:paragraph {\"align\":\"center\"} --><p class=\"has-text-align-center\">Products and creations</p><!-- /wp:paragraph --></div><!-- /wp:column --></div><!-- /wp:columns -->"
    }'
    
    echo "Updating homepage content..."
    UPDATE_RESPONSE=$(curl -s -X POST \
      -H "Authorization: Basic ${BASE64_TOKEN}" \
      -H "Content-Type: application/json" \
      -d "$UPDATE_DATA" \
      "${SITE_URL}/wp-json/wp/v2/pages/${HOMEPAGE_ID}")
    
    echo "Homepage update response: $UPDATE_RESPONSE"
    
    HOMEPAGE_URL=$(echo "$UPDATE_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)
    
    echo ""
    echo "✅ All updates completed!"
    echo "Homepage: $HOMEPAGE_URL"
    echo "人生最高の瞬間 page: $MOMENTS_URL"
    echo "プロダクト page: $PRODUCTS_URL"
else
    echo "❌ Could not find homepage ID"
fi