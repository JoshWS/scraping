from bs4 import BeautifulSoup
import requests
import sqlite3

pages = int(input("How many pages would you like to scrape? " + "\n"))

for x in range(pages):

    url = f"https://www.myanmar-now.org/en/news?page={x}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    conn = sqlite3.connect('data.db')
    db = conn.cursor()

    #makes table if not exists
    db.execute("""CREATE TABLE IF NOT EXISTS articles (
                article_ID  INTEGER PRIMARY KEY,
                title TEXT,
                link TEXT,
                summary TEXT,
                dates TEXT,
                unique (title)
                )""")

    conn.commit()

    #creating lists to store data to then insert them into table 
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

        for i in range(len(links)):
            try:
                db.execute("""INSERT INTO articles (title, link, summary, dates) VALUES (?, ?, ?, ?)""", (titles[i], links[i], summarys[i], dates[i]))
            except:
                pass
        conn.commit()


    data_entry()



    conn.commit()

    conn.close()