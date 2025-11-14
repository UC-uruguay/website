#!/bin/bash

# WordPress credentials for chaba-ba.jpn.org
SITE_URL="https://chaba-ba.jpn.org"
USERNAME="uc-japan"
APP_PASSWORD="UfAw oUaF sph2 POw6 wANG ThEn"
BASE64_TOKEN=$(echo -n "${USERNAME}:${APP_PASSWORD}" | base64)

echo "Creating simplified Kadence homepage..."

# Delete existing page first
echo "Deleting existing homepage..."
curl -s -X DELETE \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  "${SITE_URL}/wp-json/wp/v2/pages/10?force=true"

# Create the complete Kadence blocks page with proper encoding
curl -s -X POST \
  -H "Authorization: Basic ${BASE64_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "茶 Bar ～茶婆場～",
    "slug": "homepage",
    "content": "<!-- wp:kadence/rowlayout {\"uniqueID\":\"_hero001\",\"columns\":1,\"colLayout\":\"equal\",\"tabletLayout\":\"equal\",\"columnGutter\":\"default\",\"minHeight\":100,\"minHeightUnit\":\"vh\",\"verticalAlignment\":\"middle\",\"overlay\":[{\"type\":\"gradient\",\"gradient\":\"linear-gradient(135deg, rgba(47,82,51,0.8) 0%, rgba(34,139,34,0.6) 100%)\"}],\"padding\":[\"xxl\",\"lg\",\"xxl\",\"lg\"],\"htmlAnchor\":\"top\"} -->\n<div id=\"top\" class=\"wp-block-kadence-rowlayout alignnone kt-row-layout-inner kt-layout-id_hero001 kt-row-has-bg kt-row-overlay-normal\">\n\n<!-- wp:kadence/column {\"uniqueID\":\"_herocol1\"} -->\n<div class=\"wp-block-kadence-column kadence-column_herocol1\">\n\n<!-- wp:kadence/advancedheading {\"uniqueID\":\"_herotitle\",\"level\":1,\"align\":\"center\",\"color\":\"#ffffff\",\"size\":[\"4rem\",\"3.5rem\",\"2.8rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.1,1.1,1.2],\"lineType\":\"em\",\"fontWeight\":\"700\",\"margin\":[{\"desk\":[\"\",\"\",\"30px\",\"\"],\"tablet\":[\"\",\"\",\"25px\",\"\"],\"mobile\":[\"\",\"\",\"20px\",\"\"]}]} -->\n<h1 id=\"kt-adv-heading_herotitle\" class=\"wp-block-kadence-advancedheading has-text-align-center\" style=\"color:#ffffff;font-size:4rem;line-height:1.1em;font-weight:700;margin-bottom:30px\">🍵 茶 Bar ～茶婆場～</h1>\n<!-- /wp:kadence/advancedheading -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_herodate\",\"align\":\"center\",\"color\":\"#FFD700\",\"size\":[\"1.8rem\",\"1.6rem\",\"1.4rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.3,1.3,1.4],\"lineType\":\"em\",\"fontWeight\":\"600\",\"margin\":[{\"desk\":[\"\",\"\",\"20px\",\"\"],\"tablet\":[\"\",\"\",\"18px\",\"\"],\"mobile\":[\"\",\"\",\"15px\",\"\"]}]} -->\n<div class=\"wp-block-kadence-advancedtext has-text-align-center\" style=\"color:#FFD700;font-size:1.8rem;line-height:1.3em;font-weight:600;margin-bottom:20px\">📅 2025年10月18日(土) or 19日(日)<br>※時間は確定次第更新</div>\n<!-- /wp:kadence/advancedtext -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_herolocation\",\"align\":\"center\",\"color\":\"#F5E6D3\",\"size\":[\"1.4rem\",\"1.3rem\",\"1.2rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.4,1.4,1.4],\"lineType\":\"em\",\"fontWeight\":\"500\",\"margin\":[{\"desk\":[\"\",\"\",\"40px\",\"\"],\"tablet\":[\"\",\"\",\"35px\",\"\"],\"mobile\":[\"\",\"\",\"30px\",\"\"]}]} -->\n<div class=\"wp-block-kadence-advancedtext has-text-align-center\" style=\"color:#F5E6D3;font-size:1.4rem;line-height:1.4em;font-weight:500;margin-bottom:40px\">📍 ゑびすや<br>〒400-0031 山梨県甲府市丸の内１丁目１４−４</div>\n<!-- /wp:kadence/advancedtext -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_herocatch\",\"align\":\"center\",\"color\":\"#ffffff\",\"size\":[\"1.3rem\",\"1.2rem\",\"1.1rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.5,1.5,1.5],\"lineType\":\"em\",\"fontStyle\":\"italic\",\"margin\":[{\"desk\":[\"\",\"\",\"50px\",\"\"],\"tablet\":[\"\",\"\",\"40px\",\"\"],\"mobile\":[\"\",\"\",\"35px\",\"\"]}]} -->\n<div class=\"wp-block-kadence-advancedtext has-text-align-center\" style=\"color:#ffffff;font-size:1.3rem;line-height:1.5em;font-style:italic;margin-bottom:50px\">✨「一杯のお茶から始まる、特別な一日。」</div>\n<!-- /wp:kadence/advancedtext -->\n\n<!-- wp:kadence/rowlayout {\"uniqueID\":\"_herobuttons\",\"columns\":2,\"colLayout\":\"equal\",\"tabletLayout\":\"equal\",\"columnGutter\":\"default\"} -->\n<div class=\"wp-block-kadence-rowlayout alignnone kt-row-layout-inner kt-layout-id_herobuttons\">\n\n<!-- wp:kadence/column {\"uniqueID\":\"_herobtn1col\"} -->\n<div class=\"wp-block-kadence-column kadence-column_herobtn1col\">\n\n<!-- wp:kadence/advancedbutton {\"uniqueID\":\"_herobtn1\",\"text\":\"📋 おしながきを見る\",\"link\":\"#menu\",\"target\":\"_self\",\"size\":\"large\",\"paddingDesktop\":[15,30,15,30],\"colorText\":\"#ffffff\",\"background\":\"rgba(47,82,51,0.95)\",\"backgroundHover\":\"#2F5233\",\"borderRadius\":8} -->\n<div class=\"wp-block-kadence-advancedbutton kt-btn-size-large kt-btn-style-basic\"><a class=\"kt-button button kt-btn-id_herobtn1\" href=\"#menu\" style=\"color:#ffffff;background:rgba(47,82,51,0.95);padding:15px 30px;border-radius:8px\">📋 おしながきを見る</a></div>\n<!-- /wp:kadence/advancedbutton -->\n\n</div>\n<!-- /wp:kadence/column -->\n\n<!-- wp:kadence/column {\"uniqueID\":\"_herobtn2col\"} -->\n<div class=\"wp-block-kadence-column kadence-column_herobtn2col\">\n\n<!-- wp:kadence/advancedbutton {\"uniqueID\":\"_herobtn2\",\"text\":\"🗺️ アクセス情報\",\"link\":\"#access\",\"target\":\"_self\",\"size\":\"large\",\"paddingDesktop\":[15,30,15,30],\"colorText\":\"#2F5233\",\"background\":\"rgba(245,230,211,0.95)\",\"backgroundHover\":\"#F5E6D3\",\"borderRadius\":8} -->\n<div class=\"wp-block-kadence-advancedbutton kt-btn-size-large kt-btn-style-basic\"><a class=\"kt-button button kt-btn-id_herobtn2\" href=\"#access\" style=\"color:#2F5233;background:rgba(245,230,211,0.95);padding:15px 30px;border-radius:8px\">🗺️ アクセス情報</a></div>\n<!-- /wp:kadence/advancedbutton -->\n\n</div>\n<!-- /wp:kadence/column -->\n\n</div>\n<!-- /wp:kadence/rowlayout -->\n\n</div>\n<!-- /wp:kadence/column -->\n\n</div>\n<!-- /wp:kadence/rowlayout -->\n\n<!-- wp:kadence/rowlayout {\"uniqueID\":\"_concept002\",\"columns\":2,\"colLayout\":\"equal\",\"tabletLayout\":\"equal\",\"columnGutter\":\"wider\",\"padding\":[\"xxl\",\"lg\",\"xxl\",\"lg\"],\"background\":[{\"type\":\"color\",\"color\":\"#ffffff\"}],\"htmlAnchor\":\"concept\"} -->\n<div id=\"concept\" class=\"wp-block-kadence-rowlayout alignnone kt-row-layout-inner kt-layout-id_concept002 kt-row-has-bg\">\n\n<!-- wp:kadence/column {\"uniqueID\":\"_conceptcol1\",\"verticalAlignment\":\"middle\"} -->\n<div class=\"wp-block-kadence-column kadence-column_conceptcol1 kt-col-vertical-align-middle\">\n\n<!-- wp:kadence/advancedheading {\"uniqueID\":\"_concepttitle\",\"level\":2,\"color\":\"#2F5233\",\"size\":[\"2.8rem\",\"2.4rem\",\"2.1rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.2,1.2,1.3],\"lineType\":\"em\",\"fontWeight\":\"700\",\"margin\":[{\"desk\":[\"\",\"\",\"40px\",\"\"],\"tablet\":[\"\",\"\",\"35px\",\"\"],\"mobile\":[\"\",\"\",\"30px\",\"\"]}]} -->\n<h2 id=\"kt-adv-heading_concepttitle\" class=\"wp-block-kadence-advancedheading\" style=\"color:#2F5233;font-size:2.8rem;line-height:1.2em;font-weight:700;margin-bottom:40px\">🌸 コンセプト<br>「茶婆場へようこそ」</h2>\n<!-- /wp:kadence/advancedheading -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_concepttext1\",\"color\":\"#555555\",\"size\":[\"1.15rem\",\"1.05rem\",\"1rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.7,1.7,1.7],\"lineType\":\"em\",\"margin\":[{\"desk\":[\"\",\"\",\"25px\",\"\"],\"tablet\":[\"\",\"\",\"22px\",\"\"],\"mobile\":[\"\",\"\",\"20px\",\"\"]}]} -->\n<div class=\"wp-block-kadence-advancedtext\" style=\"color:#555555;font-size:1.15rem;line-height:1.7em;margin-bottom:25px\">🗾 スタッフの出身地（UC=福岡、春日=広島、なっちゃん=栃木、こまっちゃん=山梨）のお茶が楽しめる、一日限定の特別な茶Bar。</div>\n<!-- /wp:kadence/advancedtext -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_concepttext2\",\"color\":\"#555555\",\"size\":[\"1.15rem\",\"1.05rem\",\"1rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.7,1.7,1.7],\"lineType\":\"em\",\"margin\":[{\"desk\":[\"\",\"\",\"25px\",\"\"],\"tablet\":[\"\",\"\",\"22px\",\"\"],\"mobile\":[\"\",\"\",\"20px\",\"\"]}]} -->\n<div class=\"wp-block-kadence-advancedtext\" style=\"color:#555555;font-size:1.15rem;line-height:1.7em;margin-bottom:25px\">🍶 お茶を使ったお酒や、手作りのお菓子もご用意してお待ちしています。</div>\n<!-- /wp:kadence/advancedtext -->\n\n<!-- wp:kadence/advancedtext {\"uniqueID\":\"_conceptbelief\",\"color\":\"#FF8C00\",\"size\":[\"1.25rem\",\"1.15rem\",\"1.1rem\"],\"sizeType\":\"px\",\"lineHeight\":[1.5,1.5,1.5],\"lineType\":\"em\",\"fontWeight\":\"600\",\"fontStyle\":\"italic\"} -->\n<div class=\"wp-block-kadence-advancedtext\" style=\"color:#FF8C00;font-size:1.25rem;line-height:1.5em;font-weight:600;font-style:italic\">💫 とりあえずやってみることが茶 Bar ～茶婆場～の信念。</div>\n<!-- /wp:kadence/advancedtext -->\n\n</div>\n<!-- /wp:kadence/column -->\n\n<!-- wp:kadence/column {\"uniqueID\":\"_conceptcol2\"} -->\n<div class=\"wp-block-kadence-column kadence-column_conceptcol2\">\n\n<!-- wp:image {\"id\":12,\"width\":\"500px\",\"height\":\"400px\",\"scale\":\"cover\",\"sizeSlug\":\"full\",\"linkDestination\":\"none\",\"style\":{\"border\":{\"radius\":\"15px\"}}} -->\n<figure class=\"wp-block-image size-full is-resized has-custom-border\"><img src=\"https://chaba-ba.jpn.org/wp-content/uploads/2025/09/uc.jpg\" alt=\"UC\" class=\"wp-image-12\" style=\"border-radius:15px;object-fit:cover;width:500px;height:400px\"/></figure>\n<!-- /wp:image -->\n\n</div>\n<!-- /wp:kadence/column -->\n\n</div>\n<!-- /wp:kadence/rowlayout -->",
    "status": "publish",
    "type": "page"
  }' \
  "${SITE_URL}/wp-json/wp/v2/pages" > /tmp/page_response.json

