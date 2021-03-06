import unittest

from flask import Flask, jsonify, Blueprint
from mgflask.db import db_session, Base, engine
from mgflask.models import User, Article, Comment, Reply, ArticleRating, CommentRating, ReplyRating
from mgflask import comments, test_news
from mgflask.comments import bp as comments_bp
from mgflask.replies import bp as replies_bp
from flask import json


comments_app = Flask(__name__)
comments_app.register_blueprint(comments_bp, url_prefix='')
replies_app = Flask(__name__)
replies_app.register_blueprint(replies_bp, url_prefix='')

# app.app_context()

class TestEmptyComments(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(bind=engine) 
        Base.metadata.create_all(bind=engine) 
        user1 = User(username='GOODUSER', password='password')
        article1 = Article(author='ARTICLE 1', source='t source', title='title', content='content', description='desc')
        db_session.add(user1)
        db_session.add(article1)
        db_session.commit()

        # articles = db_session.query(Article).all()
        # users = db_session.query(User).all()
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine) 

    def test_post_bad_username(self):
        # print("test_post_bad_username test\n")
        testdata = json.dumps({'username': "BADUSER", 'articleID': '1', 'userComment': "Comment 1"})
        response = comments_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "username BADUSER does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNone(comments)

    def test_post_bad_article(self):
        # print("test_post_bad_article test\n")
        testdata = json.dumps({'username': "GOODUSER", 'articleID': '5555', 'userComment': "Comment 1"})
        response = comments_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "article id 5555 does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNone(comments)

    def test_post_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'username': "GOODUSER", 'articleID': '1', 'userComment': "Comment 1"})
        response = comments_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['insert_status'], "success")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNotNone(comments)
    
    def test_delete_empty(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '1'})
        response = comments_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "comment id 1 does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNone(comments)
    
    def test_edit_empty(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '1', 'content': 'Comment 1'})
        response = comments_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "comment id 1 does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNone(comments)

class TestNonEmptyComments(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(bind=engine) 
        Base.metadata.create_all(bind=engine) 
        user1 = User(username='GOODUSER', password='password')
        article1 = Article(author='ARTICLE 1', source='t source', title='title', content='content', description='desc')
        comment1 = Comment(article_id='1', username='GOODUSER', content='COMMENT 1')

        db_session.add(user1)
        db_session.add(article1)
        db_session.add(comment1)
        db_session.commit()

        # articles = db_session.query(Article).all()
        # users = db_session.query(User).all()
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine) 
    
    def test_delete_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '1'})
        response = comments_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['status'], "success")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNone(comments)

    def test_delete_fail(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '2'})
        response = comments_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "comment id 2 does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNotNone(comments)
    
    def test_edit_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '1', 'content': 'Comment 1'})
        response = comments_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['status'], "success")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNotNone(comments)


    def test_edit_fail(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'commentID': '2', 'content': 'Comment 1'})
        response = comments_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "comment id 2 does not exist in the database")
        comments = db_session.query(Comment).one_or_none()
        self.assertIsNotNone(comments)
    
class TestEmptyReplies(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(bind=engine) 
        Base.metadata.create_all(bind=engine) 
        user1 = User(username='GOODUSER', password='password')
        article1 = Article(author='ARTICLE 1', source='t source', title='title', content='content', description='desc')
        comment1 = Comment(article_id='1', username='GOODUSER', content='COMMENT 1')

        db_session.add(user1)
        db_session.add(article1)
        db_session.add(comment1)
        db_session.commit()

        # articles = db_session.query(Article).all()
        # users = db_session.query(User).all()
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine) 

    def test_post_bad_username(self):
        # print("test_post_bad_username test\n")
        testdata = json.dumps({'username': "BADUSER", 'commentID': '1', 'userReply': "Reply 1"})
        response = replies_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "username BADUSER does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNone(replies)

    def test_post_bad_comment(self):
        # print("test_post_bad_article test\n")
        testdata = json.dumps({'username': "GOODUSER", 'commentID': '5555', 'userReply': "Reply 1"})
        response = replies_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "replyID 5555 does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNone(replies)

    def test_post_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'username': "GOODUSER", 'commentID': '1', 'userReply': "Reply 1"})
        response = replies_app.test_client().post(
            '/post',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['insert_status'], "success")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNotNone(replies)
    
    def test_delete_empty(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '1'})
        response = replies_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "replyID 1 does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNone(replies)
    
    def test_edit_empty(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '1', 'content': 'Reply 1'})
        response = replies_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "replyID 1 does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNone(replies)

class TestNonEmptyReplies(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(bind=engine) 
        Base.metadata.create_all(bind=engine) 
        user1 = User(username='GOODUSER', password='password')
        article1 = Article(author='ARTICLE 1', source='t source', title='title', content='content', description='desc')
        comment1 = Comment(article_id='1', username='GOODUSER', content='COMMENT 1')
        reply1 = Reply(comment_id='1', username='GOODUSER', content='content')

        db_session.add(user1)
        db_session.add(article1)
        db_session.add(comment1)
        db_session.add(reply1)
        db_session.commit()

        # articles = db_session.query(Article).all()
        # users = db_session.query(User).all()
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine) 
    
    def test_delete_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '1'})
        response = replies_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['status'], "success")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNone(replies)

    def test_delete_fail(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '2'})
        response = replies_app.test_client().put(
            '/delete',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "replyID 2 does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNotNone(replies)
    
    def test_edit_success(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '1', 'content': 'Reply 1'})
        response = replies_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "comment successful")
        self.assertEqual(data['status'], "success")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNotNone(replies)

    def test_edit_fail(self):
        # print("test_post_success test\n")
        testdata = json.dumps({'replyID': '2', 'content': 'Reply 1'})
        response = replies_app.test_client().put(
            '/edit',
            data=testdata,
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Unsuccessful. Check Exceptions.")
        self.assertEqual(data['exception'], "replyID 2 does not exist in the database")
        replies = db_session.query(Reply).one_or_none()
        self.assertIsNotNone(replies)

if __name__ == '__main__':
    unittest.main()