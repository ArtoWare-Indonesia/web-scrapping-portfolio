import requests
from bs4 import BeautifulSoup

url = "https://www.kompas.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("=== HEADLINES KOMPAS ===\n")
    for i, title in enumerate(soup.find_all("h2"), start=1):
        print(f"{i}. {title.get_text(strip=True)}")
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for title in soup.find_all("h2"):
            file.write(title.get_text(strip=True) + "\n")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")