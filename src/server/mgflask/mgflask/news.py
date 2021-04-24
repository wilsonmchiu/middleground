from flask import (
    Blueprint,
    request,
    jsonify
)
from newsapi import NewsApiClient 

bp = Blueprint('news', __name__, url_prefix='/news')

api_keys = ['983d4d9ce3dc4f3badda1a1171eb548d', 'b5ad966ba07741858c365a83ed18a0bb']
target_sources = ["bbc-news", "fox-news", "the-wall-street-journal", "national-review", "the-huffington-post", "the-hill", "cnn"]
accepted_params= [ 'sources','qintitle','q','domains','excludeDomains', 'from', 'to', 'language', 'sortBy']
accepted_params_int = ['page','pageSize']
api_key_index_param = 'api_key_index'


#get headlines from all target sources
@bp.route('/headlines', methods=['GET'])
def get_headlines_from_all():
    topheadlines = {}
    try:
      api_key = get_api_key(request)
      newsapi = NewsApiClient(api_key=api_key)
      sources = ",".join(target_sources)
      topheadlines = newsapi.get_top_headlines(sources=sources)
    except (IndexError, ValueError)as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)

#get headlines from a designated target source
@bp.route('/headlines/<news_source>', methods=['GET'])
def get_headlines_from(news_source):
    topheadlines = {}
    try:
      api_key = get_api_key(request)
      newsapi = NewsApiClient(api_key=api_key)
      topheadlines = newsapi.get_top_headlines(sources=news_source)
    except (IndexError, ValueError) as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)

#search among all articles
@bp.route('/', methods=['GET'])
def get_everything():
    topheadlines = {}
    request_params = {}
    request_params['language']='en'   #Englsih by default
    request_params['sources']=','.join(target_sources)   #target sources by default
    print(request_params)
    for arg in request.args:
      if arg in accepted_params:
        request_params[arg] = request.args.get(arg)
      if arg in accepted_params_int:
         request_params[arg] = int(request.args.get(arg))
    try:
      api_key = get_api_key(request)
      newsapi = NewsApiClient(api_key=api_key)
      topheadlines = newsapi.get_everything(**request_params)
    except (IndexError, ValueError) as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)

# 0 by default, raises IndexError if out of range, raises ValueError if index cannot be converted to int
def get_api_key(request):
  index_str =  request.args.get(api_key_index_param)
  if index_str:
    index = int(index_str)
    if index < 0 or index >= len(api_keys):
      raise IndexError(f"{api_key_index_param} {index} is out of range");
    else:
      return api_keys[index]
  else:
      return api_keys[0]
