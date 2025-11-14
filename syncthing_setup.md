# Syncthingを使った自動同期セットアップ

Syncthingは、複数のデバイス間でファイルを自動的に同期するアプリです。
設定後は自動的に同期されるので、Gitのコミット・プッシュが不要です。

## 特徴
- 自動同期（変更を検知して自動的に同期）
- インターネット経由でも同期可能
- プライベート（データは暗号化され、中央サーバーを経由しない）
- GUI管理画面あり

## セットアップ手順

### 1. PC（WSL）側のセットアップ

```bash
# Syncthingをインストール
sudo apt update
sudo apt install syncthing

# Syncthingを起動
syncthing

# ブラウザでアクセス: http://localhost:8384
```

### 2. スマホ（Termux）側のセットアップ

```bash
# Syncthingをインストール
pkg install syncthing

# Syncthingを起動
syncthing

# ブラウザでアクセス: http://localhost:8384
```

### 3. デバイスを接続

1. **PC側のGUIを開く**（http://localhost:8384）
   - 右上の「アクション」→「デバイスIDを表示」をクリック
   - QRコードが表示される

2. **スマホ側のGUIを開く**（http://localhost:8384）
   - 右上の「+」→「デバイスを追加」
   - QRコードをスキャン、または手動でデバイスIDを入力
   - 「保存」をクリック

3. **PC側で承認**
   - 「新しいデバイスが追加されました」という通知が出る
   - 「追加」をクリック

### 4. フォルダを共有

1. **PC側のGUIで:**
   - 「フォルダを追加」をクリック
   - フォルダパス: `/home/uc`
   - ラベル: `workspace`
   - 共有するデバイスを選択（スマホを選択）
   - 「保存」

2. **スマホ側で承認:**
   - 「新しいフォルダが共有されました」という通知が出る
   - 「承認」をクリック
   - フォルダパス: `/data/data/com.termux/files/home/workspace`
   - 「保存」

### 5. 除外設定（オプション）

同期から除外したいファイル/フォルダを設定：

PC側のGUI → workspace フォルダの「編集」→「無視パターン」に以下を追加：

```
.cache
.local
.config
.ssh
.nvm
.npm
.docker
.android
.gemini
.codex
.claude
.claude.json
.claude.json.backup
.bash_history
.viminfo
.lesshst
.wget-hsts
.motd_shown
.wp_credentials
*.key
*.pub
*:Zone.Identifier
archives
optional-path-to-log-file
```

## 自動起動設定

### PC（WSL）側

```bash
# systemdサービスとして起動
sudo systemctl enable syncthing@$USER
sudo systemctl start syncthing@$USER
```

### スマホ（Termux）側

Termux起動時に自動実行するには、`~/.bashrc`に追加：

```bash
echo 'syncthing &' >> ~/.bashrc
```

## 使い方

セットアップ後は、何もする必要がありません！
ファイルを変更すると、自動的に他のデバイスに同期されます。

## トラブルシューティング

### 同期が始まらない場合

1. 両方のデバイスでSyncthingが起動しているか確認
2. GUIで「接続済み」になっているか確認
3. ファイアウォールでポートがブロックされていないか確認

### 競合が発生した場合

両方のデバイスで同じファイルを編集すると競合が発生します。
競合ファイルは `.sync-conflict` という名前で保存されます。
手動で内容を確認して、どちらを残すか決めてください。

## 推奨事項

- 大きなファイル（archives/など）は除外設定に追加することを推奨
- 定期的にGUIで同期状態を確認することを推奨
- バックアップとして、Gitも併用することを推奨
