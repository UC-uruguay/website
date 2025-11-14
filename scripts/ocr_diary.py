import google.generativeai as genai
import os
from PIL import Image

# 1. で取得したご自身のAPIキーを設定してください
API_KEY = "AIzaSyCzFs9gH3s88DXsyk7DCeKLOWib4TnChiM" 

# 画像ファイルが保存されているフォルダのパスを指定してください
IMAGE_DIR = "/home/uc/popo"

# 抽出したテキストを保存するファイルの名前
OUTPUT_FILE = "popo_gemini.txt"

# Geminiの設定
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # 最新の高速モデルがおすすめ

def ocr_image(image_path):
  """指定された画像をOCR処理し、テキストを返す関数"""
  print(f"📄 {os.path.basename(image_path)} を処理中...")
  try:
    img = Image.open(image_path)
    response = model.generate_content([
        "これは妊娠中に僕と妻がつづった日記の写真です。書かれているテキストをできるだけ正確に書き起こしてください。また、もしコンテキストがわからないときには、日記としてなりたつ自由文になるよう調整してください",
        img
    ])
    return response.text
  except Exception as e:
    print(f"🛑 エラーが発生しました: {e}")
    return None

# --- メインの処理 ---
# 出力用のファイルを追記モードで開く
with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
  # 指定されたフォルダ内のすべてのファイルに対して処理を実行
  # ファイル名でソートして、日記の順番通りに処理する
  for filename in sorted(os.listdir(IMAGE_DIR)):
    # .jpg や .png などの画像ファイルのみを対象にする
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
      full_path = os.path.join(IMAGE_DIR, filename)
      
      # 画像からテキストを抽出
      extracted_text = ocr_image(full_path)
      
      if extracted_text:
        # 抽出したテキストをファイルに書き込む
        f.write(f"--- {filename} ---\n")
        f.write(extracted_text)
        f.write("\n\n")
        print(f"✅ テキストを {OUTPUT_FILE} に追記しました。")

print("\n🎉 すべての画像の処理が完了しました！")