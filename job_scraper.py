import requests
from bs4 import BeautifulSoup

url = "https://remoteok.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)