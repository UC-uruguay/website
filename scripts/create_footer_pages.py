#!/usr/bin/env python3
"""
Create fun footer pages for UC's personal website
"""
import urllib.request
import json

# Load auth info
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth_info = json.load(f)

site_url = auth_info['site_url']
token = auth_info['base64_token']

print("🎉 Creating fun footer pages for UC's site...")

def create_page(title, slug, content):
    """Create a new WordPress page"""
    try:
        page_data = {
            "title": title,
            "content": content,
            "status": "publish",
            "slug": slug
        }
        
        data = json.dumps(page_data).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/pages", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        print(f"✅ Created page: {title} (ID: {result.get('id')})")
        return result.get('id')
        
    except Exception as e:
        print(f"❌ Error creating {title}: {e}")
        return None

# Team Page - UC's "team" (family)
team_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🏠 Team UC（って言っても家族だけど）</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>え？チーム？って思ったでしょ？まあ確かに僕のプライベートサイトなんで、「チーム」って言えるのは家族くらいなんですよね。でも最高のチームです！👨‍👩‍👦</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👨 UC（ゆーし）- CEO（Chief Everything Officer）</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>本名：中島雄志（なかしまゆうし）<br>
役職：何でも屋<br>
特技：妻と息子の可愛さを語り続けること、タイムカプセルを世界各地に埋めること<br>
弱点：ワインを見ると我慢できない、新しい友達を作りすぎる</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👩 妻 - CFO（Chief Fun Officer）</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>役職：家族の太陽<br>
特技：UCを現実世界に引き戻すこと、息子のエネルギーについていくこと<br>
コメント：「またタイムカプセル埋めてきたの？」</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👶 イチユ（イチくん）- CPO（Chief Play Officer）</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>年齢：もうすぐ3歳<br>
役職：最高遊び責任者<br>
特技：パパママを笑顔にすること、好奇心で家中を探検すること<br>
座右の銘：「なんで？なんで？なんで？」</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 チーム理念</h2>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote">
<p>「笑顔と好奇心で世界とつながろう」</p>
<cite>— Team UC家族憲章より</cite>
</blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>そんな感じで、小さいけれど愛にあふれたチームです。たまにカオスになるけど、それも含めて最高！</p>
<!-- /wp:paragraph -->'''

# History Page
history_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📚 UCの謎多き歴史</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>僕の人生、振り返ってみるとなかなかカオスで面白いんですよ。時系列で並べてみました！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🍼 幼少期（1990年代前半）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>山梨県で誕生。既にこの頃から「ちょっと変わった子」と言われる</li>
<li>初めての友達づくり開始。保育園で「みんな友達になろう！」精神を発動</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📚 学生時代（1990年代後半〜2010年代前半）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>勉強そっちのけで友達づくりに夢中</li>
<li>「なんか面白いことやりたい」病を発症</li>
<li>大学時代：哲学と人生の意味について夜な夜な語る青春を過ごす</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💼 社会人デビュー（2010年代）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>「普通のサラリーマンは僕には無理かも」と薄々気づく</li>
<li>旅行にハマる。47都道府県制覇を目指し始める</li>
<li>ワインとの運命的出会い。「これは人生を豊かにする！」</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💕 運命の出会い（2010年代後半）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>今の妻と出会う。「この人なら僕の変さを受け入れてくれそう」</li>
<li>プロポーズ時にタイムカプセルを埋める。ロマンチックなのか変なのか微妙</li>
<li>結婚。妻「やっぱり変だったけど、それがいい」</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">👶 パパになる（2020年代前半）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>イチくん誕生。親バカ街道まっしぐら</li>
<li>「息子のために世界をもっと面白くしたい」と謎の使命感に燃える</li>
<li>AI技術にハマる。「これで息子の教育ゲーム作れる！」</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌐 現在（2025年）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>このサイトを開設。「世界中の人と友達になりたい」願望を実現中</li>
<li>タイムカプセルコレクション：世界各地に約40個埋設済み</li>
<li>友達作りは相変わらず続行中。目標は「世界中に友達を作ること」</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🔮 未来の野望</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>宗教を超えた世界的な相互理解の実現（壮大すぎ？）</li>
<li>息子と一緒にタイムカプセルを掘り返す日</li>
<li>ジブリみたいなカフェを作りたい（妻との共通の夢）</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>こんな感じで、普通じゃない人生を歩んでますが、毎日楽しいです！</p>
<!-- /wp:paragraph -->'''

