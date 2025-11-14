#!/bin/bash

# Rsync同期スクリプト

echo "=== Rsync同期セットアップ ==="
echo ""
echo "このスクリプトは、PC（WSL）とスマホ（Termux）をrsyncで同期します。"
echo "前提条件: スマホのTermuxでSSHサーバーが起動していること"
echo ""

# Termux側のSSHサーバーセットアップ手順を表示
show_termux_setup() {
    echo "【スマホ（Termux）側のセットアップ】"
    echo ""
    echo "1. OpenSSHをインストール:"
    echo "   pkg install openssh"
    echo ""
    echo "2. パスワードを設定:"
    echo "   passwd"
    echo ""
    echo "3. SSHサーバーを起動:"
    echo "   sshd"
    echo ""
    echo "4. IPアドレスを確認:"
    echo "   ifconfig wlan0 | grep inet"
    echo ""
    echo "5. ポート番号を確認（通常8022）:"
    echo "   echo \$PREFIX/var/log/sshd.log"
    echo ""
}

# PC側からスマホへ同期
sync_to_phone() {
    echo ""
    read -p "スマホのIPアドレス（例: 192.168.1.100）: " PHONE_IP
    read -p "スマホのユーザー名（通常: u0_aXXX、whoamiで確認）: " PHONE_USER
    read -p "スマホのポート番号（通常: 8022）: " PHONE_PORT
    PHONE_PORT=${PHONE_PORT:-8022}

    echo ""
    echo "PCからスマホへ同期中..."
    rsync -avz --delete \
        --exclude='.git/' \
        --exclude='.cache/' \
        --exclude='.local/' \
        --exclude='archives/' \
        -e "ssh -p $PHONE_PORT" \
        /home/uc/ ${PHONE_USER}@${PHONE_IP}:~/workspace/

    echo "同期完了"
}

# スマホからPCへ同期
sync_from_phone() {
    echo ""
    read -p "スマホのIPアドレス（例: 192.168.1.100）: " PHONE_IP
    read -p "スマホのユーザー名（通常: u0_aXXX、whoamiで確認）: " PHONE_USER
    read -p "スマホのポート番号（通常: 8022）: " PHONE_PORT
    PHONE_PORT=${PHONE_PORT:-8022}

    echo ""
    echo "スマホからPCへ同期中..."
    rsync -avz --delete \
        --exclude='.git/' \
        --exclude='.cache/' \
        --exclude='.local/' \
        --exclude='archives/' \
        -e "ssh -p $PHONE_PORT" \
        ${PHONE_USER}@${PHONE_IP}:~/workspace/ /home/uc/

    echo "同期完了"
}

# メニュー
menu() {
    echo ""
    echo "【メニュー】"
    echo "1. スマホ側のセットアップ手順を表示"
    echo "2. PCからスマホへ同期"
    echo "3. スマホからPCへ同期"
    echo "4. 終了"
    echo ""
    read -p "選択してください (1-4): " choice

    case $choice in
        1) show_termux_setup; menu ;;
        2) sync_to_phone ;;
        3) sync_from_phone ;;
        4) exit 0 ;;
        *) echo "無効な選択です"; menu ;;
    esac
}

menu
