# Myanmar News Web Scraper
#### Video Demo:  https://youtu.be/TIwn9LWC7vA
#### Description:
TODO

firstly the program asks the user for an input of how many pages of the myanmar news website they would like to scrape and display. That input then geos through several checks to make sure that it is a positive integer.
If it is then it makes sure the number is now above 100, for the sake of the website not crashing or the users computer crashing if someone inputs a very high number. If those checks are not passed it asks the user to use a number from  1 - 100 untill the user provides it.

Then the inputed number between 1 - 100 from the user gets used to determine how many times the webscraper will run, and each time it does the page number in the url increases by one. This causes the program the run the same scraping code just on a different page with different articles to scrape. The program stores each articles title, link, summary, and date it was published. It accomplishes this by using beautiful soup, which i had to learn when making this project, i did now know beautiful soup prior to this. Beautiful soup allows you to take a html page and read what is inside of it and locate specific keywords and datatypes to narrow down and locate the exact information you are trying to extract.

Putting all these articles into a database makes them much more accessable to data scientists to analize and for journalists to write about and investigate things happening inside the country.

