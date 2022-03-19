import json
from bs4 import BeautifulSoup
import requests
from urllib3.util import url
from datetime import datetime

url = "https://habr.com/ru/all/"
headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

req = requests.get(url, headers=headers)
src = req.text
soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all(class_="tm-articles-list__item")
all_categories_dict = {}

for item in all_products_href:
    item_text = item.text
    item_href = "https://habr.com/ru/all/"

    all_categories_dict[item_text] = item_href

with open("news/habr/all_categories_dict.json", "w")as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
