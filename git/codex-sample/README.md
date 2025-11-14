# Amazon書籍紹介動画ジェネレーター

このリポジトリは、Amazonの書籍URLを入力として受け取り、将来的に動画を生成するためのWebアプリケーションの土台です。現在はURLを受け取って確認メッセージを表示するシンプルなフォームのみが実装されています。

## 動作確認済み環境
- Python 3.10 以上
- pip (Pythonに同梱されているパッケージマネージャ)

## セットアップ手順
1. リポジトリを取得したら、作業ディレクトリをプロジェクト直下に移動します。
   ```bash
   cd codex-sample
   ```
2. (任意) 仮想環境を作成して有効化します。
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows の場合は .venv\\Scripts\\activate
   ```
3. 依存パッケージをインストールします。
   ```bash
   pip install -r amazon_video_generator/requirements.txt
   ```

## アプリケーションの起動
1. Flaskアプリケーションのあるディレクトリに移動します。
   ```bash
   cd amazon_video_generator
   ```
2. 開発サーバーを起動します。
   ```bash
   python app.py
   ```
   `app.py` では `debug=True` で実行されるため、コードを変更すると自動で再起動されます。必要に応じて本番環境では無効化してください。

3. ブラウザで [http://127.0.0.1:5000/](http://127.0.0.1:5000/) にアクセスするとフォームが表示されます。Amazonの書籍ページのURLを入力して送信すると、受け取ったURLがコンソールに表示され、画面上には処理開始メッセージが表示されます。

## その他
- Flaskの設定を環境変数で管理したい場合は `flask --app app run` といったコマンドを利用することもできます。
- 静的ファイルは `amazon_video_generator/static/`、テンプレートは `amazon_video_generator/templates/` に配置されています。
