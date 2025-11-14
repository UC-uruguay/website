#!/bin/bash

echo "🍵 茶Bar ～茶婆場～ 最終アップロード手順"
echo "=================================="

# 新しいJWTトークンを取得してみる
echo "1. 新しいJWTトークン取得を試行中..."
curl -s -X POST "https://chaba-ba.jpn.org/wp-json/jwt-auth/v1/token" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}' > jwt_response.json 2>/dev/null

echo "2. FTPまたはファイルマネージャーでの手動アップロードをお勧めします"
echo ""
echo "📁 アップロード必要ファイル:"
echo "   - index.html (メインサイト)"
echo "   - uc.jpg (UCさんの写真)"
echo "   - haruhi.jpg (はるきちさんの写真)"  
echo "   - na.jpg (なっちゃんさんの写真)"
echo "   - ko.jpg (こまっちゃんさんの写真)"
echo ""
echo "🎯 アップロード先: chaba-ba.jpn.org のルートディレクトリ"
echo ""
echo "📝 または WordPress管理画面から:"
echo "   1. 固定ページ > 新規追加"
echo "   2. index.htmlの内容をコピー＆ペースト"
echo "   3. メディアライブラリに写真をアップロード"
echo ""
echo "✅ 準備完了！すべてのファイルは /home/uc/ にあります"