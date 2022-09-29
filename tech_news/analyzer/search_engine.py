from tech_news.database import search_news
from datetime import datetime


# Onde pesquisei o regex da query no mongoDB
# https://www.mongodb.com/docs/manual/reference/operator/query/regex/
# Requisito 6
def search_by_title(title):
    the_news = search_news({"title": {"$regex": title}, "$options": "i"})
    news_list = [(news["title"], news["url"]) for news in the_news]
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        the_date = datetime.fromisoformat(date).strftime("%Y-%m-%d")
        dates_result = search_news(
            {"timestamp": {"$regex": the_date}, "$options": "i"}
        )
        dates_list = [(news["title"], news["url"]) for news in dates_result]
        return dates_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
