from requests import get
from bs4 import BeautifulSoup

URL = "https://www.uzhnu.edu.ua/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
page = get(URL, headers=HEADERS)
soup = BeautifulSoup(page.text, 'lxml')
links = []
with open('./ok.txt', 'w') as file:
    for link in soup.find_all('a'):
        if link.get('href') is not None:
            if link.get('href') not in links:
                if 'https' in link.get('href'): 
                    file.write("href: {0}\n".format(link.get('href')))
                    links.append(link.get('href'))
    for link in links:
        URL = link
        page = get(URL, headers=HEADERS)
        soup = BeautifulSoup(page.text, 'lxml')
        for newlink in soup.find_all('a'):
            if newlink.get('href') is not None:
                if newlink.get('href') not in links:
                    if 'https' in newlink.get('href'): 
                        file.write("href: {0}\n".format(newlink.get('href')))
                        links.append(newlink.get('href'))