# Careers Page
careers_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">💼 一緒に働く？（求人情報）</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>え、プライベートサイトなのに求人？って思いました？まあ、一応書いてみました。でも本気で一緒に何かやりたい人がいたら嬉しいです！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 現在募集中のポジション</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">1. 友達（フルタイム・パートタイム問わず）</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>職務内容：</strong><br>
・一緒に笑うこと<br>
・面白いことを企画すること<br>
・ワインを飲みながら人生について語ること<br>
・たまにタイムカプセルを埋めに行くこと</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>応募資格：</strong><br>
・人生を楽しむ気持ちがある方<br>
・変わった発想を面白がれる方<br>
・子供の話を聞いて「可愛いね」と言ってくれる方</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>待遇：</strong><br>
・給料：笑顔と友情（プライスレス）<br>
・福利厚生：美味しいワインの情報共有<br>
・昇進：親友まで昇格可能</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">2. 創作パートナー（業務委託）</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>職務内容：</strong><br>
・AI音楽制作の相談相手<br>
・息子の教育ゲームのアイデア出し<br>
・ショートフィルム制作のお手伝い</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>応募資格：</strong><br>
・創造力に自信のある方<br>
・「それ面白そう！」が口癖の方<br>
・技術よりも情熱重視</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">3. 旅の同行者（不定期）</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>職務内容：</strong><br>
・温泉巡りのお供<br>
・お寺参拝の付き添い<br>
・タイムカプセル埋設の立会人</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>応募資格：</strong><br>
・好奇心旺盛な方<br>
・家族連れOKな方（イチくんも一緒の場合あり）<br>
・「なんでそんなところにタイムカプセル埋めるの？」と聞かない方</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📝 応募方法</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>履歴書とかいりません！以下の方法でお気軽にどうぞ：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>Instagram @toriaezu_uc にDM</li>
<li>X（Twitter）@TORIAEZU_OU にリプライ</li>
<li>実際に会ったときに「あ、求人見ました」と言う</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>注意事項：</strong><br>
これは半分冗談、半分本気です。でも本当に一緒に何か面白いことをやりたい方は大歓迎！</p>
<!-- /wp:paragraph -->'''

# Privacy Policy
privacy_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">🔒 プライバシーポリシー（まじめに書いたよ）</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>普段はふざけてばかりの僕ですが、プライバシーについてはちゃんと考えてます。安心してサイトを見てくださいね！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📊 どんな情報を収集するの？</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>自動的に収集される情報：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>IPアドレス（でも個人を特定するためじゃないよ）</li>
<li>ブラウザの種類（Chrome派？Firefox派？）</li>
<li>アクセス時間（深夜に見てる人、お疲れ様！）</li>
<li>どのページを見たか（ブログが人気です）</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>あなたが教えてくれる情報：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>コメントを書いてくれた時の名前とメールアドレス</li>
<li>お問い合わせフォームからの内容</li>
<li>SNSでメッセージをくれた時の情報</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🤔 その情報、何に使うの？</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>サイトをもっと見やすくするため</li>
<li>あなたからのメッセージにお返事するため</li>
<li>スパムコメントを防ぐため</li>
<li>「このページ人気だな」って分析するため</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>絶対にやらないこと：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>あなたの情報を他の人に売る（そんなことしません！）</li>
<li>変な広告を送りまくる</li>
<li>個人的な詮索をする</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🍪 クッキーについて</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>お菓子のクッキーじゃないよ！ウェブサイトのクッキーです。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>サイトを使いやすくするために使ってます</li>
<li>Google Analyticsでアクセス解析してます</li>
<li>嫌だったらブラウザ設定で無効にできます</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🛡️ 情報の保護</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>あなたの情報は大切に扱います：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>SSL暗号化でサイトを保護</li>
<li>定期的にセキュリティをチェック</li>
<li>必要以上に情報は保存しません</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">❓ 質問や削除依頼</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>「自分の情報を削除して」「これってどうなの？」など、なんでも気軽に聞いてください！</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>連絡先：</strong><br>
Instagram: @toriaezu_uc<br>
X(Twitter): @TORIAEZU_OU</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>最終更新：</strong>2025年9月（ちょくちょく更新します）</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>このポリシーを読んでくれてありがとう！質問があったらいつでもどうぞ〜</em></p>
<!-- /wp:paragraph -->'''

