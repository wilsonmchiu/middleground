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


def parse_time(time_str):
    return datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S')     

class TestNews(unittest.TestCase):

    def test_1_list_params(self):
        test_params = {'source': ["cnn", 'bbc-news'], 'title': [
                            "opinion", "covid"], 'publishedAt': ['2021-04-25', '2021-05-23'], 'limit_articles': 5}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test1 list parameters----------------")
        assertEqual(response.status_code, 200)
        asserLess(len(response.json()['articles']), test_params['limit_articles'])
        for article in response.json()['articles']:
            assertIn(article['source'], test_params['source'])
            assertIn(article['title'], test_params['title'])
            assertLessEqual(parse_time(article['publishedAt']), parse_time(test_params['publishedAt'][1]))
            assertLessEqual(parse_time(article['publishedAt'][0]), parse_time(test_params['publishedAt']))
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])
    
    def test_2_single_param(self):        
        test_params = {'source': "cnn", 'title': "vaccine", 'publishedAt': '2021-05-21', 'limit_articles': 5}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test2 single parameters----------------")
        for article in response.json()['articles']:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])
    
    def test_3_singletonlist_param(self): 
        test_params = {'source': ["cnn"], 'title': ["vaccine"], 'publishedAt': ['2021-05-21'], 'limit_articles': 5}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test3 singleton list parameters----------------")
        for article in response.json()['articles']:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])

    def test_4_no_paramself(self):
        response = requests.get(baseUrl)
        print("----------------test4 no parameters ----------------")
        for article in response.json()['articles'][:5]:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])

    def test_5_partition_by(self):
        test_params = {'partition_by': 'source', 'limit_articles': 10, 'publishedAt': ['2021-04-20', '2021-05-31']}
        response = requests.get(baseUrl, params=test_params)
        print("----------------test5 partition_by ----------------")
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