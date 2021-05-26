import unittest

from flask import Flask, jsonify, Blueprint
from mgflask.db import db_session
from mgflask.models import User, Article, Comment, Reply, ArticleRating, CommentRating, ReplyRating
from mgflask import comments

class TestComments(unittest.TestCase):

    def test_insert(self):
        comment1 = Comment(article_id='1', username='Andrew', content='COMMENT 1')
        db_session.add(comment1)
        comments = db_session.query(Comment).all()
        self.assertIn(comment1, comments)

        reply1 = Reply(comment_id='1', username='user1', content='content')
        db_session.add(reply1)
        replies = db_session.query(Reply).all()
        self.assertIn(reply1, replies)
