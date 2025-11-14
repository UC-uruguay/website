#!/bin/bash

# 茶Bar ～茶婆場～ ウェブサイト更新スクリプト

echo "🍵 茶Bar ～茶婆場～ ウェブサイト更新を開始します..."

# JWTトークン
JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# まず、メンバー写真をアップロード
echo "📸 メンバー写真をアップロード中..."

# UCの写真をアップロード
echo "アップロード中: uc.jpg"
curl -X POST "https://chaba-ba.jpn.org/wp-json/wp/v2/media" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Disposition: attachment; filename=uc.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/home/uc/uc.jpg > /tmp/uc_upload.json 2>/dev/null

echo "アップロード中: haruhi.jpg"
curl -X POST "https://chaba-ba.jpn.org/wp-json/wp/v2/media" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Disposition: attachment; filename=haruhi.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/home/uc/haruhi.jpg > /tmp/haruhi_upload.json 2>/dev/null

echo "アップロード中: na.jpg"
curl -X POST "https://chaba-ba.jpn.org/wp-json/wp/v2/media" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Disposition: attachment; filename=na.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/home/uc/na.jpg > /tmp/na_upload.json 2>/dev/null

echo "アップロード中: ko.jpg"
curl -X POST "https://chaba-ba.jpn.org/wp-json/wp/v2/media" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Disposition: attachment; filename=ko.jpg" \
  -H "Content-Type: image/jpeg" \
  --data-binary @/home/uc/ko.jpg > /tmp/ko_upload.json 2>/dev/null

# 簡単なHTMLコンテンツでページを作成/更新
echo "📝 ページコンテンツを更新中..."

# 簡潔なHTML作成（WordPressでも表示できる形式）
html_content='<div style="font-family: Hiragino Kaku Gothic Pro, Meiryo, sans-serif; line-height: 1.6; color: #2c3e2d; background: #faf9f7; padding: 20px;">

<header style="background: linear-gradient(135deg, #4a5d23 0%, #6b7c32 100%); color: white; padding: 40px 20px; text-align: center; border-radius: 15px; margin-bottom: 30px;">
  <h1 style="font-size: 2.5rem; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">茶Bar 〜茶婆場〜</h1>
  <p style="font-size: 1.2rem; margin-bottom: 20px; opacity: 0.9;">お茶の魅力を多角的に楽しめる体験型お茶バー</p>
</header>

<section style="background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);">
  <h2 style="color: #4a5d23; font-size: 2rem; margin-bottom: 20px; text-align: center;">🍵 イベント開催情報</h2>
  <div style="text-align: center; font-size: 1.1rem;">
    <p><strong style="color: #6b7c32;">📅 開催日：</strong>2025年10月18日（土）※時間未定</p>
    <p style="font-size: 0.9rem; margin-left: 2rem;">（日曜日開催の可能性もあります：10月19日（日））</p>
    <p><strong style="color: #6b7c32;">📍 場所：</strong>未定（決定次第更新いたします）</p>
    <p><strong style="color: #6b7c32;">🎯 対象：</strong>一般のお客様（どなたでも大歓迎！）</p>
  </div>
</section>

<section style="background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);">
  <h2 style="color: #4a5d23; font-size: 1.8rem; margin-bottom: 20px; text-align: center;">コンセプト</h2>
  <p style="text-align: center; font-size: 1.1rem; line-height: 1.8;">
    お茶の魅力を多角的に楽しめる体験型のお茶バー。<br>
    お茶初心者から愛好家まで、誰もが気軽に立ち寄れる温かい空間を目指します。<br>
    お酒好きの方にも楽しんでいただけるよう、お茶のお酒もご提供いたします。
  </p>
</section>

