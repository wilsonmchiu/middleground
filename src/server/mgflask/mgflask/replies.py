from flask import (
    Blueprint,
    request,
    jsonify
)

from mgflask.db import db_session
from mgflask.models import Comment, Reply, User
from datetime import datetime

bp = Blueprint('replies', __name__, url_prefix='/replies')


@bp.route('/post_reply', methods=['POST'])
def post_reply():
    response_object = {
        "insert_status": "success",
        "msg": "comment successful",
    }

    error = False

    try:
        post_data = request.get_json()
        username = post_data['username']
        commentID = post_data['commentID']
        userReply = post_data['userReply']
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        comment = db_session.query(Comment).filter_by(id=commentID).one()
        user = db_session.query(User).filter_by(username=username).one()
        newReply = Reply(username=username, user=user, content=userReply, comment=comment, 
            comment_id=commentID, date=datetime.now())
        db_session.add(newReply)
        db_session.commit()

    return jsonify(response_object)
