from flask import (
    Blueprint,
    request,
    jsonify
)

from mgflask.db import db_session
from mgflask.models import Article, Comment, User
from datetime import datetime

bp = Blueprint('comments', __name__, url_prefix='/comments')

@bp.route('/get', methods=['GET'])
def get_comments():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False
    params = request.args
    comments = []
    try:
        articleID = params.get('articleID')
        article = db_session.query(Article).filter_by(id=articleID).one()
        if not article:
            raise ValueError(f"article id {articleID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        comments = [comment.serialize_response for comment in article.comments]
        
    return jsonify({"status": response_object, "comments": comments})

        
@bp.route('/post', methods=['POST'])
def post_comment():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False
    newComment = []

    try:
        post_data = request.get_json()
        username = post_data['username']
        articleID = post_data['articleID']
        userComment = post_data['userComment']
        article = db_session.query(Article).filter_by(id=articleID).one_or_none()
        if not article:
            raise ValueError(f"article id {articleID} does not exist in the database")
        user = db_session.query(User).filter_by(username=username).one_or_none()
        if not user:
            raise ValueError(f"username {username} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        comment = Comment(username=username, user=user, content=userComment, article=article, 
            article_id=articleID, date=datetime.now())
        db_session.add(comment)
        db_session.commit()
        newComment = comment.serialize_response
    
    return jsonify({"status": response_object, "newComment": newComment})

@bp.route('/delete', methods=['PUT'])
def delete_comment():
    response_object = {
        "status": "success", 
        "msg": "comment successful",
    }
    error = False

    try:
        data = request.get_json()
        commentID = data['commentID']
        comment = db_session.query(Comment).filter_by(id=commentID).one_or_none()
        if not comment:
            raise ValueError(f"comment id {commentID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        db_session.delete(comment)
        db_session.commit()

    return jsonify(response_object)

@bp.route('/edit', methods=['PUT'])
def edit_comment():
    response_object = {
        "status": "success",
        "msg": "comment successful",
    }

    error = False
    try:
        data = request.get_json()
        commentID = data['commentID']
        content = data['content']
        comment = db_session.query(Comment).filter_by(id=commentID).one_or_none()
        if not comment:
            raise ValueError(f"comment id {commentID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        comment.content = content
        comment.date= datetime.now()
        db_session.commit()

    return jsonify(response_object)
