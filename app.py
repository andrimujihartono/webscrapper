import requests 
from bs4 import BeautifulSoup
import json

pages = requests.get('https://bro.do/collections/all')

soup= BeautifulSoup(pages.content, 'html.parser')
page_title = soup.title.text
items = []
products = soup.select('div.product-details')

for elem in products:
    title = elem.select('span.title')[0].text
    price = elem.select('span.money > span.money')[0].text
    info = {
        "title" : title.strip(),
        "price" : price.strip()
    }
    items.append(info)

filename = 'result.json'
json.dump(items, open(filename, 'w'))
print(items)