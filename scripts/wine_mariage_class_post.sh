#!/bin/bash

USERNAME="uc-japan"
APP_PASSWORD="jcps84OkAVZoW7NQdLcQSimC"

curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Starting Wine and Food Pairing Class at Yamanashi Prefectural University",
    "content": "<p>Today marks the beginning of the fall semester at Yamanashi Prefectural University, and I am excited to start a new course called \"Wine and Mariage\" (Wine and Food Pairing).</p><p>I enrolled as a working professional student and have been attending the \"Introduction to Wine\" class since the spring semester, which continues to this day. Now, starting this fall semester, I will be learning about wine paired with food, and I am really looking forward to it.</p><p>Additionally, next month I plan to take and sit for the Wine Certification Silver level exam, following the Bronze level I completed last year. I hope this class will help build my knowledge for the certification, and I am committed to working hard to learn all about Yamanashi'\''s unique wine culture.</p><p>Yamanashi Prefecture is one of Japan'\''s premier wine-producing regions, and being able to study wine here is a wonderful opportunity. I'\''m excited to deepen my understanding of wine through both theory and practical pairing experiences.</p>",
    "status": "publish",
    "categories": [1]
  }'
