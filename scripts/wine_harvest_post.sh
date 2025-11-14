#!/bin/bash

USERNAME="uc-japan"
APP_PASSWORD="MWExSgYfvQ98OmvvJ7rfuibb"

curl -X POST "https://uc.x0.com/wp-json/wp/v2/posts" \
  -u "${USERNAME}:${APP_PASSWORD}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Grape Harvesting and Winery Tour at Chateau Sakaori - Wine Introduction Course",
    "content": "<p>This month, I attended one of the final two sessions of the Wine Introduction course at Yamanashi Prefectural University, which I have been taking since the spring semester. This session was particularly special as we got to experience hands-on grape harvesting and a comprehensive winery tour.</p><h2>Visit to Chateau Sakaori Winery</h2><p>Our class visited <strong>Chateau Sakaori Winery</strong>, where we had the incredible opportunity to harvest grapes - the very foundation of wine production. Getting to pick the grapes with my own hands gave me a deeper appreciation for the entire winemaking process and the work that goes into every bottle.</p><h2>Learning the Winemaking Process</h2><p>After the harvest, we received detailed explanations about how wine is made, from grape to bottle. We then toured the cellar facilities, observing the equipment and processes used in wine production. Seeing the professional operation up close was fascinating and educational.</p><h2>Wine Tasting Session</h2><p>The experience concluded with a wine tasting session, where I got to enjoy several different wines alongside the students. It was wonderful to taste the fruits of the winery'\''s labor while discussing what we had learned throughout the day.</p><h2>A Uniquely Yamanashi Experience</h2><p>What struck me most about this experience was how unique it is to be able to drink wine, socialize, and learn as part of a university course. This is something that can only happen in Yamanashi, Japan'\''s premier wine-producing region.</p><p>Being able to mix with students, enjoy wine together in an academic setting, and learn about the local wine culture felt like a truly special opportunity. This kind of educational and cultural experience is unique to Yamanashi, and I found it incredibly enjoyable.</p><p>I genuinely believe this wine culture - combining education, social interaction, and appreciation for local products - is something worth spreading more widely. It'\''s experiences like these that make me grateful to be living and learning in Yamanashi Prefecture.</p>",
    "status": "publish",
    "categories": [1]
  }'
