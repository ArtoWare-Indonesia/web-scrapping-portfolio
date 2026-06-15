import requests
from bs4 import BeautifulSoup

url = "https://www.kompas.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)