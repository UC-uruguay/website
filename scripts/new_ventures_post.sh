#!/bin/bash

USERNAME="uc-japan"
APP_PASSWORD="MWExSgYfvQ98OmvvJ7rfuibb"

curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Exciting New Ventures: Pop-up Shop with My Son and Challenge Shop Application",
    "content": "<p>October is shaping up to be an exciting month full of new entrepreneurial experiments! In addition to the Cha Bar event on October 19th (Sunday), I have two more ventures in the works that I'\''m really looking forward to.</p><h2>Pop-up Drink Stand with Ichiyu (October 25th)</h2><p>On <strong>October 25th</strong>, my son Ichiyu and I will be running a pop-up drink stand on Orion Street in Kofu. This is part of a Kofu City initiative that supports small business experiments.</p><p>We'\''ll be selling drinks at <strong>100 yen per cup</strong>, and the main goal is to give Ichiyu hands-on experience running a shop. I want him to practice this many times so he can develop a real understanding of money, business transactions, and customer service. I'\''m hoping this repeated experience will help him build a strong concept of money and entrepreneurship from a young age.</p><h2>Applying for Koshu City Challenge Shop</h2><p>I'\''ve also discovered that Koshu City is offering a Challenge Shop program where aspiring entrepreneurs can rent retail space for just <strong>10,000 yen per month</strong> (plus utilities like water and electricity). This is an incredible opportunity to test business ideas without the usual high overhead costs.</p><p>I haven'\''t submitted the application documents yet, but I'\''m planning to apply soon. If approved, I could start operating as early as next month or the month after. It'\''s another exciting opportunity to experiment with new business concepts in a low-risk environment.</p><h2>Looking Forward to New Beginnings</h2><p>Between the Cha Bar event on October 19th, the pop-up shop with Ichiyu on October 25th, and the potential Challenge Shop starting next month, there are so many new things beginning simultaneously. I'\''m genuinely excited about all these opportunities to learn, experiment, and grow both personally and as an entrepreneur.</p><p>Each of these ventures represents a different aspect of what I'\''m passionate about: community building through tea culture, teaching entrepreneurship to the next generation, and exploring new business models in Yamanashi. I can'\''t wait to see how each of these projects develops!</p>",
    "status": "publish",
    "categories": [1]
  }'
