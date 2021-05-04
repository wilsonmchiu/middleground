from flask import Flask, jsonify, Blueprint
from mgflask.db import db_session
from mgflask.models import User, Article, Comment, Reply, ArticleRating, CommentRating, ReplyRating

bp = Blueprint('db', __name__, url_prefix='/test_db')


@bp.route('/', methods=('GET', 'POST'))
def test_db():
    user1 = User(username='user1', password='pass1')
    article1 = Article(author='ARTICLE 1', source='t source',
                       title='title', content='content', description='desc')
    comment1 = Comment(article_id='1', username='user1',
                       content='COMMENT 1')
    reply = Reply(comment_id='1', username='user1',
                  content='content')
    articleRating = ArticleRating(item_id='1', username='user1')
    commentRating = CommentRating(item_id='1', username='user1')
    replyRating = ReplyRating(item_id='1', username='user1')

    db_session.add(user1)
    db_session.add(article1)
    db_session.add(comment1)
    db_session.add(reply)
    db_session.add(articleRating)
    db_session.add(commentRating)
    db_session.add(replyRating)
    db_session.commit()

    articles = db_session.query(Article).all()
    comments = db_session.query(Comment).all()
    replies = db_session.query(Reply).all()
    article_ratings = db_session.query(ArticleRating).all()
    comment_ratings = db_session.query(CommentRating).all()
    reply_ratings = db_session.query(ReplyRating).all()

    return jsonify(articles=[c.serialize for c in articles],
                   comments=[c.serialize for c in comments],
                   replies=[c.serialize for c in replies],
                   article_ratings=[c.serialize for c in article_ratings],
                   comment_ratings=[c.serialize for c in comment_ratings],
                   reply_ratings=[c.serialize for c in reply_ratings])
