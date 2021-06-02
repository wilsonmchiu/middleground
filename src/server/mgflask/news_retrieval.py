from newsapi import NewsApiClient 
from mgflask.db import db_session
from mgflask.models import Article
from sqlalchemy import and_
from datetime import datetime

API_KEYS = ['983d4d9ce3dc4f3badda1a1171eb548d', 'b5ad966ba07741858c365a83ed18a0bb']
KEY_INDEX_PARAM = "api_key_index"
TARGET_SOURCES = ["bbc-news", "fox-news", "the-wall-street-journal", "national-review", "the-huffington-post", "the-hill", "cnn"]
# documentation on newsapi parameters: https://newsapi.org/docs/endpoints/top-headlines 
# newsapi-python implementation: https://github.com/mattlisiv/newsapi-python/blob/master/newsapi/newsapi_client.py
EVERYTHING_PARAMS= [ 'sources','qintitle','q','domains','exclude_domains', 'from_param', 'to', 'language', 'sortBy', 'page','page_size']
HEADLINES_PARAMS= [ 'sources','qintitle','q', 'country', 'category', 'language', 'page','page_size']


def get_headlines(**args):
    request_params = {}
    request_params['language']='en'   #English by default
    request_params['page_size']= 100
    if 'sources' not in args and 'category' not in args and not 'country' not in args: #country and category cannot coexist with sources
      request_params['sources']=','.join(TARGET_SOURCES)   #target sources by default
    for key in args:
      if key in HEADLINES_PARAMS:
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
    request_params['sources']=','.join(TARGET_SOURCES)   #target sources by default
    for key in args:
      if key in EVERYTHING_PARAMS:
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

def populate_db():
  """
  Used to populate database in whichever db
  instance you are using.
  REFERENCE: This acts the same as test_retrieval() 
  from previous commit iterations
  """
  get_headlines( q="US", qintitle="US", page_size=80, language='en', page=1,
   sources = "bbc-news, fox-news, the-wall-street-journal, national-review, the-huffington-post, the-hill, cnn")
  get_everything(q="US", qintitle="US", page_size=80, language='en',page=1, sources="cnn, bbc-news", from_param="2021-05-05", to="2021-05-20")

def insert_articles(newsapi_articles):
  count=0;
  duplicate_count=0
  for article in newsapi_articles:
    if not article['content']: #throw away articles with no content
      continue
    if db_session.query(Article.id).filter(and_(Article.url==article['url'], Article.description==article['description'])).all():   
      #check for duplicates by matching the descriptions and url. Could be changed to check with other fields as well
      duplicate_count+=1
      continue
    if article['source']['id']:    #source id could be None 
      article['source'] = article['source']['id']          
    else:                           #use source name as backup
      article['source'] = article['source']['name']
    #remove redundant digits and convert to a datetime object        
    article['publishedAt'] = datetime.strptime(article['publishedAt'][:19], '%Y-%m-%dT%H:%M:%S')     
    db_article = Article(**article)
    db_session.add(db_article)
    count+=1

  db_session.commit()
  print(str(duplicate_count), " duplicate articles detected")
  print(str(count), " articles inserted into database")

def get_api_key(args): 
  if isinstance(args, dict) and KEY_INDEX_PARAM in args:
    index = int(args[KEY_INDEX_PARAM])
    if index < 0 or index >= len(API_KEYS):
      raise IndexError(f"{api_key_index_param} {index} is out of range");
    else:
      return API_KEYS[index]
  else:
      return API_KEYS[0]