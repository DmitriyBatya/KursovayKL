import requests
from bs4 import BeautifulSoup
class parse:
    def __init__(self):
        self.get_html = requests.get("https://v1.ru/text/").text
        print(self.get_html)
        self.news = BeautifulSoup(self.get_html, 'lxml').findAll('article', class_='MNazv')
        print(self.news)
        self.name = ''
        self.link = ''
        self.date = ''
        self.views = ''
        self.comments = ''
        self.text = ''

    def Name_News(self, idx):
        self.name = self.news[idx].find('h2', class_='MNb9').find('a').text

    def Link_News(self, idx):
        self.link = 'https://v1.ru' + self.news[idx].find('h2', class_='MNb9').find('a').get('href')

    def Date_news(self, idx):
        self.date = self.news[idx].find('time').get('datetime')

    def Views_News(self, idx):
        self.views = self.news[idx].find('div', class_='LXch').find('span').text.replace("\xa0", "")

    def Comments_News(self, idx):
        if self.news[idx].find('div', class_='LXawl').findAll('span', class_='LXbt')[1].text == " Обсудить ":
            self.comments = "0"
        else:
            self.comments = self.news[idx].find('div', class_='LXawl').findAll('span', class_='LXbt')[1].text

    def Text_News(self):
        txt = ''
        for i in range(len(self.news)):
            s = self.news[i].findAll('p')
            for j in range(len(s)):
                txt += s[j].text + '\n'
        self.text = txt




