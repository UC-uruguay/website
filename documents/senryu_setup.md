# Teaンリュウ（川柳）ページ セットアップ手順

## 📋 概要
このページは、Googleの無料サービス「Firebase」を使って、リアルタイムで川柳の投稿といいねができる仕組みです。

## 🚀 セットアップ手順（5-10分）

### 1. Firebaseプロジェクトの作成

1. **Firebase コンソールにアクセス**
   - https://console.firebase.google.com/ にアクセス
   - Googleアカウントでログイン

2. **新規プロジェクトを作成**
   - 「プロジェクトを追加」をクリック
   - プロジェクト名: `chaba-ba-senryu`（任意の名前でOK）
   - Google アナリティクス: 不要なのでOFFにしてOK
   - 「プロジェクトを作成」をクリック

### 2. Realtime Database の設定

1. **左メニューから「構築」→「Realtime Database」を選択**

2. **「データベースを作成」をクリック**

3. **ロケーション選択**
   - 「asia-southeast1 (シンガポール)」を選択（日本に近い）
   - 「次へ」をクリック

4. **セキュリティルール**
   - 「テストモードで開始」を選択
   - 「有効にする」をクリック

5. **セキュリティルールの更新（重要！）**
   - 「ルール」タブをクリック
   - 以下のルールに書き換えて「公開」をクリック：

```json
{
  "rules": {
    "senryus": {
      ".read": true,
      ".write": true
    }
  }
}
```

### 3. Firebase設定の取得

1. **プロジェクト設定を開く**
   - 左上の歯車アイコン ⚙️ → 「プロジェクトの設定」をクリック

2. **アプリを追加**
   - 下にスクロールして「マイアプリ」セクションを探す
   - ウェブアイコン `</>` をクリック
   - アプリのニックネーム: `senryu-web`（任意）
   - 「Firebase Hosting」はチェック不要
   - 「アプリを登録」をクリック

3. **設定をコピー**
   - 表示される `firebaseConfig` の内容をコピー
   - 例：
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "chaba-ba-senryu.firebaseapp.com",
  databaseURL: "https://chaba-ba-senryu-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "chaba-ba-senryu",
  storageBucket: "chaba-ba-senryu.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:xxxxxxxxxxxxx"
};
```

### 4. HTMLファイルの更新

1. **senryu.html を開く**

2. **Firebase設定を置き換え**
   - 44行目あたりの `firebaseConfig` の部分を探す
   - 先ほどコピーした設定で置き換える

```javascript
// この部分を置き換える
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",  // ← ここを実際の値に
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

3. **ファイルを保存**

### 5. 動作確認

1. **senryu.html をブラウザで開く**
   - ファイルをダブルクリック、または
   - ブラウザにドラッグ&ドロップ

2. **テスト投稿**
   - 名前と川柳を入力して投稿
   - すぐに表示されることを確認

3. **別のデバイスでも開いてみる**
   - スマホやタブレットでも同じファイルを開く
   - リアルタイムで同期されることを確認

## 🎉 使い方

### イベント当日の準備

1. **senryu.html をサーバーにアップロード**（推奨）
   - chaba-ba.jpn.org にアップロード
   - URLは: https://chaba-ba.jpn.org/senryu.html

2. **QRコード作成**
   - https://www.qrcode-monkey.com/ などでURLのQRコードを作成
   - 会場に掲示

3. **参加者に案内**
   - QRコードを読み取ってアクセス
   - 投稿といいねを楽しむ

### セキュリティについて

- テストモードは30日で期限切れになります
- イベント後は以下のルールに変更することをおすすめ：

```json
{
  "rules": {
    "senryus": {
      ".read": true,
      ".write": false
    }
  }
}
```

これで投稿を停止し、閲覧のみ可能になります。

## 🔧 トラブルシューティング

### 投稿できない
- Firebaseの設定が正しいか確認
- ブラウザのコンソール（F12キー）でエラーを確認

### リアルタイム更新されない
- インターネット接続を確認
- ページをリロード

### いいねが反映されない
- ブラウザのキャッシュをクリア
- 別のブラウザで試す

## 📱 サーバーへのアップロード方法

chaba-ba.jpn.org にアップロードする場合：

```bash
# SCPでアップロード（例）
scp /home/uc/senryu.html user@chaba-ba.jpn.org:/var/www/html/
```

または、WordPressの管理画面からメディアライブラリにHTMLをアップロードし、直接リンクで公開することもできます。

---

質問があれば、いつでもお聞きください！🍵
