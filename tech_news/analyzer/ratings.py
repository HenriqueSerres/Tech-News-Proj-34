from operator import itemgetter
from tech_news.database import search_news

# Onde pesquisei função sorted:
# https://www.w3schools.com/python/ref_func_sorted.asp


# Requisito 10
def top_5_news():
    all_news = search_news({})
    top_five = []
    sorted_news = sorted(
        all_news, key=itemgetter("comments_count"), reverse=True
    )
    for news in sorted_news[:5]:
        top_five.append((news["title"], news["url"]))
    print(top_five)
    return top_five


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
