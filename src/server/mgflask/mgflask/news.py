from flask import (
    Blueprint,
    request,
    jsonify
)
from newsapi import NewsApiClient 
from datetime import datetime
from mgflask.db import db_session
from mgflask.models import Article
from sqlalchemy import and_, or_

bp = Blueprint('news', __name__, url_prefix='/news')

# Query parameters should be sent in json format in request body. Accepted parameters are values are defined below.
# Each query parameter can contain a single or a list of accepted values. 

# these columns are defined in model.py to match news.api parameters: https://newsapi.org/docs/endpoints/top-headlines
# exact_columns need to match exactly
exact_columns= [ 'id', 'author', 'source', 'url', 'urlToImage']
# fuzzy_columns uses the LIKE operator to partically match
fuzzy_columns = ['title', 'content', 'description']
# for range columns the first two values will be interpreted as the lower and upper bouond and the rest discarded (if only one value then it will be the lower bound) 
range_columns = ['leftBias', 'right-Bias', 'publishedAt']
# query on comments and article_ratings not yet implemented

# upper limit on the number of to return
limit_articles_param = 'limit_articles'

#search among all articles
@bp.route('/', methods=['GET'])
def get_articles():
    params = request.json
    filters = []

    if params: 
      for col in Article.__table__.columns:
        param = params.get(col.key)
        if col.key in exact_columns and param:
          if isinstance(param, list):
            filters.append(col.in_(param))
          else:
            filters.append( col==param )
        elif col.key in fuzzy_columns and param:
          if isinstance(param, list):
            fuzzy_filters = [col.ilike("%"+each+"%") for each in param]
            filters.append(or_(*fuzzy_filters))
          else:
            filters.append(col.ilike("%"+param+"%"))
        elif col.key in range_columns and param:
          if isinstance(param, list):
            if len(param)>=2:
              filters.append(col.between(param[0], param[1]))
            else:
              filters.append(col>= param[0])
          else:
             filters.append(col>= param)


    articles = db_session.query(Article).filter(and_(*filters))

    if params and params.get(limit_articles_param):
      articles = articles[:params.get(limit_articles_param)]

    return jsonify({"articles":[article.serialize_response for article in articles]})