# Terms and Conditions
terms_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📜 利用規約（かしこまった感じで書いてみた）</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>まあ、個人サイトなんで堅苦しい規約はいらないと思うんですが、一応書いておきますね。基本的に「みんなで楽しくやろう」ってことです！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎯 このサイトの使い方</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>OK：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>記事を読んで楽しむ</li>
<li>写真を見て「いいなー」って思う</li>
<li>コメントで感想を教える</li>
<li>SNSでシェアしてくれる（すごく嬉しい！）</li>
<li>友達に「面白いサイトがあるよ」と紹介する</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>NG：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>誹謗中傷（みんなで楽しくやりましょう）</li>
<li>スパムコメント（邪魔です）</li>
<li>コンテンツの無断転載（一言言ってくれればOK）</li>
<li>他の人に迷惑をかける行為</li>
<li>変な商品の宣伝（お断り）</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📝 コメントについて</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>基本的に何でも歓迎！感想、質問、雑談なんでもどうぞ</li>
<li>でも他の人が嫌な気持ちになるコメントはダメ</li>
<li>僕が「これはちょっと...」と思ったら削除することがあります</li>
<li>返事は頑張ってしますが、遅れることもあります（ごめん）</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📷 写真と動画について</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>基本的に僕が撮影したものか、許可を得たものです</li>
<li>家族の写真も載せてますが、プライバシーには気をつけてます</li>
<li>もし「この写真使わないで」ってことがあったら教えてください</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🔗 リンクについて</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>このサイトにリンクを貼る：</strong><br>
大歓迎！事前連絡も不要です。どんどん紹介してください！</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>このサイトから外部リンク：</strong><br>
面白いサイトや参考になるサイトにリンクを貼ることがあります。でも、リンク先の内容については責任持てません。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">⚠️ 免責事項（一応書いとく）</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>情報は正確に書くよう心がけてますが、間違いがあったらごめんなさい</li>
<li>サイトの内容で何か損害があっても責任は取れません（個人サイトなので）</li>
<li>予告なしにコンテンツを変更することがあります</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🤝 最終的には...</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>難しいことは置いといて、みんなで楽しくやりましょう！</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>相手を思いやる気持ちがあれば大丈夫</li>
<li>わからないことがあったら気軽に聞いてください</li>
<li>一緒に面白いことを作っていきましょう</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>何か質問があったら：</strong><br>
Instagram: @toriaezu_uc<br>
X(Twitter): @TORIAEZU_OU</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>最後まで読んでくれてありがとう！みんなで楽しいサイトにしていきましょう〜</em></p>
<!-- /wp:paragraph -->'''

# Contact Us
contact_content = '''<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">📮 連絡先（お気軽にどうぞ！）</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>何か話したいこと、聞きたいこと、一緒にやりたいことがあったら、遠慮せずに連絡してください！新しい人との出会いが大好きなので、どんなメッセージでも嬉しいです。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🌟 一番返事が早いのはこちら</h2>
<!-- /wp:heading -->

<!-- wp:columns -->
<div class="wp-block-columns">
<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"left"}} -->
<ul class="wp-block-social-links has-visible-labels is-style-logos-only">
<!-- wp:social-link {"url":"https://www.instagram.com/toriaezu_uc","service":"instagram"} -->
<li class="wp-block-social-link wp-social-link-instagram">
<a href="https://www.instagram.com/toriaezu_uc" class="wp-block-social-link-anchor">Instagram</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:paragraph -->
<p><strong>@toriaezu_uc</strong><br>
日常の写真とか、息子の可愛い様子とか載せてます。DMで話しかけてくれたら嬉しいです！</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column">
<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"className":"is-style-logos-only","layout":{"type":"flex","justifyContent":"left"}} -->
<ul class="wp-block-social-links has-visible-labels is-style-logos-only">
<!-- wp:social-link {"url":"https://x.com/TORIAEZU_OU","service":"x"} -->
<li class="wp-block-social-link wp-social-link-x">
<a href="https://x.com/TORIAEZU_OU" class="wp-block-social-link-anchor">X (Twitter)</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:paragraph -->
<p><strong>@TORIAEZU_OU</strong><br>
思ったことをつぶやいてます。リプライやDMお待ちしてます！</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">📱 その他のSNS</h2>
<!-- /wp:heading -->

