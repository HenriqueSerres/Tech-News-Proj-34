import requests
# import parsel
from time import sleep


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
