import unittest
import requests
import os
import sys
import subprocess
import time
import signal
import psutil
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

sys.path.insert(0, '')
from mgflask import news_retrieval
from mgflask.db import Base, engine


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
host = "http://127.0.0.1:5000"
endpoint = "news"
baseUrl = host + "/"+endpoint
app_name = 'mgflask'
today = strftime(datetime.today())
oneMonthBefore = strftime(datetime.today() - relativedelta(months=1) + timedelta(days=1))

class TestNews(unittest.TestCase):


    def test_1_list_params(self):
        test_params = {'source': ["cnn", 'bbc-news'], 'title': [
                            "opinion", "covid"], 'publishedAt': [oneMonthBefore, today]}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test1 list parameters----------------")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()['articles']), 0)
        for article in response.json()['articles']:
            self.assertIn(article['source'], test_params['source'])
            self.assertRegex( article['title'].lower(), "|".join(test_params['title']))
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][1]))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0]))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])
     
    def test_2_single_param(self):        
        test_params = {'source': "cnn", 'title': "vaccine", 'publishedAt': today, 'limit_articles': 5}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test2 single parameters----------------")
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.json()['articles']), test_params['limit_articles'])
        self.assertGreater(len(response.json()['articles']), 0)
        for article in response.json()['articles']:
            self.assertEqual(article['source'], test_params['source'])
            self.assertIn(test_params['title'], article['title'].lower())
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'])+timedelta(days=1))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt']))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])
    
    def test_3_singletonlist_param(self): 
        test_params = {'source': ["cnn"], 'title': ["vaccine"], 'publishedAt': [today]}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test3 singleton list parameters----------------")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()['articles']), 0)
        for article in response.json()['articles']:
            self.assertIn(article['source'], test_params['source'])
            self.assertRegex( article['title'].lower(), "|".join(test_params['title']))
            self.assertLessEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0])+timedelta(days=1))
            self.assertGreaterEqual(strptime(article['publishedAt']), strptime(test_params['publishedAt'][0]))
            # print("source: ", article['source'])
            # print("title: ", article['title'])
            # print("publishedAt: ", article['publishedAt'])

    def test_4_no_paramself(self):
        response = requests.get(baseUrl)
        print("----------------test4 no parameters ----------------")
        self.assertGreater(len(response.json()['articles']), 0)
        # for article in response.json()['articles'][:5]:
             # print("source: ", article['source'])
             # print("title: ", article['title'])
             # print("publishedAt: ", article['publishedAt'])

    def test_5_partition_by(self):
        test_params = {'partition_by': 'source', 'publishedAt': [oneMonthBefore, today]}
        response = requests.get(baseUrl, params=test_params)
        self.assertLessEqual(response.status_code, 200)
        print("----------------test5 partition_by ----------------")
        self.assertGreater(len(response.json()['articles']), 0)
        for partition_key, partition in response.json()['articles'].items():
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
        news_retrieval.get_headlines(q="US", qintitle="US", page_size=80, language='en', page=1, 
                                  sources = "bbc-news, fox-news, the-wall-street-journal, national-review, the-huffington-post, the-hill, cnn")
        news_retrieval.get_everything(q="US", qintitle="US", page_size=80, language='en',
                                  page=1, sources="cnn, bbc-news", from_param=oneMonthBefore, to=today)
        
        '''
        global server_proc
        server_proc=subprocess.Popen("export FLASK_APP="+app_name+ " && flask run", shell = True, cwd="..")
        time.sleep(3)
        
        '''
    @classmethod
    def tearDownClass(cls):
       Base.metadata.drop_all(bind=engine)
       '''
       if server_proc is None:
            pass
       else:
            for child in psutil.Process(server_proc.pid).children(recursive=True):
                child.kill()
            server_proc.kill()
       '''
       
if __name__ == '__main__':
    unittest.main()