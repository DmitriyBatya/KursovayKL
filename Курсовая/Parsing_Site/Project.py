from Models import DateBase, Parsing
import requests
from bs4 import BeautifulSoup
soup = Parsing.parse()
db = DateBase.Date()
dct_news = {}
print(soup.news)
for i in range(len(soup.news)):
    soup.Name_News(i)
    soup.Link_News(i)
    soup.Date_news(i)
    soup.Views_News(i)
    soup.Comments_News(i)
    verify = db.new.find_one({'Name_news': soup.name})
    if not(verify == 'None'):
        for new in db.new.find():
            if new['Name_news'] == soup.name:
                new['Views_news'] = soup.views
                new['Comments_news'] = soup.comments
    else:
        soup.news = BeautifulSoup(requests.get(
            'https://v1.ru' + soup.news[i].find('h2', class_='MNb9').find('a').get('href')
        ).text, 'lxml').findAll('div', class_='LTawf')
        soup.Text_News()
        dct_news = {
            'Name_news': soup.name,
            'Date_news': soup.date,
            'Link_news': soup.link,
            'Views_news': soup.views,
            'Text_news': soup.text,
            'Comments_news': soup.comments
        }
        db.inset(dct_news)

