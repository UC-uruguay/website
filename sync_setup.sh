#!/bin/bash

# Git同期セットアップスクリプト

echo "=== Git同期セットアップ ==="
echo ""
echo "このスクリプトは、PC（WSL）とスマホ（Termux）を同期するためのGit環境を設定します。"
echo ""

# 現在のディレクトリをGitリポジトリとして初期化
init_git() {
    echo "1. Gitリポジトリを初期化..."
    cd /home/uc

    if [ ! -d ".git" ]; then
        git init
        echo "Gitリポジトリを初期化しました"
    else
        echo "既にGitリポジトリです"
    fi

    # .gitignoreを作成
    cat > .gitignore <<EOF
# システムファイル
.cache/
.config/
.local/
.ssh/
.nvm/
.npm/
.docker/
.android/
.gemini/
.codex/

# Claude設定（個別管理）
.claude/
.claude.json
.claude.json.backup

# 一時ファイル
*.log
optional-path-to-log-file
.bash_history
.viminfo
.lesshst
.wget-hsts
.motd_shown

# 認証情報
.wp_credentials
*.key
*.pub
*:Zone.Identifier

# アーカイブ
archives/
EOF

    echo ".gitignoreを作成しました"
}

# リモートリポジトリを追加
add_remote() {
    echo ""
    echo "2. GitHubリポジトリを作成してください:"
    echo "   https://github.com/new"
    echo ""
    read -p "リポジトリURL（例: https://github.com/username/workspace.git）: " REPO_URL

    if [ -n "$REPO_URL" ]; then
        git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
        echo "リモートリポジトリを設定しました"
    fi
}

# 初回コミット
first_commit() {
    echo ""
    echo "3. 初回コミット..."
    git add .
    git commit -m "Initial commit: Organized workspace"
    echo "コミットしました"
}

# プッシュ
push_to_remote() {
    echo ""
    echo "4. リモートにプッシュ..."
    git branch -M main
    git push -u origin main
    echo "プッシュしました"
}

# メイン実行
main() {
    init_git
    add_remote
    first_commit
    push_to_remote

    echo ""
    echo "=== セットアップ完了 ==="
    echo ""
    echo "【PCでの同期方法】"
    echo "  git add ."
    echo "  git commit -m 'メッセージ'"
    echo "  git push"
    echo ""
    echo "【スマホ（Termux）での同期方法】"
    echo "  1. 初回のみ:"
    echo "     cd ~"
    echo "     git clone $REPO_URL workspace"
    echo "     cd workspace"
    echo ""
    echo "  2. 同期（PCの変更を取得）:"
    echo "     git pull"
    echo ""
    echo "  3. スマホで変更した場合:"
    echo "     git add ."
    echo "     git commit -m 'メッセージ'"
    echo "     git push"
    echo ""
}

main