<section style="background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);">
  <h2 style="color: #4a5d23; font-size: 1.8rem; margin-bottom: 20px; text-align: center;">🍃 商品・メニュー</h2>
  
  <h3 style="color: #4a5d23; margin: 20px 0 10px 0;">各地のお茶</h3>
  <ul style="list-style: none; padding-left: 0;">
    <li style="padding: 5px 0;">🌱 <strong>福岡</strong>：八女茶をはじめとする銘茶</li>
    <li style="padding: 5px 0;">🌱 <strong>広島</strong>：地元の香り豊かなお茶</li>
    <li style="padding: 5px 0;">🌱 <strong>栃木</strong>：自然の恵みあふれるお茶</li>
    <li style="padding: 5px 0;">🌱 <strong>山梨</strong>：山の清涼感あるお茶</li>
    <li style="padding: 5px 0;">🌱 <strong>飲み比べセット</strong>：地域の味を楽しむ</li>
    <li style="padding: 5px 0;">🌱 <strong>オリジナルブレンド体験</strong>：お好みの茶葉をブレンド</li>
  </ul>
  <p style="margin-top: 10px; font-style: italic; color: #6b7c32;">※「お茶漬け」「おにぎり」などの軽食も検討中</p>

  <h3 style="color: #4a5d23; margin: 20px 0 10px 0;">🍰 お茶のお菓子</h3>
  <ul style="list-style: none; padding-left: 0;">
    <li style="padding: 5px 0;">🍃 <strong>抹茶ティラミス</strong>：濃厚な抹茶の風味</li>
    <li style="padding: 5px 0;">🍃 <strong>カスタムお団子</strong>：きなこ・あんこ・黒蜜・黒ゴマから選択</li>
    <li style="padding: 5px 0;">🍃 <strong>抹茶ベースお菓子</strong>：季節の和スイーツ</li>
    <li style="padding: 5px 0;">🍃 <strong>ほうじ茶お菓子</strong>：香ばしさを楽しむ</li>
  </ul>

  <h3 style="color: #4a5d23; margin: 20px 0 10px 0;">🎁 オリジナルグッズ</h3>
  <ul style="list-style: none; padding-left: 0;">
    <li style="padding: 5px 0;">🎀 <strong>SUZURIグッズ</strong>：ソックス・ハンカチ</li>
    <li style="padding: 5px 0;">🎀 <strong>プラ板キーホルダー</strong>：手作りの温もり</li>
    <li style="padding: 5px 0;">🎀 <strong>ビーズキーホルダー</strong>：ドット絵デザイン</li>
    <li style="padding: 5px 0;">🎀 <strong>オリジナルブレンド茶葉</strong>：メンバー厳選</li>
    <li style="padding: 5px 0;">🎀 <strong>茶柱のお守り</strong>：運気アップの可愛いアイテム</li>
  </ul>
</section>

<section style="background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);">
  <h2 style="color: #4a5d23; font-size: 1.8rem; margin-bottom: 20px; text-align: center;">🎉 企画・イベント</h2>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
    <div style="text-align: center; padding: 20px; border: 2px solid #c8d5b9; border-radius: 10px;">
      <div style="font-size: 2rem; margin-bottom: 10px;">🌿</div>
      <h3 style="color: #4a5d23; margin-bottom: 10px;">茶柱立てたい</h3>
      <p>運試し体験！茶柱を立てて幸運をつかみましょう。</p>
    </div>
    
    <div style="text-align: center; padding: 20px; border: 2px solid #c8d5b9; border-radius: 10px;">
      <div style="font-size: 2rem; margin-bottom: 10px;">🏆</div>
      <h3 style="color: #4a5d23; margin-bottom: 10px;">お茶割り選手権</h3>
      <p>お客様参加型イベント！あなたのお茶割り技術を競い合いましょう。</p>
    </div>
    
    <div style="text-align: center; padding: 20px; border: 2px solid #c8d5b9; border-radius: 10px;">
      <div style="font-size: 2rem; margin-bottom: 10px;">🔮</div>
      <h3 style="color: #4a5d23; margin-bottom: 10px;">お茶占い・お茶診断</h3>
      <p>気軽に楽しめるお茶の世界。あなたにぴったりのお茶を見つけませんか？</p>
    </div>
    
    <div style="text-align: center; padding: 20px; border: 2px solid #c8d5b9; border-radius: 10px;">
      <div style="font-size: 2rem; margin-bottom: 10px;">🗾</div>
      <h3 style="color: #4a5d23; margin-bottom: 10px;">都道府県お茶当て</h3>
      <p>日本地図を使ったゲーム形式！各地のお茶の特徴を当ててみましょう。</p>
    </div>
  </div>
</section>

