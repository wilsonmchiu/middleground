import requests
from mgflask import news_retrieval

# call test_trieval() to put articles into the database
# call test_endpoint() to get articles from database (make sure the server is running)


def test_retrieval():
    news_retrieval.get_headlines(
        q="US", qintitle="US", page_size=80, language='en', page=1, sources = "bbc-news, fox-news, the-wall-street-journal, national-review, the-huffington-post, the-hill, cnn")
    news_retrieval.get_everything(q="US", qintitle="US", page_size=80, language='en',
                                  page=1, sources="cnn, bbc-news", from_param="2021-04-20", to="2021-05-03")


def test_endpoint():
    baseUrl = "http://127.0.0.1:5000/news"

    response = requests.get(baseUrl, json={'source': ["cnn", 'bbc-news'], 'title': [
                            "opinion", "covid"], 'publishedAt': ['2021-04-25', '2021-05-03'], 'limit_articles': 5})
    print("----------------test1 list parameters----------------")
    for article in response.json()['articles']:
        print("source: ", article['source'])
        print("title: ", article['title'])
        print("publishedAt: ", article['publishedAt'])

    response = requests.get(baseUrl, json={
                            'source': "cnn", 'title': "opinion", 'publishedAt': '2021-04-25', 'limit_articles': 5})
    print("----------------test2 single parameters----------------")
    for article in response.json()['articles']:
        print("source: ", article['source'])
        print("title: ", article['title'])
        print("publishedAt: ", article['publishedAt'])

    response = requests.get(baseUrl)
    print("----------------test3 no parameters ----------------")
    for article in response.json()['articles'][:5]:
        print("source: ", article['source'])
        print("title: ", article['title'])
        print("publishedAt: ", article['publishedAt'])

    response = requests.get(baseUrl, json={'partition_by': 'source', 'limit_articles': 50, 'publishedAt': '2021-05-11'})
    print("----------------test4 parameter:organized_by ----------------")
    for partition_key, partition in response.json()['articles'].items():
        print( partition_key, ": ")
        for article in partition:
            print("source: ", article['source'])
            print("title: ", article['title'])
            print("publishedAt: ", article['publishedAt'])


test_endpoint()
