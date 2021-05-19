from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from mgflask.db import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True)
    password = Column(String(24), nullable=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
        }


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    publishedAt = Column(DateTime)
    author = Column(String(60))
    source = Column(String(24), nullable=False)
    title = Column(String(60), nullable=False)
    right_bias = Column(Integer, default=0)
    left_bias = Column(Integer, default=0)
    content = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    url = Column(Text)
    urlToImage = Column(Text)
    comments = relationship('Comment', back_populates="article")
    article_ratings = relationship('ArticleRating', back_populates="article")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'publishedAt': self.publishedAt,
            'author': self.author,
            'source': self.source,
            'title': self.title,
            'right_bias': self.right_bias,
            'left_bias': self.left_bias,
            'content': self.content,
            'description': self.description,
            'url': self.url,
            'urlToImage': self.urlToImage,
            'comments': str(self.comments),
            'article_ratings': str(self.article_ratings),
        }

    @property
    def serialize_response(self):
        """Return object data in easily serializeable format as response to the client"""
        return {
            'id': self.id,
            'publishedAt': self.publishedAt.strftime('%Y-%m-%d %H:%M:%S') if self.publishedAt else None,
            'author': self.author,
            'source': self.source,
            'title': self.title,
            'right_bias': self.right_bias,
            'left_bias': self.left_bias,
            'content': self.content,
            'description': self.description,
            'url': self.url,
            'urlToImage': self.urlToImage,
            'comments': [comment.serialize_response for comment in self.comments],
            'article_ratings': [rating.serialize_response for rating in self.article_ratings],
        }


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    article = relationship('Article', back_populates="comments")
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)
    date = Column(DateTime)
    username = Column(String(60), ForeignKey('user.username'))
    user = relationship("User")
    right_bias = Column(Integer, default=0)
    left_bias = Column(Integer, default=0)
    content = Column(Text, nullable=False)
    replies = relationship('Reply', back_populates="comment")
    comment_ratings = relationship('CommentRating', back_populates="comment")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'article_id': self.article_id,
            'date': self.date,
            'user': str(self.user),
            'username': self.username,
            'right_bias': self.right_bias,
            'left_bias': self.left_bias,
            'content': self.content,
            'article': str(self.article),
            'replies': str(self.replies),
            'comment_ratings': str(self.comment_ratings)
        }

    @property
    def serialize_response(self):
        """Return object data as response to the client"""
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else None,
            'username': self.username,
            'right_bias': self.right_bias,
            'left_bias': self.left_bias,
            'content': self.content,
            'comment_ratings': [rating.serialize_response for rating in self.comment_ratings],
        }

class Reply(Base):
    __tablename__ = 'reply'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable=False)
    comment = relationship('Comment')
    date = Column(DateTime)
    user = relationship("User")
    username = Column(String(60), ForeignKey('user.username'))
    right_bias = Column(Integer, default=0)
    left_bias = Column(Integer, default=0)
    content = Column(Text, nullable=False)
    reply_ratings = relationship('ReplyRating', back_populates="reply")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'comment_id': self.comment_id,
            'comment': str(self.comment),
            'date': self.date,
            'user': str(self.user),
            'username': self.username,
            'right_bias': self.right_bias,
            'left_bias': self.left_bias,
            'content': self.content,
            'reply_ratings': str(self.reply_ratings)
        }


class ArticleRating(Base):
    __tablename__ = 'article_rating'
    item_id = Column(Integer, ForeignKey('article.id'),
                     primary_key=True, nullable=False)
    username = Column(String(24), ForeignKey('user.username'),
                      nullable=False, primary_key=True)
    user = relationship('User')
    rated = Column(Boolean, default=False)
    article = relationship('Article')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'item_id': self.item_id,
            'username': self.username,
            'user': str(self.user),
            'rated': self.rated,
            'article': str(self.article),
        }

    @property
    def serialize_response(self):
        """Return object data as response to the client"""
        return {
            'username': self.username,
            'rated': self.rated,
        }


class CommentRating(Base):
    __tablename__ = 'comment_rating'
    item_id = Column(Integer, ForeignKey('comment.id'),
                     primary_key=True, nullable=False)
    username = Column(String(24), ForeignKey('user.username'),
                      nullable=False, primary_key=True)
    user = relationship('User')
    rated = Column(Boolean, default=False)
    comment = relationship('Comment')

    @property
    def serialize_response(self):
        """Return object data as response to the client"""
        return {
            'username': self.username,
            'rated': self.rated,
        }

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'item_id': self.item_id,
            'username': self.username,
            'user': str(self.user),
            'rated': self.rated,
            'comment': str(self.comment),
        }


class ReplyRating(Base):
    __tablename__ = 'reply_rating'
    item_id = Column(Integer, ForeignKey('reply.id'),
                     primary_key=True, nullable=False)
    username = Column(String(24), ForeignKey('user.username'),
                      nullable=False, primary_key=True)
    user = relationship('User')
    rated = Column(Boolean, default=False)
    reply = relationship('Reply')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'item_id': self.item_id,
            'username': self.username,
            'user': str(self.user),
            'rated': self.rated,
            'reply': str(self.reply),
        }
