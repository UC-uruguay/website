#!/bin/bash

# Get a fresh JWT token
echo "Getting fresh JWT token..."
JWT_RESPONSE=$(curl -s -X POST "https://chaba-ba.jpn.org/wp-json/jwt-auth/v1/token" \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}')

# Extract token (simple grep approach since no jq)
JWT_TOKEN=$(echo "$JWT_RESPONSE" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

if [ -z "$JWT_TOKEN" ]; then
    echo "Failed to get JWT token. Using existing token..."
    JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"
else
    echo "Got fresh JWT token!"
fi

# Try to update the homepage content using WordPress REST API
echo "Updating homepage content..."

# Simple approach - try to update page ID 1 (usually homepage)
response=$(curl -s -X PUT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -d '{
    "title": "茶Bar ～茶婆場～", 
    "content": "<!DOCTYPE html><html lang=\"ja\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>茶Bar ～茶婆場～</title></head><body><h1>茶Bar ～茶婆場～</h1><p>お茶の魅力を多角的に楽しめる体験型お茶バー</p><h2>イベント開催情報</h2><p><strong>開催日：</strong>2025年10月18日（土）※時間未定（日曜日開催の可能性もあります：10月19日（日））</p><p><strong>場所：</strong>未定（決定次第更新いたします）</p><p><strong>対象：</strong>一般のお客様（どなたでも大歓迎！）</p></body></html>",
    "status": "publish"
  }' \
  "https://chaba-ba.jpn.org/wp-json/wp/v2/pages/1")

echo "Response: $response"

# Also try creating a new page
echo "Creating new page..."
response2=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -d '{
    "title": "茶Bar ～茶婆場～ ホームページ", 
    "content": "<!DOCTYPE html><html lang=\"ja\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>茶Bar ～茶婆場～</title><style>body{font-family: \"Hiragino Kaku Gothic Pro\", \"Meiryo\", sans-serif;line-height:1.6;color:#2c3e2d;background:#faf9f7}.hero{background:linear-gradient(135deg,#4a5d23,#6b7c32);color:white;padding:4rem 0;text-align:center}.hero h1{font-size:3rem;margin-bottom:1rem}</style></head><body><div class=\"hero\"><h1>茶Bar ～茶婆場～</h1><p>お茶の魅力を多角的に楽しめる体験型お茶バー</p></div><section><h2>🍵 イベント開催情報</h2><p><strong>📅 開催日：</strong>2025年10月18日（土）※時間未定<br><small>（日曜日開催の可能性もあります：10月19日（日））</small></p><p><strong>📍 場所：</strong>未定（決定次第更新いたします）</p><p><strong>🎯 対象：</strong>一般のお客様（どなたでも大歓迎！）</p></section><section><h2>コンセプト</h2><p>お茶の魅力を多角的に楽しめる体験型のお茶バー。お茶初心者から愛好家まで、誰もが気軽に立ち寄れる温かい空間を目指します。お酒好きの方にも楽しんでいただけるよう、お茶のお酒もご提供いたします。</p></section></body></html>",
    "status": "publish",
    "slug": "chababa-home"
  }' \
  "https://chaba-ba.jpn.org/wp-json/wp/v2/pages")

echo "New page response: $response2"