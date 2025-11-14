#!/bin/bash

JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# カスタムCSSを追加してヒーロー背景を変更
curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -H "Authorization: Bearer ${JWT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Hero Background Update",
    "content": "<style>.hero { background-image: url('\''https://uc.x0.com/wp-content/uploads/2025/01/chalogo.png'\'') !important; background-size: cover !important; background-position: center !important; } .hero::before { background: rgba(0, 0, 0, 0.3) !important; }</style>",
    "status": "publish"
  }'

echo ""
echo "✅ ヒーロー背景のスタイルを更新しました"
