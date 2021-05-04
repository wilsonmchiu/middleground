from mgflask import news_util

news_util.get_headlines(q="US", qintitle="US", page_size=80, language='en', page=1, sources="bbc-news")
news_util.get_everything(q="US", qintitle="US", page_size=80, language='en', page=1, sources="cnn", from_param="2021-04-04", to="2021-05-03")