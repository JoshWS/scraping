from bs4 import BeautifulSoup
import requests
import sqlite3

# ask for user input for amount of pages, check to make sure the input is a positive integer.
while True:
    try:
        pages = int(input("How many pages would you like to scrape and display? " + "\n"))
    except ValueError:
        print('Sorry Please try a number form 1 - 100')
        continue
    else:
        if pages <= 0:
            continue
        else:
            if pages > 100:
                continue
            else:
                break


conn = sqlite3.connect('data.db')
db = conn.cursor()

#makes table if not exists
#db.execute("""DROP TABLE articles""")
db.execute("""CREATE TABLE IF NOT EXISTS articles (
            article_ID  INTEGER PRIMARY KEY,
            title TEXT,
            link TEXT,
            summary TEXT,
            dates TEXT,
            unique (title)
            )""")

conn.commit()

# finds the locations of the each piece of data and isolates the data a want in the format I need it in
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


    conn = sqlite3.connect('data.db')
    db = conn.cursor()
    for i in range(len(links)):
        try:
            db.execute("""INSERT INTO articles (title, link, summary, dates) VALUES (?, ?, ?, ?)""", (titles[i], links[i], summarys[i], dates[i]))
        except:
            pass
    conn.commit()
    conn.close()

# iterate through each page and grabs all the information from the articles that I scrape for 
for x in range(pages):

    url = f"https://www.myanmar-now.org/en/news?page={x}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    #creating lists to store data to then insert them into table 
    titles = []
    links = []
    summarys = []
    dates = []

    data_entry()



conn = sqlite3.connect('data.db')
db = conn.cursor()

# displays the data in a organized way
displayed_data = pages * 13
iterations = 0
db.execute("""SELECT * FROM articles""")
data = db.fetchall()
for d in data:
    iterations += 1
    if iterations > displayed_data:
        break
    
    print(f"----------{d[0]}----------")
    print(f"TITLE: {d[1]}")
    print(f"LINK: {d[2]}")
    print(f"SUMMARY: {d[3]}")
    print(f"DATE: {d[4]}")
    print('\n')

conn.commit()
conn.close()