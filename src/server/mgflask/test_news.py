import unittest
import requests
import os
import subprocess
import time
import signal
import psutil



host = "http://127.0.0.1:5000"
endpoint = "news"
baseUrl = host + "/"+endpoint
app_name = 'mgflask'


class TestNews(unittest.TestCase):

    def test_1_list_params(self):
        response = requests.get(baseUrl, params={'source': ["cnn", 'bbc-news'], 'title': [
                            "opinion", "covid"], 'publishedAt': ['2021-04-25', '2021-05-23'], 'limit_articles': 5})
        print("----------------test1 list parameters----------------")
        for article in response.json()['articles']:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])
    
    def test_2_single_paramself(self):        
        response = requests.get(baseUrl, params={'source': "cnn", 'title': "vaccine", 'publishedAt': '2021-05-21', 'limit_articles': 5})
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
        response = requests.get(baseUrl, params={'partition_by': 'source', 'limit_articles': 10, 'publishedAt': ['2021-04-20', '2021-05-31']})
        print("----------------test4 parameter:partition_by ----------------")
        for partition_key, partition in response.json()['articles'].items():
            print( partition_key, ": ")
            for article in partition:
                print("source: ", article['source'])
                print("title: ", article['title'])
                print("publishedAt: ", article['publishedAt'])

    @classmethod
    def setUpClass(cls):
        global server_proc
        server_proc=subprocess.Popen("export FLASK_APP="+app_name+ " && flask run", shell = True, cwd="..")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
       if server_proc is None:
            pass
       else:
            for child in psutil.Process(server_proc.pid).children(recursive=True):
                child.kill()
            server_proc.kill()

if __name__ == '__main__':
    unittest.main()