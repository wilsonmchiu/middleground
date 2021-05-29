import unittest
import requests
import os
import sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json

sys.path.insert(0, os.path.join(sys.path[0], '../..'))
print(sys.path)
from mgflask import news_retrieval, app
from mgflask.db import Base, engine
from flask import Flask


# time functions
def strptime(time_str):
    try:
        return datetime.strptime(time_str, '%Y-%m-%d') 
    except ValueError:
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')  

def strftime(time_obj):
    try:
        return datetime.strftime(time_obj, '%Y-%m-%d')
    except:
        return datetime.strftime(time_obj, '%Y-%m-%d %H:%M:%S')



# variables
endpoint = "news/"
today = strftime(datetime.today())
oneMonthBefore = strftime(datetime.today() - relativedelta(months=1) + timedelta(days=1))

class TestNews(unittest.TestCase):


    def test_1_list_params(self):
        test_params = {'source': ["cnn", 'bbc-news'], 'title': ['a', 'the'], 'publishedAt': [oneMonthBefore, today]}
        response = client.get(endpoint, query_string=test_params)
        print("----------------test1 list parameters----------------")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        for article in data['articles']:
            self.assertIn(article['source'], test_params['source'])
            self.assertRegex( article['title'].lower(), "|".join(test_params['title']))
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][1]))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0]))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])

    def test_2_single_param(self):        
        test_params = {'source': "cnn", 'title': 'a','publishedAt': today, 'limit_articles': 5}
        response = client.get(endpoint, query_string=test_params)
        print("----------------test2 single parameters----------------")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertLessEqual(len(data['articles']), test_params['limit_articles'])
        for article in data['articles']:
            self.assertEqual(article['source'], test_params['source'])
            self.assertIn(test_params['title'], article['title'].lower())
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'])+timedelta(days=1))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt']))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])
    
    def test_3_singletonlist_param(self): 
        test_params = {'source': ["cnn"], 'title': ['a'], 'publishedAt': [today]}
        response = client.get(endpoint, query_string=test_params)
        print("----------------test3 singleton list parameters----------------")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        for article in data['articles']:
            self.assertIn(article['source'], test_params['source'])
            self.assertRegex( article['title'].lower(), "|".join(test_params['title']))
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0])+timedelta(days=1))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0]))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])

    def test_4_no_param(self):
        response = client.get(endpoint)
        print("----------------test4 no parameters ----------------")
        data = json.loads(response.get_data(as_text=True))
        self.assertGreater(len(data['articles']), 0)
        #for article in data['articles']:
             # print("source: ", article['source'])
             # print("title: ", article['title'])
             # print("publishedAt: ", article['publishedAt'])

    def test_5_partition_by(self):
        test_params = {'partition_by': 'source', 'publishedAt': [oneMonthBefore, today]}
        response = client.get(endpoint, query_string=test_params)
        self.assertLessEqual(response.status_code, 200)
        print("----------------test5 partition_by ----------------")
        data = json.loads(response.get_data(as_text=True))
        self.assertGreater(len(data['articles']), 0)
        for partition_key, partition in data['articles'].items():
            # print( partition_key, ": ")
            for article in partition:
                self.assertEqual(article['source'], partition_key)
                self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][1]))
                self.assertGreaterEqual( strptime(article['publishedAt']),strptime( test_params['publishedAt'][0]))
                # print("source: ", article['source'])
                # print("title: ", article['title'])
                # print("publishedAt: ", article['publishedAt'])
                
    @classmethod
    def setUpClass(cls):
        global client
        client = app.test_client()
        
        news_retrieval.get_headlines(q="US", qintitle="US", page_size=80, language='en', page=1, 
                                  sources = "bbc-news, fox-news, the-wall-street-journal, national-review, the-huffington-post, the-hill, cnn")
        news_retrieval.get_everything(q="US", qintitle="US", page_size=80, language='en',
                                  page=1, sources="cnn, bbc-news", from_param=oneMonthBefore, to=today)
        
    @classmethod
    def tearDownClass(cls):
       if engine.url=="sqlite:///test.db":  #avoid deleting production data
           Base.metadata.drop_all(bind=engine)
       

if __name__ == '__main__':
    unittest.main()