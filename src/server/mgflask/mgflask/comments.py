from flask import (
    Blueprint,
    request,
    jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from uuid import uuid4

from mgflask.db import db_session
from mgflask.models import Article, Comment, User
from datetime import datetime

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/post_comment', methods=['POST'])
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
