from pymongo import MongoClient
class Date:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.news_parse
        self.new = self.db.news

    def inset(self, date_news):
        self.new.insert_one(date_news)

