import requests
import parsel
from time import sleep
from tech_news.database import create_news


# Requisito 1


def fetch(url, timeout=3):
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=timeout, headers=header)
        sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)

    titles_list = []
    titles_list = selector.css(".entry-title a::attr(href)").getall()
    return titles_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    data = {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css(".label::text").get(),
    }
    return data


# Requisito 5
def get_tech_news(amount):
    response = fetch("https://blog.betrybe.com")
    news_urls = scrape_novidades(response)
    news = list()

    while amount > len(news_urls):
        next_page = scrape_next_page_link(response)
        new_page = fetch(next_page)
        news_urls.extend(scrape_novidades(new_page))

    for url in news_urls[:amount]:
        noticias = fetch(url)
        news.append(scrape_noticia(noticias))

    create_news(news)

    return news
