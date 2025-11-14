#!/bin/bash

# PC（WSL）とスマホ（Termux）をシンプルにGit同期するスクリプト
# GitHub CLI不要版

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PHONE_FTP="ftp://ucjp:Tis304268@192.168.1.54:2121"
PHONE_PATH="/data/data/com.termux/files/home"
PC_PATH="/home/uc"

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}  PC⇔スマホ シンプルGit同期${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""

# lftpの確認
echo -e "${YELLOW}[1/6] lftpを確認中...${NC}"
if ! command -v lftp &> /dev/null; then
    echo -e "${RED}lftpがインストールされていません${NC}"
    echo "WSLで実行してください: sudo apt install -y lftp"
    exit 1
fi
echo -e "${GREEN}✓ lftpがインストールされています${NC}"
echo ""

# FTP接続確認
echo -e "${YELLOW}[2/6] スマホへのFTP接続を確認中...${NC}"
if lftp -e "ls; bye" $PHONE_FTP &>/dev/null; then
    echo -e "${GREEN}✓ FTP接続成功！${NC}"
else
    echo -e "${RED}✗ FTP接続失敗${NC}"
    echo "スマホのFTPサーバーが起動していることを確認してください"
    exit 1
fi
echo ""

# バックアップ
echo -e "${YELLOW}[3/6] スマホから重要ファイルをバックアップ中...${NC}"
BACKUP_DIR="$PC_PATH/phone_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "プロジェクトフォルダをバックアップ中..."
lftp -e "mirror --verbose --only-newer $PHONE_PATH/uc-site $BACKUP_DIR/uc-site 2>/dev/null || true; bye" $PHONE_FTP || true
lftp -e "mirror --verbose --only-newer $PHONE_PATH/website $BACKUP_DIR/website 2>/dev/null || true; bye" $PHONE_FTP || true
lftp -e "mirror --verbose --only-newer $PHONE_PATH/ai-pressroom $BACKUP_DIR/ai-pressroom 2>/dev/null || true; bye" $PHONE_FTP || true

echo -e "${GREEN}✓ バックアップ完了: $BACKUP_DIR${NC}"
echo ""

# Git初期化
echo -e "${YELLOW}[4/6] PCでGitリポジトリを初期化中...${NC}"
cd $PC_PATH

if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✓ Gitリポジトリを初期化しました${NC}"
else
    echo -e "${GREEN}✓ 既にGitリポジトリです${NC}"
fi

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
echo -e "${YELLOW}[5/6] GitHubリポジトリを作成中...${NC}"
echo ""
read -p "GitHubアクセストークンを入力してください: " GITHUB_TOKEN

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

# 既存のリポジトリ一覧を取得してローカルにないものをチェック
echo "既存のGitHubリポジトリを確認中..."
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
fi

echo ""
read -p "新しいリポジトリ名を入力してください（デフォルト: workspace）: " REPO_NAME
REPO_NAME=${REPO_NAME:-workspace}

# リポジトリが既に存在するか確認
REPO_EXISTS=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $GITHUB_TOKEN" "https://api.github.com/repos/$GITHUB_USER/$REPO_NAME")

if [ "$REPO_EXISTS" = "200" ]; then
    echo -e "${YELLOW}リポジトリ '$REPO_NAME' は既に存在します${NC}"
    read -p "既存のリポジトリを使用しますか？ (y/n): " USE_EXISTING
    if [ "$USE_EXISTING" != "y" ]; then
        read -p "別のリポジトリ名を入力してください: " REPO_NAME
        # 新しいリポジトリを作成
        curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
            -d "{\"name\":\"$REPO_NAME\",\"private\":true}" \
            https://api.github.com/user/repos > /dev/null
        echo -e "${GREEN}✓ GitHubリポジトリ '$REPO_NAME' を作成しました${NC}"
    fi
else
    # 新しいリポジトリを作成
    curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
        -d "{\"name\":\"$REPO_NAME\",\"private\":true}" \
        https://api.github.com/user/repos > /dev/null
    echo -e "${GREEN}✓ GitHubリポジトリ '$REPO_NAME' を作成しました${NC}"
fi

REPO_URL="https://$GITHUB_TOKEN@github.com/$GITHUB_USER/$REPO_NAME.git"
echo "リポジトリURL: https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo ""

# リモートを設定
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

# 初回コミット
git add .
git commit -m "Initial commit: Organized workspace" || echo "既にコミット済み"

# プッシュ
git branch -M main
echo ""
echo "GitHubにプッシュしています..."
if git push -u origin main; then
    echo -e "${GREEN}✓ GitHubへのプッシュ成功！${NC}"
else
    echo -e "${RED}✗ プッシュ失敗${NC}"
    echo "認証エラーの場合は、Personal Access Tokenを設定してください"
    echo "https://github.com/settings/tokens"
    exit 1
fi
echo ""

# リポジトリURLを保存
echo "$REPO_URL" > $PC_PATH/.git_repo_url

# FTP同期
echo -e "${YELLOW}[6/6] FTP経由でスマホに同期中...${NC}"
echo "これには数分かかる場合があります..."
echo ""

lftp $PHONE_FTP <<EOF
set ftp:ssl-allow no
mirror --reverse --delete --verbose \
    --exclude .git/ \
    --exclude .cache/ \
    --exclude .local/ \
    --exclude phone_backup_*/ \
    $PC_PATH $PHONE_PATH
bye
EOF

echo -e "${GREEN}✓ スマホへの同期完了！${NC}"
echo ""

# スマホ側用スクリプトを作成
cat > $PC_PATH/phone_git_setup.sh <<'PHONE_SCRIPT'
#!/data/data/com.termux/files/usr/bin/bash

echo "========================================="
echo "  スマホ側のGit設定"
echo "========================================="
echo ""

cd ~

# Gitがインストールされているか確認
if ! command -v git &> /dev/null; then
    echo "Gitをインストールしています..."
    pkg install -y git
fi

# 既存の.gitディレクトリを削除
if [ -d ".git" ]; then
    rm -rf .git
fi

# リポジトリURLを取得
if [ -f ".git_repo_url" ]; then
    REPO_URL=$(cat .git_repo_url)
    echo "リポジトリURL: $REPO_URL"
else
    echo "リポジトリURLが見つかりません"
    read -p "リポジトリURL: " REPO_URL
fi

# Gitリポジトリを初期化
git init
git remote add origin "$REPO_URL"

# 既存のファイルをコミット
git add .
git commit -m "Synced from PC via FTP" || true

# ブランチ名を設定
git branch -M main

# リモートの内容を取得
git fetch origin main

# リモートと同期
git reset --hard origin/main

echo ""
echo "✓ Git設定完了！"
echo ""
echo "【今後の使い方】"
echo ""
echo "■ PCの変更をスマホに反映:"
echo "  git pull"
echo ""
echo "■ スマホで変更した場合:"
echo "  git add ."
echo "  git commit -m 'メッセージ'"
echo "  git push"
echo ""
PHONE_SCRIPT

chmod +x $PC_PATH/phone_git_setup.sh

# スマホ側にスクリプトを転送
lftp -e "put $PC_PATH/phone_git_setup.sh -o $PHONE_PATH/phone_git_setup.sh; bye" $PHONE_FTP

echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}  ✓ 全ての設定が完了しました！${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""
echo -e "${YELLOW}【次のステップ】${NC}"
echo ""
echo "1. スマホ（Termux）を開いてください"
echo ""
echo "2. 以下のコマンドを実行してください:"
echo -e "   ${GREEN}cd ~${NC}"
echo -e "   ${GREEN}bash phone_git_setup.sh${NC}"
echo ""
echo "3. 完了！今後の使い方:"
echo ""
echo "■ PCで変更した場合:"
echo "  cd /home/uc"
echo "  git add ."
echo "  git commit -m 'メッセージ'"
echo "  git push"
echo ""
echo "■ スマホで変更をPCに反映:"
echo "  git pull"
echo ""
echo -e "${YELLOW}バックアップ場所:${NC} $BACKUP_DIR"
echo ""
