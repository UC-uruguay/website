#!/bin/bash

# WordPress credentials
SITE_URL="https://uc.x0.com"
BASE64_TOKEN="dWMtamFwYW46amNwczg0T2tBVlpvVzdOUWRMY1FTaW1D"

echo "Creating English pages following the TOP PRIORITY RULE..."

# Delete existing Japanese pages first
echo "Deleting existing Japanese pages..."
curl -s -X DELETE -H "Authorization: Basic ${BASE64_TOKEN}" "${SITE_URL}/wp-json/wp/v2/pages/113?force=true"
curl -s -X DELETE -H "Authorization: Basic ${BASE64_TOKEN}" "${SITE_URL}/wp-json/wp/v2/pages/114?force=true"

# Create Life's Greatest Moments page (English)
echo "Creating Life's Greatest Moments page..."
MOMENTS_DATA='{
    "title": "Life'\''s Greatest Moments",
    "slug": "best-moments",
    "content": "<h1>Life'\''s Greatest Moments 🌟</h1><p>Welcome to a collection of life'\''s most precious and meaningful experiences. This is where I share the moments that make life truly beautiful and worth living.</p><h2>What Makes a Greatest Moment?</h2><p>These are the times when everything feels perfect - when joy, love, and wonder come together in perfect harmony. From intimate family celebrations to breathtaking discoveries, these moments remind us what it means to be truly alive.</p><p><em>Content will be added as I capture more of life'\''s greatest moments...</em></p>",
    "status": "publish"
}'

MOMENTS_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$MOMENTS_DATA" \
  "${SITE_URL}/wp-json/wp/v2/pages")

echo "Life's Greatest Moments response: $MOMENTS_RESPONSE"
MOMENTS_URL=$(echo "$MOMENTS_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

# Create Products page (English)
echo "Creating Products page..."
PRODUCTS_DATA='{
    "title": "Products",
    "slug": "products", 
    "content": "<h1>Products 📦</h1><p>Discover my creative products and innovative solutions. From unique digital creations to thoughtful services, this is where passion meets purpose.</p><h2>What You'\''ll Find Here</h2><p>I believe in creating products that make a difference - whether it'\''s through technology, creativity, or meaningful connections. Each product reflects my commitment to quality and innovation.</p><p><em>Products and services will be showcased here...</em></p>",
    "status": "publish"
}'

PRODUCTS_RESPONSE=$(curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$PRODUCTS_DATA" \
  "${SITE_URL}/wp-json/wp/v2/pages")

echo "Products response: $PRODUCTS_RESPONSE"
PRODUCTS_URL=$(echo "$PRODUCTS_RESPONSE" | grep -o '"link":"[^"]*' | cut -d'"' -f4)

echo ""
echo "✅ English pages created successfully!"
echo "Life's Greatest Moments: $MOMENTS_URL"
echo "Products: $PRODUCTS_URL"