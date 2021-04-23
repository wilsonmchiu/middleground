from flask import (
    Blueprint,
    request,
    jsonify,
    request
)
from newsapi import NewsApiClient 

bp = Blueprint('news', __name__, url_prefix='/news')

api_keys = ['983d4d9ce3dc4f3badda1a1171eb548d', 'b5ad966ba07741858c365a83ed18a0bb']
target_sources = ["bbc-news", "fox-news", "the-wall-street-journal", "national-review", "the-huffington-post", "the-hill", "cnn"]
accepted_params= [ 'sources','qintitle','q','domains','excludeDomains', 'from', 'to', 'language', 'sortBy', 'page', 'pageSize']


#get headlines from all target sources
@bp.route('/headlines', methods=['GET'])
def get_headlines_from_all():
    topheadlines = {}
    newsapi = NewsApiClient(api_key=api_keys[0])
    sources = ",".join(target_sources)
    print(str(request_params))
    try:
      topheadlines = newsapi.get_top_headlines(sources=sources)
    except ValueError as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)

#get headlines from a designated target source
@bp.route('/headlines/<news_source>', methods=['GET'])
def get_headlines_from(news_source):
    newsapi = NewsApiClient(api_key=api_keys[0])
    try:
      topheadlines = newsapi.get_top_headlines(sources=news_source)
    except ValueError as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)

#search among all articles
@bp.route('/everything', methods=['GET'])
def get_everything():
    topheadlines = {}
    request_params = {}
    newsapi = NewsApiClient(api_key=api_keys[0])
    request_params['language']='en'   #Englsih by default
    request_params['sources']=','.join(target_sources)   #target sources by default
    for arg in request.args:
      if arg in accepted_params:
        request_params[arg] = request.args.get(arg)
    try:
      topheadlines = newsapi.get_everything(**request_params)
    except ValueError as e:
      topheadlines['status'] = 'error'
      topheadlines['message'] = str(e)

    return jsonify(topheadlines)
    