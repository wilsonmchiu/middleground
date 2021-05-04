from newsapi import NewsApiClient 
from mgflask.db import db_session
from mgflask.models import User, Article, Comment, Reply, ArticleRating, CommentRating, ReplyRating
from datetime import datetime

api_keys = ['983d4d9ce3dc4f3badda1a1171eb548d', 'b5ad966ba07741858c365a83ed18a0bb']
target_sources = ["bbc-news", "fox-news", "the-wall-street-journal", "national-review", "the-huffington-post", "the-hill", "cnn"]
# documentation on newsapi parameters: https://newsapi.org/docs/endpoints/top-headlines 
# newsapi-python implementation: https://github.com/mattlisiv/newsapi-python/blob/master/newsapi/newsapi_client.py
everything_params= [ 'sources','qintitle','q','domains','exclude_domains', 'from_param', 'to', 'language', 'sortBy', 'page','page_size']
headlines_params= [ 'sources','qintitle','q', 'country', 'category', 'language', 'page','page_size']


def get_headlines(**args):
    request_params = {}
    request_params['language']='en'   #English by default
    request_params['page_size']= 100
    if 'sources' not in args and 'category' not in args and not 'country' not in args: #country and category cannot coexist with sources
      request_params['sources']=','.join(target_sources)   #target sources by default
    for key in args:
      if key in headlines_params:
        request_params[key] = args[key]

    try:
      newsapi = NewsApiClient(api_key=get_api_key(args))
      newsapi_res = newsapi.get_top_headlines(**request_params)
    except (IndexError, ValueError)as e:
      print("retrieve from headlines failed, error: ",str(e))
      return
    if newsapi_res['status']=='error':
      print("retrieve from headlines failed, code: ", newsapi_res['status'], " message: ", newsapi_res['message'])
      return 
    
    insert_articles(newsapi_res['articles'])


def get_everything(**args):
    request_params = {}
    request_params['language']='en'   #English by default
    request_params['sources']=','.join(target_sources)   #target sources by default
    for key in args:
      if key in everything_params:
        request_params[key] = args[key]

    try:
      newsapi = NewsApiClient(api_key=get_api_key(args))
      newsapi_res = newsapi.get_everything(**request_params)
    except (IndexError, ValueError)as e:
      print("retrieve from everything failed, error: ",str(e))
      return
    if newsapi_res['status']=='error':
      print("retrieve from everything failed, code: ", newsapi_res['status'], " message: ", newsapi_res['message'])
      return 
    
    insert_articles(newsapi_res['articles'])


def insert_articles(newsapi_articles):
  count=0;

  for article in newsapi_articles:
    if not article['content']: #throw away articles with no content
      continue
    if article['source']['id']:    #source id could be None 
      article['source'] = article['source']['id']          
    else:                           #use source name as backup
      article['source'] = article['source']['name']        
    article['publishedAt'] = datetime.strptime(article['publishedAt'][:19], '%Y-%m-%dT%H:%M:%S')     #remove redundant digits and convert to datetime object
    db_article = Article(**article)
    db_session.add(db_article)
    count+=1

  db_session.commit()
  print(str(count), " articles inserted into database")

def get_api_key(args): 
  if isinstance(args, dict) and 'api_key_index' in args:
    index = int(args['api_key_index'])
    if index < 0 or index >= len(api_keys):
      raise IndexError(f"{api_key_index_param} {index} is out of range");
    else:
      return api_keys[index]
  else:
      return api_keys[0]