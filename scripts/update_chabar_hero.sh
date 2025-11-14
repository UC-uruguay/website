#!/bin/bash

JWT_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VjLngwLmNvbSIsImlhdCI6MTc1NjgxMDIzNiwiZXhwIjoxNzU2ODEzODM2LCJ1c2VyX2lkIjoxLCJqdGkiOiJCQ08yTTluM2tnN2FNbHRaN2p1N1J6M09pSWl5RXBBayJ9.F89PaKJxhGRzcO4KBjI7GfnEPQ5F0OCEUICX1l__-hY"

PAGE_ID=11

# 現在のコンテンツを取得
CURRENT_CONTENT=$(curl -s "https://uc.x0.com/wp-json/wp/v2/pages/${PAGE_ID}" | python3 -c "import sys, json; print(json.load(sys.stdin)['content']['rendered'])")

# 新しいコンテンツのファイルを作成（ヒーローセクションの背景をchalogo.pngに変更）
cat > /tmp/chabar_updated.html << 'EOF'
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>茶Bar 〜茶婆場〜 | やまなしワインクラス</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            line-height: 1.6;
            color: #333;
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
            background: rgba(0, 0, 0, 0.2);
        }

        .hero-content {
            position: relative;
            z-index: 1;
            padding: 2rem;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 8vw, 5rem);
            margin-bottom: 1rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
        }

        .hero .event-info {
            font-size: clamp(1.2rem, 3vw, 2rem);
            margin-bottom: 0.5rem;
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
            gap: 1.5rem;
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

        .section:nth-child(even) {
            background: #f9f9f9;
        }

        .section h2 {
            color: #4A5D23;
            margin-bottom: 2rem;
            font-size: clamp(2rem, 5vw, 3rem);
            text-align: center;
        }

        .concept {
            text-align: center;
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }

        .menu-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .menu-item {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .menu-item:hover {
            transform: translateY(-5px);
        }

        .menu-item h3 {
            color: #4A5D23;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .team-member {
            text-align: center;
            padding: 1.5rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .team-member h4 {
            color: #4A5D23;
            margin-top: 1rem;
            font-size: 1.3rem;
        }

        .access-info {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
        }

        footer {
            background: #4A5D23;
            color: white;
            text-align: center;
            padding: 2rem;
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            nav ul {
                gap: 1rem;
            }
        }

        .scroll-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #4A5D23;
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1000;
        }

        .scroll-top.visible {
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="hero">
        <div class="hero-content">
            <h1>茶Bar 〜茶婆場〜</h1>
            <div class="event-info">2025年10月19日（日）14:30-17:30</div>
            <div class="event-info">@えびす屋（山梨県甲府市）</div>
        </div>
    </div>

    <nav>
        <ul>
            <li><a href="#concept">コンセプト</a></li>
            <li><a href="#tea-menu">お茶メニュー</a></li>
            <li><a href="#food-menu">フードメニュー</a></li>
            <li><a href="#activities">茶活動</a></li>
            <li><a href="#team">チーム</a></li>
            <li><a href="#access">アクセス</a></li>
        </ul>
    </nav>

    <section id="concept" class="section">
        <h2>コンセプト</h2>
        <div class="concept">
            <p>茶Barは、お茶を通じて人々が集い、語らい、楽しむ新しい形のお茶会です。</p>
            <p>伝統的な茶道の形式にとらわれず、もっと気軽に、もっと自由に、お茶の魅力を楽しんでいただけます。</p>
            <p>様々な種類のお茶と、それに合わせた軽食をご用意してお待ちしています。</p>
        </div>
    </section>

    <section id="tea-menu" class="section">
        <h2>お茶メニュー</h2>
        <div class="menu-grid">
            <div class="menu-item">
                <h3>🍵 煎茶</h3>
                <p>爽やかな香りと旨味が特徴の日本茶の代表格</p>
            </div>
            <div class="menu-item">
                <h3>🍃 玉露</h3>
                <p>濃厚な旨味と甘みを堪能できる高級茶</p>
            </div>
            <div class="menu-item">
                <h3>🌿 抹茶</h3>
                <p>香り高く、健康効果も期待できる粉末茶</p>
            </div>
            <div class="menu-item">
                <h3>🌸 ほうじ茶</h3>
                <p>香ばしい香りとまろやかな味わい</p>
            </div>
        </div>
    </section>

    <section id="food-menu" class="section">
        <h2>フードメニュー</h2>
        <div class="menu-grid">
            <div class="menu-item">
                <h3>🍡 和菓子</h3>
                <p>お茶によく合う季節の和菓子各種</p>
            </div>
            <div class="menu-item">
                <h3>🍰 抹茶スイーツ</h3>
                <p>抹茶を使ったオリジナルデザート</p>
            </div>
            <div class="menu-item">
                <h3>🍙 茶漬け</h3>
                <p>さっぱりとしたお茶漬けで〆の一品</p>
            </div>
        </div>
    </section>

    <section id="activities" class="section">
        <h2>茶活動</h2>
        <div class="menu-grid">
            <div class="menu-item">
                <h3>🎓 お茶の淹れ方講座</h3>
                <p>美味しいお茶の淹れ方を学べます</p>
            </div>
            <div class="menu-item">
                <h3>🎨 茶道体験</h3>
                <p>本格的な茶道の作法を体験</p>
            </div>
            <div class="menu-item">
                <h3>💬 茶話会</h3>
                <p>お茶を飲みながら自由に歓談</p>
            </div>
        </div>
    </section>

    <section id="team" class="section">
        <h2>チーム</h2>
        <div class="team-grid">
            <div class="team-member">
                <h4>茶師 - 田中さん</h4>
                <p>30年の経験を持つベテラン茶師</p>
            </div>
            <div class="team-member">
                <h4>パティシエ - 佐藤さん</h4>
                <p>和と洋を融合させたスイーツ職人</p>
            </div>
            <div class="team-member">
                <h4>茶道家 - 鈴木さん</h4>
                <p>伝統を大切にしながら新しい形を提案</p>
            </div>
        </div>
    </section>

    <section id="access" class="section">
        <h2>アクセス</h2>
        <div class="access-info">
            <h3>会場：えびす屋</h3>
            <p>〒400-0000 山梨県甲府市</p>
            <h3 style="margin-top: 2rem;">アクセス方法</h3>
            <p>JR甲府駅より徒歩10分</p>
            <p>中央自動車道 甲府昭和ICより車で15分</p>
            <h3 style="margin-top: 2rem;">お問い合わせ</h3>
            <p>Email: info@chaba-ba.jpn.org</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 茶Bar 実行委員会 All rights reserved.</p>
    </footer>

    <div class="scroll-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">↑</div>

    <script>
        window.addEventListener('scroll', function() {
            const scrollTop = document.querySelector('.scroll-top');
            if (window.pageYOffset > 300) {
                scrollTop.classList.add('visible');
            } else {
                scrollTop.classList.remove('visible');
            }
        });
    </script>
</body>
</html>
EOF

# JSONペイロードを作成
python3 << 'PYTHON'
import json

with open('/tmp/chabar_updated.html', 'r') as f:
    content = f.read()

payload = {
    "content": content
}

with open('/tmp/chabar_payload.json', 'w') as f:
    json.dump(payload, f)
PYTHON

# コンテンツを更新
curl -X POST "https://uc.x0.com/wp-json/wp/v2/pages/${PAGE_ID}" \
  -H "Authorization: Bearer ${JWT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @/tmp/chabar_payload.json

echo ""
echo "✅ ヒーローセクションの背景をchalogo.pngに更新しました！"
