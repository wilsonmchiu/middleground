from flask import (
    Blueprint,
    request,
    jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from uuid import uuid4

from mgflask.db import db_session
from mgflask.models import User

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
        userComment = post_data['userComment']
        loggedIn = post_data['isLoggedIn']
        password = "password"
        if not loggedIn:
            response_object['insert_status'] = "fail"
            response_object['msg'] = 'login required.'
            error = True
    except Exception as e:
        response_object['msg'] = "Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        newComment = User(username=userComment,
                       password=generate_password_hash(password))
        db_session.add(newComment)
        db_session.commit()

    return jsonify(response_object)
