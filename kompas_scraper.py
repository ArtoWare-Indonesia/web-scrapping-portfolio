import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.kompas.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for title in soup.find_all("h2"):
    text = title.get_text(strip=True)

    if len(text) > 20 and text not in ["Lihat semua", "Produk Rekomendasi"]:
        headlines.append(text)

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    for headline in headlines:
        writer.writerow([headline])

print(f"Berhasil menyimpan {len(headlines)} headline ke headlines.csv")