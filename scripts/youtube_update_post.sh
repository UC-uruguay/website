#!/bin/bash

# Create WordPress post about YouTube channel update
curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "YouTube Channel Update - Posted Ichiyu'\''s Monthly Summary Video!",
    "content": "<p>I have been updating my YouTube channel for more than 10 years. I used to upload about my own life, but for the past 3 years, it has been all about my son Ichiyu.</p><p>I was updating consistently, but this month I was busy and couldn'\''t upload much. However, I finally posted a monthly summary video.</p><p>Please check it out and subscribe to my channel!</p><p><a href=\"https://youtu.be/Mx_KEkE2O6A?si=8cmeEKbA_XYyPdGS\" target=\"_blank\">YouTube Video Link</a></p>",
    "status": "publish",
    "categories": [1]
  }'