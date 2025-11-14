#!/usr/bin/env python3
"""
UCチャットボットをWordPressに統合するスクリプト
"""

import requests
from requests.auth import HTTPBasicAuth
import json

# WordPress credentials
WP_URL = "https://uc.x0.com"
USERNAME = "uc-japan"
APP_PASSWORD = "DSFTuQ8Ss5aGYRl32boMFEKG"  # スペースを削除

def create_chatbot_page():
    """チャットボット説明ページを作成"""

    # Read the embed code
    with open('wordpress-embed-code.html', 'r', encoding='utf-8') as f:
        embed_code = f.read()

    # WordPressページのコンテンツ
    page_content = f"""
<!-- wp:heading -->
<h2>UCについて何でも聞いてみよう！</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>このチャットボットは、UC（中嶋雄士）さんについての質問に答えます。経歴、実績、哲学、会社、プロジェクトなど、何でも聞いてください！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":3}} -->
<h3>使い方</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li>右下のチャットボタンをクリック</li>
<li>質問を入力するか、クイック質問ボタンをクリック</li>
<li>UCについて詳しく知ることができます！</li>
</ul>
<!-- /wp:list -->

<!-- wp:heading {{"level":3}} -->
<h3>よくある質問</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul>
<li>UCって誰ですか？</li>
<li>どんな会社を経営していますか？</li>
<li>サハラマラソンについて教えて</li>
<li>「とりあえず」精神って何ですか？</li>
<li>タイムカプセルについて</li>
<li>例のプールパーティーって？</li>
<li>どんな国に住んだことがありますか？</li>
</ul>
<!-- /wp:list -->

<!-- wp:separator -->
<hr class="wp-block-separator"/>
<!-- /wp:separator -->

<!-- wp:heading {{"level":3}} -->
<h3>セットアップ手順（管理者向け）</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>注意：</strong> チャットボットを動作させるには、バックエンドサーバーを起動する必要があります。</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code># サーバーの起動
cd /home/uc/uc-site
npm start

# または PM2で常駐化
pm2 start chatbot-server.js --name uc-chatbot
pm2 save</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>詳しいセットアップ手順は <code>/home/uc/uc-site/README.md</code> を参照してください。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
{embed_code}
<!-- /wp:html -->
"""

    # Create page data
    page_data = {
        "title": "UCチャットボット",
        "content": page_content,
        "status": "publish",
        "type": "page",
    }

    # Create the page
    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/pages",
        auth=HTTPBasicAuth(USERNAME, APP_PASSWORD),
        json=page_data
    )

    if response.status_code in [200, 201]:
        page = response.json()
        print(f"✅ ページ作成成功！")
        print(f"   ページID: {page['id']}")
        print(f"   URL: {page['link']}")
        return page
    else:
        print(f"❌ ページ作成失敗")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        return None

def add_to_site_footer():
    """サイトのフッターにチャットボットを追加（カスタムHTMLウィジェット経由）"""

    print("\n📝 フッターへの追加方法:")
    print("   1. WordPressダッシュボード > 外観 > ウィジェット")
    print("   2. 'カスタムHTML' ウィジェットをフッターエリアに追加")
    print("   3. wordpress-embed-code.html の内容をペースト")
    print("   4. API_URLをサーバーのURLに変更")
    print("   5. 保存")

def main():
    print("=" * 60)
    print("UCチャットボット - WordPress統合")
    print("=" * 60)

    # Test authentication
    print("\n1️⃣ 認証テスト...")
    response = requests.get(
        f"{WP_URL}/wp-json/wp/v2/users/me",
        auth=HTTPBasicAuth(USERNAME, APP_PASSWORD)
    )

    if response.status_code == 200:
        user = response.json()
        print(f"   ✅ 認証成功: {user.get('name', 'N/A')}")
    else:
        print(f"   ❌ 認証失敗")
        return

    # Create chatbot page
    print("\n2️⃣ チャットボットページ作成...")
    page = create_chatbot_page()

    if page:
        print("\n" + "=" * 60)
        print("✨ WordPressへの統合が完了しました！")
        print("=" * 60)
        print(f"\n📄 作成されたページ: {page['link']}")
        print("\n⚠️ 次のステップ:")
        print("   1. チャットボットサーバーを起動してください:")
        print("      cd /home/uc/uc-site && npm start")
        print("\n   2. wordpress-embed-code.html のAPI_URLを更新:")
        print("      現在: http://localhost:3000/api/chat")
        print("      変更後: https://your-server-url:3000/api/chat")
        print("\n   3. サーバーを本番環境にデプロイ（推奨）:")
        print("      - PM2で常駐化")
        print("      - Nginxでリバースプロキシ設定")
        print("      - 詳細はREADME.mdを参照")
        print("\n" + "=" * 60)

    # Show footer instructions
    print("\n3️⃣ サイト全体に表示する方法:")
    add_to_site_footer()

if __name__ == "__main__":
    main()
