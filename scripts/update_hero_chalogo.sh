#!/bin/bash

JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

# ホームページのIDを取得
PAGE_ID=$(curl -s "https://uc.x0.com/wp-json/wp/v2/pages?slug=chaba-ba-2" | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['id'])")

# ファイルにHTMLコンテンツを保存
cat > /tmp/hero_content.html << 'EOF'
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>茶葉場 2025 - 福井県池田町で開催される茶摘みイベント</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            background-color: #F5E6D3;
        }

        .hero {
            height: 100vh;
            background-image: url('https://uc.x0.com/wp-content/uploads/2025/01/chalogo.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            position: relative;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.3);
        }

        .hero-content {
            position: relative;
            z-index: 1;
            padding: 2rem;
        }

        .hero-content h1 {
            font-size: clamp(2rem, 5vw, 4rem);
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .hero-content h1 img {
            max-width: 500px;
            width: 100%;
            display: none;
        }

        .hero-content .date {
            font-size: clamp(1rem, 3vw, 1.5rem);
            margin-bottom: 0.5rem;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .hero-content .location {
            font-size: clamp(1rem, 3vw, 1.3rem);
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .hero-content .catchphrase {
            font-size: clamp(1rem, 2.5vw, 1.2rem);
            font-style: italic;
            opacity: 0.9;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        nav {
            background: rgba(74, 93, 35, 0.95);
            color: white;
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #FFD700;
        }

        .section {
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section h2 {
            color: #4A5D23;
            margin-bottom: 2rem;
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            text-align: center;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }

        .card h3 {
            color: #4A5D23;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .card p {
            color: #555;
            line-height: 1.8;
        }

        .event-info {
            background: linear-gradient(135deg, #4A5D23 0%, #6B8E23 100%);
            color: white;
            padding: 3rem 2rem;
            margin: 2rem 0;
            border-radius: 15px;
        }

        .event-info h3 {
            color: #FFD700;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .info-item {
            background: rgba(255,255,255,0.1);
            padding: 1.5rem;
            border-radius: 8px;
            backdrop-filter: blur(10px);
        }

        .info-item strong {
            color: #FFD700;
            display: block;
            margin-bottom: 0.5rem;
        }

        footer {
            background: #4A5D23;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
        }

        @media (max-width: 768px) {
            nav ul {
                gap: 1rem;
            }
            
            .section {
                padding: 2rem 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="hero">
        <div class="hero-content">
            <h1><img src="https://uc.x0.com/wp-content/uploads/2025/01/chalogo.png" alt="茶葉場 2025"></h1>
            <div class="date">2025年5月3日（土）〜 5月4日（日）</div>
            <div class="location">福井県今立郡池田町</div>
            <div class="catchphrase">〜茶摘みを通じて、地域の魅力を再発見〜</div>
        </div>
    </div>

    <nav>
        <ul>
            <li><a href="#about">茶葉場について</a></li>
            <li><a href="#event">イベント詳細</a></li>
            <li><a href="#highlights">見どころ</a></li>
            <li><a href="#access">アクセス</a></li>
        </ul>
    </nav>

    <section id="about" class="section">
        <h2>茶葉場について</h2>
        <p style="text-align: center; max-width: 800px; margin: 0 auto; font-size: 1.1rem; color: #555;">
            茶葉場は、福井県池田町で開催される茶摘み体験イベントです。<br>
            地域の豊かな自然と文化に触れながら、参加者全員で茶摘みを楽しみ、<br>
            地域コミュニティの絆を深めることを目的としています。
        </p>
    </section>

    <section id="event" class="section">
        <h2>イベント詳細</h2>
        <div class="event-info">
            <h3>📅 開催情報</h3>
            <div class="info-grid">
                <div class="info-item">
                    <strong>日時</strong>
                    2025年5月3日（土）〜 5月4日（日）
                </div>
                <div class="info-item">
                    <strong>場所</strong>
                    福井県今立郡池田町
                </div>
                <div class="info-item">
                    <strong>参加費</strong>
                    無料（事前申込制）
                </div>
                <div class="info-item">
                    <strong>定員</strong>
                    各日50名様
                </div>
            </div>
        </div>

        <div class="cards">
            <div class="card">
                <h3>🍵 茶摘み体験</h3>
                <p>地元の茶農家さんの指導のもと、本格的な茶摘み体験ができます。摘んだ茶葉はお持ち帰りいただけます。</p>
            </div>
            <div class="card">
                <h3>🏞️ 自然散策</h3>
                <p>池田町の美しい自然を満喫できるガイド付き散策ツアー。四季折々の景色をお楽しみください。</p>
            </div>
            <div class="card">
                <h3>🍱 地元グルメ</h3>
                <p>池田町の新鮮な食材を使った特製ランチをご用意。地域の味覚をお楽しみいただけます。</p>
            </div>
        </div>
    </section>

    <section id="highlights" class="section" style="background: white; margin: 2rem auto; border-radius: 15px;">
        <h2>見どころ</h2>
        <div class="cards">
            <div class="card">
                <h3>🌱 茶文化体験</h3>
                <p>日本の茶文化について学び、実際に茶道の基本を体験できます。</p>
            </div>
            <div class="card">
                <h3>👥 地域交流</h3>
                <p>地元の方々との交流を通じて、池田町の魅力を深く知ることができます。</p>
            </div>
            <div class="card">
                <h3>📸 フォトスポット</h3>
                <p>茶畑や自然景観など、SNS映えする撮影スポットが満載です。</p>
            </div>
        </div>
    </section>

    <section id="access" class="section">
        <h2>アクセス</h2>
        <div class="card" style="max-width: 800px; margin: 0 auto;">
            <h3>🚗 お車でお越しの方</h3>
            <p>北陸自動車道 武生ICより約30分<br>無料駐車場完備</p>
            
            <h3 style="margin-top: 2rem;">🚃 公共交通機関でお越しの方</h3>
            <p>JR武生駅よりバスで約40分<br>「池田町役場前」下車徒歩5分</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 茶葉場実行委員会 All rights reserved.</p>
        <p style="margin-top: 0.5rem; opacity: 0.8;">お問い合わせ: info@chaba-ba.jpn.org</p>
    </footer>
</body>
</html>
EOF

# JSONペイロードを作成
python3 << 'PYTHON'
import json
import sys

with open('/tmp/hero_content.html', 'r') as f:
    content = f.read()

payload = {
    "content": content
}

with open('/tmp/payload.json', 'w') as f:
    json.dump(payload, f)
PYTHON

# コンテンツを更新
curl -X POST "https://uc.x0.com/wp-json/wp/v2/pages/${PAGE_ID}" \
  -H "Authorization: Bearer ${JWT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @/tmp/payload.json

echo ""
echo "✅ ヒーローセクションの背景をchalogo.pngに更新しました"
