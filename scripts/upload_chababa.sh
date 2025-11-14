#!/bin/bash

# Set the JWT token
JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# First, let's get the current homepage ID
echo "Getting current homepage information..."
homepage_id=$(curl -s -H "Authorization: Bearer $JWT_TOKEN" \
  "https://chaba-ba.jpn.org/wp-json/wp/v2/pages?per_page=100" | \
  jq -r '.[] | select(.slug == "home" or .title.rendered == "Home" or .id == 1) | .id' | head -1)

if [ -z "$homepage_id" ]; then
    echo "No homepage found, will create a new page..."
    homepage_id=""
fi

# Read the HTML content and escape it properly
content=$(cat /home/uc/chababa_website.html | sed 's/\\/\\\\/g' | sed 's/"/\\"/g' | sed 's/$/\\n/' | tr -d '\n')

# Create JSON payload
json_payload=$(cat <<EOF
{
  "title": "茶Bar 〜茶婆場〜",
  "content": "$content",
  "status": "publish",
  "type": "page",
  "slug": "home"
}
EOF
)

if [ -n "$homepage_id" ]; then
    echo "Updating existing homepage (ID: $homepage_id)..."
    response=$(curl -s -X PUT \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $JWT_TOKEN" \
      -d "$json_payload" \
      "https://chaba-ba.jpn.org/wp-json/wp/v2/pages/$homepage_id")
else
    echo "Creating new homepage..."
    response=$(curl -s -X POST \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $JWT_TOKEN" \
      -d "$json_payload" \
      "https://chaba-ba.jpn.org/wp-json/wp/v2/pages")
fi

echo "Response: $response"

# Check if successful
if echo "$response" | jq -e '.id' > /dev/null 2>&1; then
    page_id=$(echo "$response" | jq -r '.id')
    echo "✅ Successfully uploaded! Page ID: $page_id"
    
    # Set as homepage
    echo "Setting as homepage..."
    curl -s -X POST \
      -H "Authorization: Bearer $JWT_TOKEN" \
      -d "show_on_front=page&page_on_front=$page_id" \
      "https://chaba-ba.jpn.org/wp-admin/admin-ajax.php?action=update_option"
    
    echo "✅ Homepage updated successfully!"
else
    echo "❌ Error uploading page:"
    echo "$response" | jq '.'
fi