#!/bin/bash

USERNAME="uc-japan"
APP_PASSWORD="MWExSgYfvQ98OmvvJ7rfuibb"

curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Join Us at Cha Bar (茶Bar 〜茶婆場〜) - Tea Gathering Event on October 19th",
    "content": "<p>I am excited to announce that we have launched a new website for our upcoming tea gathering event, <strong>Cha Bar (茶Bar 〜茶婆場〜)</strong>, which will be held on <strong>Sunday, October 19th from 2:30 PM to 5:30 PM</strong>!</p><h2>Event Details</h2><p><strong>Date:</strong> October 19th (Sunday), 2025<br><strong>Time:</strong> 14:30 - 17:30<br><strong>Location:</strong> Ebisu-ya, 1-14-14 Marunouchi, Kofu City, Yamanashi Prefecture<br><strong>Website:</strong> <a href=\"https://chaba-ba.jpn.org/\" target=\"_blank\">https://chaba-ba.jpn.org/</a></p><h2>What is Cha Bar?</h2><p>Cha Bar is a one-day limited community bar where you can enjoy various types of Japanese tea while making new friends. Our concept is simple: <em>\"Chaっと広がる、Chaんと繋がる、友だち作りの大Chaンス！\"</em> (Expand casually, connect properly, and seize the great chance to make friends!)</p><h2>What We Offer</h2><ul><li><strong>Tea Selection:</strong> Try four different types of tea with traditional sweets (1,000 yen)</li><li><strong>Individual Teas:</strong> Fujiakaori, Vietnamese tea, Earl Grey, Kuromoji tea, and more (500 yen each)</li><li><strong>Food Menu:</strong> Traditional dango sets, matcha tiramisu, ochazuke, and more</li><li><strong>Activities:</strong> Tea fortune-telling, tea blending competition, regional tea tasting game, and more!</li></ul><h2>Everyone is Welcome!</h2><p>This event is open to anyone who wants to enjoy tea and meet new people. Whether you'\''re a tea enthusiast or just curious about Japanese tea culture, you'\''re more than welcome to join us. We'\''ve updated our website with all the details about the menu, team members, and activities planned for the day.</p><p>Please visit our website at <a href=\"https://chaba-ba.jpn.org/\" target=\"_blank\">https://chaba-ba.jpn.org/</a> for more information, and we look forward to seeing you on October 19th!</p><p>Come enjoy a cup of tea and make lifelong friendships. As the Japanese tea spirit says, <em>\"一期一会\"</em> (once in a lifetime encounter) - this meeting might be a once-in-a-lifetime opportunity!</p>",
    "status": "publish",
    "categories": [1]
  }'
