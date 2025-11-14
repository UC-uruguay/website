#!/bin/bash

# PC（WSL）とスマホ（Termux）を完全自動でGit同期するスクリプト

set -e  # エラーが発生したら停止

# 色付き出力
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# スマホのFTP情報
PHONE_FTP="ftp://192.168.1.54:2121"
PHONE_PATH="/data/data/com.termux/files/home"
PC_PATH="/home/uc"

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}  PC⇔スマホ 完全自動Git同期${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""

# ステップ0: 必要なパッケージを確認・インストール
echo -e "${YELLOW}[0/7] 必要なパッケージを確認中...${NC}"
if ! command -v lftp &> /dev/null; then
    echo "lftpをインストールしています..."
    sudo apt update && sudo apt install -y lftp
fi
if ! command -v gh &> /dev/null; then
    echo "GitHub CLIをインストールしています..."
    sudo apt install -y gh
fi
echo -e "${GREEN}✓ 必要なパッケージがインストールされています${NC}"
echo ""

# ステップ1: FTP接続を確認
echo -e "${YELLOW}[1/7] スマホへのFTP接続を確認中...${NC}"
if lftp -e "ls; bye" $PHONE_FTP &>/dev/null; then
    echo -e "${GREEN}✓ FTP接続成功！${NC}"
else
    echo -e "${RED}✗ FTP接続失敗${NC}"
    echo "スマホのFTPサーバーが起動していることを確認してください"
    echo "Termuxで実行: termux-ftp-server"
    exit 1
fi
echo ""

# ステップ2: スマホから重要ファイルをバックアップ（念のため）
echo -e "${YELLOW}[2/7] スマホから重要ファイルをバックアップ中...${NC}"
BACKUP_DIR="$PC_PATH/phone_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# CLAUDE.mdを含むプロジェクトフォルダをバックアップ
echo "プロジェクトフォルダをバックアップ中..."
lftp -e "mirror --verbose --only-newer $PHONE_PATH/uc-site $BACKUP_DIR/uc-site; bye" $PHONE_FTP 2>/dev/null || true
lftp -e "mirror --verbose --only-newer $PHONE_PATH/website $BACKUP_DIR/website; bye" $PHONE_FTP 2>/dev/null || true
lftp -e "mirror --verbose --only-newer $PHONE_PATH/ai-pressroom $BACKUP_DIR/ai-pressroom; bye" $PHONE_FTP 2>/dev/null || true

echo -e "${GREEN}✓ バックアップ完了: $BACKUP_DIR${NC}"
echo ""

# ステップ3: PCでGitリポジトリを初期化
echo -e "${YELLOW}[3/7] PCでGitリポジトリを初期化中...${NC}"
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

# FTPサーバーの一時ファイル
.ftpconfig
EOF

echo -e "${GREEN}✓ .gitignoreを作成しました${NC}"
echo ""

# ステップ4: GitHub CLIで認証確認
echo -e "${YELLOW}[4/7] GitHub認証を確認中...${NC}"
if ! gh auth status &>/dev/null; then
    echo "GitHubにログインしてください..."
    gh auth login
fi
echo -e "${GREEN}✓ GitHub認証済み${NC}"
echo ""

# ステップ5: GitHubリポジトリを自動作成
echo -e "${YELLOW}[5/7] GitHubリポジトリを作成中...${NC}"
read -p "リポジトリ名を入力してください（デフォルト: workspace）: " REPO_NAME
REPO_NAME=${REPO_NAME:-workspace}

# リポジトリが既に存在するか確認
if gh repo view "$REPO_NAME" &>/dev/null; then
    echo -e "${YELLOW}リポジトリ '$REPO_NAME' は既に存在します${NC}"
    read -p "既存のリポジトリを使用しますか？ (y/n): " USE_EXISTING
    if [ "$USE_EXISTING" != "y" ]; then
        read -p "別のリポジトリ名を入力してください: " REPO_NAME
        gh repo create "$REPO_NAME" --private --confirm
    fi
else
    gh repo create "$REPO_NAME" --private --confirm
    echo -e "${GREEN}✓ GitHubリポジトリ '$REPO_NAME' を作成しました${NC}"
fi

# リポジトリURLを取得
REPO_URL=$(gh repo view "$REPO_NAME" --json url -q .url)
echo "リポジトリURL: $REPO_URL"
echo ""

# ステップ6: GitHubにプッシュ
echo -e "${YELLOW}[6/7] GitHubにプッシュ中...${NC}"

# リモートを設定
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

# 初回コミット
git add .
git commit -m "Initial commit: Organized workspace with scripts, images, documents, etc." || true

# プッシュ
git branch -M main
if git push -u origin main; then
    echo -e "${GREEN}✓ GitHubへのプッシュ成功！${NC}"
else
    echo -e "${RED}✗ プッシュ失敗${NC}"
    exit 1
fi
echo ""

# リポジトリURLをファイルに保存（スマホ側で使用）
echo "$REPO_URL" > $PC_PATH/.git_repo_url

echo -e "${YELLOW}[7/7] FTP経由でスマホに同期中...${NC}"
echo "これには数分かかる場合があります..."
echo ""

# スマホ側の古いファイルを削除してから同期
lftp -e "set ftp:ssl-allow no; open $PHONE_FTP; mirror --reverse --delete --verbose --exclude .git/ --exclude .cache/ --exclude .local/ --exclude phone_backup_*/ $PC_PATH $PHONE_PATH; bye" <<EOF
mirror --reverse --delete --verbose --exclude .git/ --exclude .cache/ --exclude .local/ --exclude phone_backup_*/ $PC_PATH $PHONE_PATH
bye
EOF

echo -e "${GREEN}✓ スマホへの同期完了！${NC}"
echo ""

# スマホ側用のGit設定スクリプトを作成
echo -e "${YELLOW}スマホ側用のセットアップスクリプトを作成中...${NC}"

cat > $PC_PATH/phone_git_setup.sh <<'PHONE_SCRIPT'
#!/data/data/com.termux/files/usr/bin/bash

# スマホ（Termux）側のGit設定スクリプト

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

# 既存の.gitディレクトリを削除（FTPで転送されない）
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

# .gitignoreを確認
if [ ! -f ".gitignore" ]; then
    echo ".gitignoreが見つかりません（PCから同期されるはずです）"
fi

# 既存のファイルをコミット
git add .
git commit -m "Synced from PC via FTP" || true

# ブランチ名を設定
git branch -M main

# リモートの内容を取得
git fetch origin main

# リモートと同期（競合がある場合は上書き）
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

echo -e "${GREEN}✓ スマホ側用スクリプトを作成・転送しました${NC}"
echo ""

# 完了メッセージ
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
echo "■ スマホで変更した場合:"
echo "  git add ."
echo "  git commit -m 'メッセージ'"
echo "  git push"
echo ""
echo "■ PCで変更をスマホに反映:"
echo "  git pull"
echo ""
echo -e "${YELLOW}バックアップ場所:${NC} $BACKUP_DIR"
echo ""
