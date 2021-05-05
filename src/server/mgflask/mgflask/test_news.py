import requests

baseUrl = "http://127.0.0.1:5000/news"

response = requests.get(baseUrl, json={'source': ["cnn", 'bbc-news'], 'title': ["opinion", "covid"], 'publishedAt': ['2021-04-25', '2021-05-03'], 'limit_articles':5})
print("----------------test1 list parameters----------------")
for article in response.json()['articles']:
	print("source: ", article['source'])
	print("title: ", article['title'])
	print("publishedAt: ", article['publishedAt'])

response = requests.get(baseUrl, json={'source': "cnn", 'title': "covid", 'publishedAt': '2021-04-03', 'limit_articles':5})
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