echo ""
echo "Response:"
cat /tmp/page_response.json

# Extract post URL from response
POST_URL=$(grep -o '"link":"[^"]*' /tmp/page_response.json | cut -d'"' -f4)
POST_ID=$(grep -o '"id":[0-9]*' /tmp/page_response.json | head -1 | cut -d':' -f2)

if [ -n "$POST_URL" ]; then
    echo ""
    echo "✅ Simplified Kadence homepage created successfully!"
    echo "Page ID: $POST_ID"
    echo "Page URL: $POST_URL"
    echo ""
    echo "📸 Member photos uploaded:"
    echo "- UC (ID: 12): https://chaba-ba.jpn.org/wp-content/uploads/2025/09/uc.jpg"
    echo "- Haruhi (ID: 13): https://chaba-ba.jpn.org/wp-content/uploads/2025/09/haruhi.jpg"
    echo "- Na (ID: 14): https://chaba-ba.jpn.org/wp-content/uploads/2025/09/na.jpg"
    echo "- Ko (ID: 15): https://chaba-ba.jpn.org/wp-content/uploads/2025/09/ko.jpg"
    echo ""
    echo "🎯 Manual setup:"
    echo "1. Settings > Reading > Select 'A static page' > Choose this page as homepage"
    echo "2. Customize > Kadence Design > Global Colors > Set Primary: #2F5233, Secondary: #FF8C00"
    echo "3. Header Builder > Add navigation menu"
else
    echo ""
    echo "❌ Failed to create homepage"
fi