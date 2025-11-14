#!/bin/bash

# WordPress投稿スクリプト
# 使い方: ./post_to_wordpress.sh "タイトル" "本文HTML"

SITE_URL="https://uc.x0.com"
USERNAME="uc-japan"
PASSWORD="zgrCJ86d4HLrzKqz7ycb1fAo"

TITLE="$1"
CONTENT="$2"
STATUS="${3:-draft}"  # デフォルトは下書き

if [ -z "$TITLE" ] || [ -z "$CONTENT" ]; then
    echo "使い方: $0 \"タイトル\" \"本文HTML\" [status]"
    echo "例: $0 \"My Title\" \"<p>Content</p>\" \"publish\""
    exit 1
fi

# JSON作成
JSON_DATA=$(jq -n \
    --arg title "$TITLE" \
    --arg content "$CONTENT" \
    --arg status "$STATUS" \
    '{title: $title, content: $content, status: $status}')

# 投稿
RESPONSE=$(curl -s -X POST "${SITE_URL}/wp-json/wp/v2/posts" \
    -u "${USERNAME}:${PASSWORD}" \
    -H "Content-Type: application/json" \
    -d "$JSON_DATA")

# 結果確認
if echo "$RESPONSE" | jq -e '.id' > /dev/null 2>&1; then
    POST_ID=$(echo "$RESPONSE" | jq -r '.id')
    POST_LINK=$(echo "$RESPONSE" | jq -r '.link')
    echo "✓ 投稿成功！"
    echo "  ID: $POST_ID"
    echo "  URL: $POST_LINK"
else
    echo "✗ 投稿失敗"
    echo "$RESPONSE" | jq -r '.message // "エラー詳細不明"'
fi