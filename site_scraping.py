from bs4 import BeautifulSoup
import requests
import sqlite3

url = f"https://www.myanmar-now.org/en/news"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

conn = sqlite3.connect('data.db')

db = conn.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS articles (
            title TEXT,
            links TEXT,
            author TEXT,
            body TEXT,
            dates TEXT
            )""")

conn.commit()

articles = {}

news_title = []
author = []
body = []
dates = []
links = []

article_locations = doc.find_all(class_="news-image")
for a in article_locations:
    urls = a.find('a')
    full_urls = f"https://www.myanmar-now.org{urls['href']}"
    links.append(full_urls)

titles = doc.find_all(class_='news-title')
for b in titles:
    title = b.find('a').string
    news_title.append(title)

for i in range(len(links)):
    articles[news_title[i]] = links[i]


#db.execute("""INSERT INTO articles (title, links) VALUES( 'potato', 'tomato')""")
conn.commit()


conn.close()