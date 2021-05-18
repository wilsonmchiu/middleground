from flask import (
    Blueprint,
    request,
    jsonify
)

from mgflask.db import db_session
from mgflask.models import Article, Comment, User
from datetime import datetime

bp = Blueprint('comments', __name__, url_prefix='/comments')



@bp.route('/post', methods=['POST'])
def post_comment():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False

    try:
        post_data = request.get_json()
        username = post_data['username']
        articleID = post_data['articleID']
        userComment = post_data['userComment']
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        article = db_session.query(Article).filter_by(id=articleID).one()
        user = db_session.query(User).filter_by(username=username).one()
        newComment = Comment(username=username, user=user, content=userComment, article=article, 
            article_id=articleID, date=datetime.now())
        db_session.add(newComment)
        db_session.commit()

    return jsonify(response_object)

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
        comment = db_session.query(Comment).filter_by(id=commentID).one()
        if not comment:
            raise ValueError(f"comment id {commentID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        print("deleting comment", commentID)
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
    print("in edit")
    try:
        data = request.get_json()
        commentID = data['commentID']
        content = data['content']
        comment = db_session.query(Comment).filter_by(id=commentID).one()
        if not comment:
            raise ValueError(f"comment id {commentID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        print("updating comment", commentID, "content: ",content)
        comment.content = content
        comment.date= datetime.now()
        db_session.commit()

    return jsonify(response_object)
