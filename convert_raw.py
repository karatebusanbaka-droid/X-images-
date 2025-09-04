import csv

def to_raw_url(blob_url: str) -> str:
    """GitHubのblob URLをraw URLに変換"""
    return blob_url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")

# ===== 入力ファイル =====
# GitHubのURLを1行ずつ入れたCSVやTXTを用意してください
input_file = "urls.csv"   # 例: urls.csv に blob のURLを入れる
output_file = "urls_raw.csv"

# ===== URL変換 =====
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader if row]  # 1列目を全部取得

raw_urls = [to_raw_url(url) for url in urls]

# ===== 結果を書き出し =====
with open(output_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    for url in raw_urls:
        writer.writerow([url])

print("✅ 変換完了！結果は", output_file, "に保存されました。")