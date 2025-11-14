#!/bin/bash

# PC側でGitリポジトリを作成してGitHubにプッシュ（FTP不要版）

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PC_PATH="/home/uc"

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}  PC側 Git設定＆GitHubプッシュ${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""

cd $PC_PATH

# Git初期化
echo -e "${YELLOW}[1/5] PCでGitリポジトリを初期化中...${NC}"
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✓ Gitリポジトリを初期化しました${NC}"
else
    echo -e "${GREEN}✓ 既にGitリポジトリです${NC}"
fi
echo ""

# .gitignoreを作成
cat > .gitignore <<'EOF'
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

# Claude設定
.claude/
.claude.json
.claude.json.backup

# 一時ファイル
*.log
.bash_history
.viminfo
.lesshst
.wget-hsts
.motd_shown
.sudo_as_admin_successful

# 認証情報
.wp_credentials
*.key.pub
*:Zone.Identifier

# バックアップ
phone_backup_*/
EOF

echo -e "${GREEN}✓ .gitignoreを作成しました${NC}"
echo ""

# GitHubアクセストークンを取得
echo -e "${YELLOW}[2/5] GitHubに接続中...${NC}"
read -p "GitHubアクセストークン: " GITHUB_TOKEN

if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}アクセストークンが入力されていません${NC}"
    exit 1
fi

# GitHubユーザー名を取得
GITHUB_USER=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user | grep -o '"login": "[^"]*' | cut -d'"' -f4)

if [ -z "$GITHUB_USER" ]; then
    echo -e "${RED}アクセストークンが無効です${NC}"
    exit 1
fi

echo -e "${GREEN}✓ GitHubユーザー: $GITHUB_USER${NC}"
echo ""

# 既存のリポジトリ一覧を取得
echo -e "${YELLOW}[3/5] 既存のGitHubリポジトリを確認中...${NC}"
REPOS=$(curl -s -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/user/repos?per_page=100" | grep -o '"full_name": "[^"]*' | cut -d'"' -f4)

echo ""
echo "【ローカルに存在しないGitHubリポジトリ】"
MISSING_REPOS=""
for repo in $REPOS; do
    repo_name=$(basename $repo)
    if [ ! -d "$PC_PATH/$repo_name" ]; then
        echo "  - $repo_name"
        MISSING_REPOS="$MISSING_REPOS $repo_name"
    fi
done

if [ -n "$MISSING_REPOS" ]; then
    echo ""
    read -p "これらのリポジトリをクローンしますか？ (y/n): " CLONE_REPOS
    if [ "$CLONE_REPOS" = "y" ]; then
        for repo in $REPOS; do
            repo_name=$(basename $repo)
            if [ ! -d "$PC_PATH/$repo_name" ]; then
                echo "クローン中: $repo_name"
                git clone "https://$GITHUB_TOKEN@github.com/$repo.git" "$PC_PATH/$repo_name" 2>/dev/null || true
            fi
        done
        echo -e "${GREEN}✓ クローン完了${NC}"
    fi
else
    echo "  （全てのリポジトリがローカルに存在します）"
fi

echo ""

# 新しいリポジトリを作成
echo -e "${YELLOW}[4/5] 新しいリポジトリを作成中...${NC}"
read -p "リポジトリ名（デフォルト: workspace）: " REPO_NAME
REPO_NAME=${REPO_NAME:-workspace}

# リポジトリが既に存在するか確認
REPO_EXISTS=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/repos/$GITHUB_USER/$REPO_NAME")

if [ "$REPO_EXISTS" = "200" ]; then
    echo -e "${YELLOW}リポジトリ '$REPO_NAME' は既に存在します${NC}"
    read -p "既存のリポジトリを使用しますか？ (y/n): " USE_EXISTING
    if [ "$USE_EXISTING" != "y" ]; then
        read -p "別のリポジトリ名を入力してください: " REPO_NAME
        curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
            -d "{\"name\":\"$REPO_NAME\",\"private\":true}" \
            https://api.github.com/user/repos > /dev/null
        echo -e "${GREEN}✓ GitHubリポジトリ '$REPO_NAME' を作成しました${NC}"
    fi
else
    curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
        -d "{\"name\":\"$REPO_NAME\",\"private\":true}" \
        https://api.github.com/user/repos > /dev/null
    echo -e "${GREEN}✓ GitHubリポジトリ '$REPO_NAME' を作成しました${NC}"
fi

REPO_URL="https://$GITHUB_TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git"
REPO_URL_PUBLIC="https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo ""

# GitHubにプッシュ
echo -e "${YELLOW}[5/5] GitHubにプッシュ中...${NC}"

git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

git add .
git commit -m "Initial commit: Organized workspace" || echo "既にコミット済み"

git branch -M main

if git push -u origin main; then
    echo -e "${GREEN}✓ GitHubへのプッシュ成功！${NC}"
else
    echo -e "${RED}✗ プッシュ失敗${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}  ✓ PC側の設定が完了しました！${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""
echo -e "${YELLOW}【次: スマホ（Termux）での作業】${NC}"
echo ""
echo "1. Termuxを開いてください"
echo ""
echo "2. 既存のファイルをバックアップ（必要に応じて）:"
echo -e "   ${GREEN}mv ~/uc-site ~/uc-site.backup${NC}"
echo -e "   ${GREEN}mv ~/website ~/website.backup${NC}"
echo ""
echo "3. GitHubからクローン:"
echo -e "   ${GREEN}cd ~${NC}"
echo -e "   ${GREEN}rm -rf * .*${NC}  ${RED}# 注意: 全ファイル削除${NC}"
echo -e "   ${GREEN}git clone $REPO_URL_PUBLIC .${NC}"
echo ""
echo "4. 今後の使い方:"
echo ""
echo "■ PCで変更した場合:"
echo "  cd /home/uc"
echo "  git add ."
echo "  git commit -m 'メッセージ'"
echo "  git push"
echo ""
echo "■ スマホで変更をPCに反映:"
echo "  cd ~"
echo "  git pull"
echo ""
echo "■ スマホで変更した場合:"
echo "  cd ~"
echo "  git add ."
echo "  git commit -m 'メッセージ'"
echo "  git push"
echo ""
echo "■ PCで変更をスマホに反映:"
echo "  cd /home/uc"
echo "  git pull"
echo ""
echo -e "${BLUE}リポジトリURL: $REPO_URL_PUBLIC${NC}"
echo ""
