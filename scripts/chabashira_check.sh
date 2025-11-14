#!/bin/bash

echo "🔍 茶柱落としゲーム - 診断スクリプト"
echo "================================"
echo ""

# ファイルの存在確認
echo "📁 ファイルの存在確認:"
if [ -f "/home/uc/chabashira.html" ]; then
    echo "✅ chabashira.html が存在します"
else
    echo "❌ chabashira.html が見つかりません"
fi

if [ -f "/home/uc/chabashira_api.php" ]; then
    echo "✅ chabashira_api.php が存在します"
else
    echo "❌ chabashira_api.php が見つかりません"
fi

echo ""
echo "📝 サーバーにアップロードする必要があるファイル:"
echo "   - chabashira.html"
echo "   - chabashira_api.php"
echo ""
echo "🚀 アップロード手順:"
echo "   1. 上記2ファイルをサーバーの同じフォルダにアップロード"
echo "   2. 権限設定: chmod 777 /var/www/html/"
echo "   3. ブラウザでアクセス: https://chaba-ba.jpn.org/chabashira.html"
echo ""
