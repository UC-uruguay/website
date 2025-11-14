#!/bin/bash

echo "🧹 茶Bar 〜茶婆場〜 データ削除スクリプト"
echo "=========================================="
echo ""

# 確認メッセージ
read -p "全てのテストデータを削除しますか？ (y/N): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "キャンセルしました。"
    exit 0
fi

echo ""
echo "データを削除中..."

# 川柳データを削除
if [ -f "senryu_data.json" ]; then
    echo "[]" > senryu_data.json
    echo "✅ 川柳データをクリアしました"
else
    echo "ℹ️  川柳データファイルが見つかりません"
fi

# 茶柱落としゲームデータを削除
if [ -f "chabashira_data.json" ]; then
    echo "[]" > chabashira_data.json
    echo "✅ 茶柱落としゲームデータをクリアしました"
else
    echo "ℹ️  茶柱落としゲームデータファイルが見つかりません"
fi

# チャ友の声データを削除
if [ -f "voices_data.json" ]; then
    echo "[]" > voices_data.json
    echo "✅ チャ友の声データをクリアしました"
else
    echo "ℹ️  チャ友の声データファイルが見つかりません"
fi

# アップロード画像を削除
if [ -d "uploads" ]; then
    rm -rf uploads/*
    echo "✅ アップロード画像を削除しました"
else
    echo "ℹ️  uploadsフォルダが見つかりません"
fi

echo ""
echo "🎉 データ削除完了！"
echo ""
echo "削除されたデータ:"
echo "  - 川柳投稿"
echo "  - 茶柱落としゲームのスコア"
echo "  - チャ友の声"
echo "  - アップロード画像"
echo ""
echo "これでクリーンな状態からイベントを開始できます！"
