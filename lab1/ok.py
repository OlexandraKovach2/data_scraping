import requests
from bs4 import BeautifulSoup

URL = "https://www.uzhnu.edu.ua/uk/cat/faculty"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.text)

with open('ok.txt', 'w') as f:
    for link in soup.find_all('a'):
        f.write(f"{link.get('href')}\n")