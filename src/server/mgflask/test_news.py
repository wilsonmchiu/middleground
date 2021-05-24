import unittest
import requests
import os
import subprocess
import time


######################## initialize variables ################################################

host = "http://127.0.0.1:5000"
endpoint = "news"
baseUrl = host + "/"+endpoint
app_name = 'mgflask'
server_proc = None


################################# Unit Test Class ############################################################

class TestNews(unittest.TestCase):

    def test_1_list_params(self):
        response = requests.get(baseUrl, params={'source': ["cnn", 'bbc-news'], 'title': [
                            "opinion", "covid"], 'publishedAt': ['2021-04-25', '2021-05-03'], 'limit_articles': 5})
        print("----------------test1 list parameters----------------")
        for article in response.json()['articles']:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])
    
    def test_2_single_paramself(self):        
        response = requests.get(baseUrl, params={'source': "cnn", 'title': "opinion", 'publishedAt': '2021-04-25', 'limit_articles': 5})
        print("----------------test2 single parameters----------------")
        for article in response.json()['articles']:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])

    def test_3_no_paramself(self):
        response = requests.get(baseUrl)
        print("----------------test3 no parameters ----------------")
        for article in response.json()['articles'][:5]:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])

    def test_4_partition_by(self):
        response = requests.get(baseUrl, params={'partition_by': 'source', 'limit_articles': 50, 'publishedAt': ['2021-04-20', '2021-05-31']})
        print("----------------test4 parameter:partition_by ----------------")
        for partition_key, partition in response.json()['articles'].items():
            print( partition_key, ": ")
            for article in partition:
                print("source: ", article['source'])
                print("title: ", article['title'])
                print("publishedAt: ", article['publishedAt'])

'''
    @classmethod
    def setUpClass(cls):
        server_proc = subprocess.Popen("export FLASK_APP="+app_name+ " && flask run", shell = True, cwd="..")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
       server_proc.kill()
       '''

if __name__ == '__main__':
    unittest.main()