<!-- wp:social-links {"openInNewTab":true,"showLabels":true,"layout":{"type":"flex","justifyContent":"left","flexWrap":"wrap"}} -->
<ul class="wp-block-social-links has-visible-labels">
<!-- wp:social-link {"url":"https://www.facebook.com/yushi.nakashima/","service":"facebook"} -->
<li class="wp-block-social-link wp-social-link-facebook">
<a href="https://www.facebook.com/yushi.nakashima/" class="wp-block-social-link-anchor">Facebook</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.tiktok.com/@ucjapan360","service":"tiktok"} -->
<li class="wp-block-social-link wp-social-link-tiktok">
<a href="https://www.tiktok.com/@ucjapan360" class="wp-block-social-link-anchor">TikTok</a>
</li>
<!-- /wp:social-link -->

<!-- wp:social-link {"url":"https://www.linkedin.com/in/yushi-nakashima-084045124/","service":"linkedin"} -->
<li class="wp-block-social-link wp-social-link-linkedin">
<a href="https://www.linkedin.com/in/yushi-nakashima-084045124/" class="wp-block-social-link-anchor">LinkedIn</a>
</li>
<!-- /wp:social-link -->
</ul>
<!-- /wp:social-links -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">💬 こんなメッセージ大歓迎</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>📝 「ブログ読んだよ！」</li>
<li>🍷 「ワインのこと教えて」</li>
<li>🎨 「一緒にクリエイティブなことやろう」</li>
<li>🌏 「今度そっち行くから案内して」</li>
<li>👶 「子育ての話しよう」</li>
<li>🏛️ 「おすすめのお寺教えて」</li>
<li>💭 「人生について語ろう」</li>
<li>🤝 「友達になりたい」</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">⏰ 返事について</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>基本的に24時間以内に返事するように心がけてます！でも、</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>息子と遊んでて遅れることがある</li>
<li>たまに温泉に行って圏外になることがある</li>
<li>ワインを飲みすぎて寝落ちすることがある（ごめん）</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>でも必ず返事しますので、気長に待ってくださいね！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">🎯 特別なお誘い</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>もし山梨に来ることがあったら、ぜひ教えてください！</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<li>🍇 ワイナリー巡りにお連れします</li>
<li>♨️ 隠れた温泉スポット教えます</li>
<li>🏛️ おすすめのお寺案内します</li>
<li>👨‍👩‍👦 よかったら家族でお会いしましょう</li>
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><strong>最後に：</strong><br>
人見知りしないし、年齢や国籍関係なく誰でも歓迎です。一緒に面白いことしましょう！</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em>あなたからの連絡、楽しみに待ってます〜！</em> 🌟</p>
<!-- /wp:paragraph -->'''

# Create all pages
pages = [
    ("Team", "team", team_content),
    ("History", "history", history_content),
    ("Careers", "careers", careers_content),
    ("Privacy Policy", "privacy-policy", privacy_content),
    ("Terms and Conditions", "terms-conditions", terms_content),
    ("Contact Us", "contact", contact_content)
]

created_pages = []
for title, slug, content in pages:
    page_id = create_page(title, slug, content)
    if page_id:
        created_pages.append((title, slug, page_id))

print(f"\n🎉 Created {len(created_pages)} footer pages!")
print("📋 Pages created:")
for title, slug, page_id in created_pages:
    print(f"  - {title}: https://uc.x0.com/{slug}/")

print("\n💡 Next steps:")
print("1. Check the pages on your website")
print("2. Add these pages to your footer menu in WordPress Admin")
print("3. Customize the content as needed")