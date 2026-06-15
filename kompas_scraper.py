import requests
from bs4 import BeautifulSoup

url = "https://www.kompas.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for title in soup.find_all("h2"):
    print(title.get_text())