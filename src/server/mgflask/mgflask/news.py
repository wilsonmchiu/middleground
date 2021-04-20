from flask import (
    Blueprint,
    request,
    jsonify
)
from newsapi import NewsApiClient

bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/asdf', methods=('GET', 'POST'))
def testNewsAPI():
    newsapi = NewsApiClient(api_key='983d4d9ce3dc4f3badda1a1171eb548d')
    top_headlines = newsapi.get_everything(q='bitcoin',
                                           sources='bbc-news,the-verge',
                                           domains='bbc.co.uk,techcrunch.com',
                                           language='en',
                                           sort_by='relevancy')
    return jsonify(top_headlines)
