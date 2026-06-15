import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.kompas.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    for title in soup.find_all("h2"):
        writer.writerow([title.get_text()])