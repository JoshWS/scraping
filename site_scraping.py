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
            link TEXT,
            summary TEXT,
            dates TEXT
            )""")

conn.commit()


titles = []
links = []
summarys = []
dates = []


def data_entry():

    link_locations = doc.find_all(class_='news-image')
    for a in link_locations:
        urls = a.find('a')
        full_urls = f"https://www.myanmar-now.org{urls['href']}"
        links.append(full_urls)


    title_locations = doc.find_all(class_='news-title')
    for b in title_locations:
        title = b.find('a').string
        titles.append(title)
    

    summary_locations = doc.find_all(class_='news-body')
    for c in summary_locations:
        summary = c.string
        summarys.append(summary)


    date_locations = doc.find_all(class_='news-date')
    for d in date_locations:
        date = d.string 
        dates.append(date)


data_entry()


for i in range(len(links)):
    db.execute("""INSERT INTO articles (title, link, summary, dates) VALUES (?, ?, ?, ?)""", (titles[i], links[i], summarys[i], dates[i]))
    conn.commit()

conn.commit()

conn.close()