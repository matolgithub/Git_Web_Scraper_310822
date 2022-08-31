import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
}

url_main = 'https://3dnews.ru/'
url_news = 'https://3dnews.ru/news/'


def get_articles_url(url):
    s = requests.Session()
    response = s.get(url=url_news, headers=headers)

    # with open('index.html', 'w') as file:
    #     file.write(response.text) 

    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    links = soup.find(class_="cntPrevWrapper")
    pprint(links)
    # for link in links:
    #     news_url_link = link.get('href')
    #     print(news_url_link)


def main():
    get_articles_url(url=url_news)


if __name__ == '__main__':
    main()
    