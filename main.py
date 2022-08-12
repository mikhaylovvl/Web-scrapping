import re

import requests
from bs4 import BeautifulSoup


def get_news():
    BASE_LINK = "https://habr.com"
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome"
                        " / 102.0.5005.148 YaBrowser / 22.7.2.899 Yowser / 2.5 Safari / 537.36"
    }

    res = requests.get(url="https://habr.com/ru/all/", headers=headers).text
    soup = BeautifulSoup(res, "lxml")

    all_news = soup.findAll("div", class_="tm-article-snippet")

    pattern = r"[Дд]изайн|[Фф]ото|[Ww]eb|[Pp]ython|LINSTOR"
    for a_news in all_news:
        time_published_news = a_news.find("span", class_="tm-article-snippet__datetime-published").find("time"). \
            get("title")
        link_news = a_news.find("a", class_="tm-article-snippet__title-link").get("href")
        title_news = a_news.find("a", class_="tm-article-snippet__title-link").find("span").text
        result = re.findall(pattern, title_news)
        if result:
            print(f"<{time_published_news}> - <{title_news}"
                  f"> - <{BASE_LINK + link_news}>")


if __name__ == '__main__':
    get_news()
