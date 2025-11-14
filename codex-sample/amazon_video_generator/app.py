from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amazon_url = request.form.get('amazon_url')
        print(f"受け取ったURL: {amazon_url}")
        # ここに後の処理を追加していく
        return render_template('index.html', message="URLを受け取りました。処理を開始します。")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
