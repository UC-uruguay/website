#!/usr/bin/env python3
"""
Test Application Password authentication
"""
import urllib.request
import json
import base64

def test_app_password():
    site_url = "https://uc.x0.com"
    username = "uc-japan"
    
    print("🔑 Application Password テスト")
    print("=" * 40)
    
    # Application Passwordを入力してもらう
    app_password = input("Application Password を入力してください (24文字、スペースあり): ").strip()
    
    if not app_password:
        print("❌ Application Password が入力されていません")
        return False
    
    # スペースを削除してBase64エンコード
    clean_password = app_password.replace(' ', '')
    credentials = f"{username}:{clean_password}"
    token = base64.b64encode(credentials.encode()).decode()
    
    print(f"👤 ユーザー: {username}")
    print(f"🔐 認証トークン生成完了")
    
    # ユーザー情報取得テスト
    try:
        print("\n📋 ユーザー情報取得テスト...")
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/users/me")
        request.add_header('Authorization', f'Basic {token}')
        
        with urllib.request.urlopen(request) as response:
            user_data = json.loads(response.read().decode('utf-8'))
            
        print("✅ ユーザー情報取得成功!")
        print(f"   ID: {user_data.get('id')}")
        print(f"   名前: {user_data.get('name')}")
        print(f"   権限: {list(user_data.get('capabilities', {}).keys())[:5]}...")
        
        # 投稿作成権限チェック
        can_publish = user_data.get('capabilities', {}).get('publish_posts', False)
        print(f"   投稿作成権限: {'✅ あり' if can_publish else '❌ なし'}")
        
    except Exception as e:
        print(f"❌ ユーザー情報取得失敗: {e}")
        return False
    
    # テスト投稿作成
    try:
        print("\n📝 テスト投稿作成...")
        test_post = {
            "title": "🧪 Claude Code テスト投稿",
            "content": "<p>これはClaude CodeによるApplication Password認証テストです。</p><p>作成日時: 2025年8月29日</p>",
            "status": "draft",  # 下書きとして作成
            "meta": {
                "test_post": True
            }
        }
        
        data = json.dumps(test_post).encode('utf-8')
        request = urllib.request.Request(f"{site_url}/wp-json/wp/v2/posts", data=data)
        request.add_header('Authorization', f'Basic {token}')
        request.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(request) as response:
            post_data = json.loads(response.read().decode('utf-8'))
            
        print("✅ テスト投稿作成成功!")
        print(f"   投稿ID: {post_data.get('id')}")
        print(f"   タイトル: {post_data.get('title', {}).get('rendered')}")
        print(f"   ステータス: {post_data.get('status')}")
        print(f"   編集URL: {site_url}/wp-admin/post.php?post={post_data.get('id')}&action=edit")
        
        # 成功した認証情報を保存
        auth_info = {
            "username": username,
            "app_password": clean_password,
            "base64_token": token,
            "site_url": site_url
        }
        
        with open('/home/uc/wordpress_auth.json', 'w') as f:
            json.dump(auth_info, f, indent=2)
        
        print("\n💾 認証情報を wordpress_auth.json に保存しました")
        print("🎉 Application Password設定完了！")
        print("🚀 これで Claude Code からの完全自動投稿が可能です")
        
        return True
        
    except Exception as e:
        print(f"❌ テスト投稿作成失敗: {e}")
        return False

if __name__ == "__main__":
    test_app_password()