<section style="background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.08);">
  <h2 style="color: #4a5d23; font-size: 1.8rem; margin-bottom: 20px; text-align: center;">👥 メンバー紹介</h2>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
    <div style="text-align: center; padding: 20px;">
      <img src="uc.jpg" alt="UC" style="width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 10px; border: 3px solid #c8d5b9; object-fit: cover;">
      <div style="font-size: 1.2rem; font-weight: bold; color: #4a5d23; margin-bottom: 5px;">UC</div>
      <div style="color: #6b7c32; font-weight: 500; margin-bottom: 5px;">福岡県出身</div>
      <div style="color: #2c3e2d; font-style: italic;">好きなお茶：緑茶</div>
    </div>
    
    <div style="text-align: center; padding: 20px;">
      <img src="haruhi.jpg" alt="はるきち" style="width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 10px; border: 3px solid #c8d5b9; object-fit: cover;">
      <div style="font-size: 1.2rem; font-weight: bold; color: #4a5d23; margin-bottom: 5px;">はるきち</div>
      <div style="color: #6b7c32; font-weight: 500; margin-bottom: 5px;">広島県出身</div>
      <div style="color: #2c3e2d; font-style: italic;">好きなお茶：マテ茶</div>
    </div>
    
    <div style="text-align: center; padding: 20px;">
      <img src="na.jpg" alt="なっちゃん" style="width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 10px; border: 3px solid #c8d5b9; object-fit: cover;">
      <div style="font-size: 1.2rem; font-weight: bold; color: #4a5d23; margin-bottom: 5px;">なっちゃん</div>
      <div style="color: #6b7c32; font-weight: 500; margin-bottom: 5px;">栃木県出身</div>
      <div style="color: #2c3e2d; font-style: italic;">好きなお茶：ドクダミ茶</div>
    </div>
    
    <div style="text-align: center; padding: 20px;">
      <img src="ko.jpg" alt="こまっちゃん" style="width: 100px; height: 100px; border-radius: 50%; margin: 0 auto 10px; border: 3px solid #c8d5b9; object-fit: cover;">
      <div style="font-size: 1.2rem; font-weight: bold; color: #4a5d23; margin-bottom: 5px;">こまっちゃん</div>
      <div style="color: #6b7c32; font-weight: 500; margin-bottom: 5px;">山梨県出身</div>
      <div style="color: #2c3e2d; font-style: italic;">好きなお茶：ダージリン</div>
    </div>
  </div>
</section>

<section style="background: linear-gradient(135deg, #4a5d23 0%, #6b7c32 100%); color: white; padding: 30px; border-radius: 15px; text-align: center;">
  <h2 style="margin-bottom: 20px; font-size: 1.8rem;">📍 店舗情報・アクセス</h2>
  <h3 style="margin-bottom: 10px; font-size: 1.5rem;">開催場所について</h3>
  <p style="font-size: 1.1rem; opacity: 0.9;">
    現在、開催場所を調整中です。<br>
    決定次第、こちらのページにて詳細なアクセス情報を掲載いたします。<br>
    最新情報をお待ちください！
  </p>
</section>

<footer style="background: #2c3e2d; color: white; text-align: center; padding: 20px; border-radius: 15px; margin-top: 30px;">
  <p>&copy; 2025 茶Bar 〜茶婆場〜 All rights reserved.</p>
  <p style="font-size: 0.9rem; opacity: 0.8;">お茶の魅力を多角的に楽しめる体験型お茶バーへようこそ</p>
</footer>

</div>'

# HTMLコンテンツをエンコード
encoded_content=$(echo "$html_content" | sed 's/"/\\"/g' | tr '\n' ' ')

# 新しいページを作成
echo "新しいページを作成中..."
response=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -d "{
    \"title\": \"茶Bar ～茶婆場～\", 
    \"content\": \"$encoded_content\",
    \"status\": \"publish\",
    \"slug\": \"chababa\"
  }" \
  "https://chaba-ba.jpn.org/wp-json/wp/v2/pages")

echo "作成結果: $response"

# ホームページの更新も試行
echo "ホームページを更新中..."
homepage_response=$(curl -s -X PUT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -d "{
    \"title\": \"茶Bar ～茶婆場～\", 
    \"content\": \"$encoded_content\",
    \"status\": \"publish\"
  }" \
  "https://chaba-ba.jpn.org/wp-json/wp/v2/pages/1")

echo "ホームページ更新結果: $homepage_response"

echo "🎉 茶Bar ～茶婆場～ ウェブサイト更新完了！"
echo "サイトをご確認ください: https://chaba-ba.jpn.org"