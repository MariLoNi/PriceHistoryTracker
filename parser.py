from lxml import html
from urllib.parse import urlparse
import requests


PARSERS_BY_DOMAIN = {
    'ipiter.ru': lambda tree: tree.xpath('//meta[@itemprop="price"]/@content')[0],
}


def get_domain(url):
    return urlparse(url).netloc


def get_price(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    domain = get_domain(url)
    parser = PARSERS_BY_DOMAIN.get(domain)
    return parser(tree)
