import requests
from bs4 import BeautifulSoup
import sqlite3

# database stuff
con = sqlite3.connect('books.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books
                    (title text PRIMARY KEY, price real, stock text)''')


# no pagination in this example
starturl = 'https://books.toscrape.com/'

def clean(item):
    return item.strip().replace('Â','').replace('£', '')

def get_page(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text, features='html.parser')
    return sp

def parse_soup(sp):
    book_list = []
    article = sp.find_all('article', {'class': 'product_pod'})
    for book in article:
        title = book.find('img', {'class': 'thumbnail'})['alt']
        price = float(clean(book.find('p', {'class': 'price_color'}).text))
        stock = clean(book.find('p', {'class': 'instock availability'}).text)
        book_list.append((title, price, stock))
    return book_list

sp = get_page(starturl)
book_list = parse_soup(sp)

print(book_list)

cur.executemany("INSERT OR IGNORE INTO books VALUES (?,?,?)", book_list)
con.commit()