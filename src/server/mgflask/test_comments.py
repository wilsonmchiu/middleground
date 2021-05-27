import unittest

from flask import Flask, jsonify, Blueprint
from mgflask.db import db_session, Base, engine
from mgflask.models import User, Article, Comment, Reply, ArticleRating, CommentRating, ReplyRating
from mgflask import comments
from comments import bp
from flask import json

class TestComments(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(bind=engine) 
        user1 = User(username='GOODUSER', password='password')
        article1 = Article(author='ARTICLE 1', source='t source', title='title', content='content', description='desc')
        db_session.add(user1)
        db_session.add(article1)
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine) 

    def post_bad_username(self):
        testdata = json.dumps({'username': "BADUSER", 'articleID': '1', 'userComment': "Comment 1"})
        response = bp.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.msg, "Unsuccessful. Check Exceptions.")
        self.assertEqual(response.exception, "username BADUSER does not exist in the database")
        comments = db_session.query(Comment).one()
        self.assertIsNone(comments)

    def post_bad_article(self):
        testdata = json.dumps({'username': "GOODUSER", 'articleID': '5555', 'userComment': "Comment 1"})
        response = bp.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.msg, "Unsuccessful. Check Exceptions.")
        self.assertEqual(response.exception, "article id 5555 does not exist in the database")
        comments = db_session.query(Comment).one()
        self.assertIsNone(comments)

    def post_success(self):
        testdata = json.dumps({'username': "GOODUSER", 'articleID': '1', 'userComment': "Comment 1"})
        response = bp.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.msg, "comment successful")
        self.assertEqual(response.insert_status, "success")
        comments = db_session.query(Comment).one()
        self.assertIsNotNone(comments)
    
if __name__ == '__main__':
    unittest.main()