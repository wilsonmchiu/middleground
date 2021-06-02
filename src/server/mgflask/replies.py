from flask import (
    Blueprint,
    request,
    jsonify
)

from mgflask.db import db_session
from mgflask.models import Comment, Reply, User
from datetime import datetime

bp = Blueprint('replies', __name__, url_prefix='/replies')

@bp.route('/get', methods=['GET'])
def get_replies():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False
    params = request.args
    replies = []
    try:
        commentID = params.get('commentID')
        comment = db_session.query(Comment).filter_by(id=commentID).one()
        if not comment:
            raise ValueError(f"comment id {commentID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        replies = [reply.serialize_response for reply in comment.replies]
        
    return jsonify({"status": response_object, "replies": replies})

@bp.route('/post', methods=['POST'])
def post_reply():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False
    newReply = []

    try:
        post_data = request.get_json()
        username = post_data['username']
        commentID = post_data['commentID']
        userReply = post_data['userReply']
        comment = db_session.query(Comment).filter_by(id=commentID).one_or_none()
        if not comment:
            raise ValueError(f"replyID {commentID} does not exist in the database")
        user = db_session.query(User).filter_by(username=username).one_or_none()
        if not user:
            raise ValueError(f"username {username} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        reply = Reply(username=username, user=user, content=userReply, comment=comment, 
            comment_id=commentID, date=datetime.now())
        db_session.add(reply)
        db_session.commit()
        newReply = reply.serialize_response

    return jsonify({"status": response_object, "newReply": newReply})

@bp.route('/delete', methods=['PUT'])
def delete_comment():
    response_object = {
        "status": "success", 
        "msg": "comment successful",
    }
    error = False

    try:
        data = request.get_json()
        replyID = data['replyID']
        reply = db_session.query(Reply).filter_by(id=replyID).one_or_none()
        if not reply:
            raise ValueError(f"replyID {replyID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        db_session.delete(reply)
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
        replyID = data['replyID']
        content = data['content']
        reply = db_session.query(Reply).filter_by(id=replyID).one_or_none()
        if not reply:
            raise ValueError(f"replyID {replyID} does not exist in the database")
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        reply.content = content
        reply.date= datetime.now()
        db_session.commit()

    return jsonify(response_object)
