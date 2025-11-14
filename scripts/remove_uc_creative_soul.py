#!/usr/bin/env python3
import requests
import json
from datetime import datetime

# 認証情報を読み込み
with open('/home/uc/wordpress_auth.json', 'r') as f:
    auth = json.load(f)

base_url = auth['site_url'] + '/wp-json/wp/v2'
headers = {
    'Authorization': f'Basic {auth["base64_token"]}',
    'Content-Type': 'application/json'
}

def update_page_content(page_id, new_content):
    """ページのコンテンツを更新"""
    url = f"{base_url}/pages/{page_id}"
    data = {'content': new_content}
    
    response = requests.post(url, json=data, headers=headers)
    return response

def get_pages():
    """全ページを取得"""
    url = f"{base_url}/pages"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

def remove_uc_creative_soul_text():
    """「UC-Creative Soul from Japan」テキストを削除"""
    pages = get_pages()
    
    for page in pages:
        content = page['content']['rendered']
        title = page['title']['rendered']
        
        print(f"チェック中: {title}")
        
        # 「UC-Creative Soul from Japan」を含むかチェック
        if 'UC-Creative Soul from Japan' in content or 'UC-Creative Soul from Japan' in title:
            print(f"「UC-Creative Soul from Japan」が見つかりました: {title}")
            
            # コンテンツから削除
            new_content = content.replace('UC-Creative Soul from Japan', '')
            new_content = new_content.replace('<h1>UC-Creative Soul from Japan</h1>', '')
            new_content = new_content.replace('<h2>UC-Creative Soul from Japan</h2>', '')
            new_content = new_content.replace('<h3>UC-Creative Soul from Japan</h3>', '')
            
            # 余分な改行や空白を整理
            new_content = new_content.replace('\n\n\n', '\n\n')
            new_content = new_content.strip()
            
            # ページを更新
            response = update_page_content(page['id'], new_content)
            
            if response.status_code == 200:
                print(f"✅ 更新完了: {title}")
            else:
                print(f"❌ 更新失敗: {title} - {response.status_code}")
                print(response.text)

def main():
    print("「UC-Creative Soul from Japan」の削除を開始します...")
    remove_uc_creative_soul_text()
    print("処理完了")

if __name__ == "__main__":
    main()