from flask import (
    Blueprint,
    request,
    jsonify,
    current_app
)

from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from uuid import uuid4


from mgflask.db import db_session
from mgflask.models import User
from functools import wraps

import jwt
import datetime


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/test_users', methods=('GET', 'POST'))
def test_users():
    users = db_session.query(User).all()
    return jsonify(users=[(c.username, c.password) for c in users])


def get_user(id):
    try:
        if(isinstance(id, int)):
            user = db_session.query(User).filter_by(id=id).one()
        if(isinstance(id, str)):
            user = db_session.query(User).filter_by(username=id).one()
        return user
    except:
        return None


@bp.route('/register', methods=['POST'])
def register():
    response_object = {
        "insert_status": "success",
        "msg": "registration successful",
    }

    error = False

    try:
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']

        user_found = get_user(username)
        if not username:
            response_object['insert_status'] = "fail"
            response_object['msg'] = "Username is required"
            error = True
        elif not password:
            response_object['insert_status'] = "fail"
            response_object['msg'] = 'Password is required.'
            error = True
        elif user_found is not None:
            response_object['insert_status'] = "fail"
            response_object['msg'] = "User already registered"
            error = True
    except Exception as e:
        response_object['msg'] = "Registration Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        newUser = User(username=username,
                       password=generate_password_hash(password),
                       )
        db_session.add(newUser)
        db_session.commit()
        return jsonify(response_object), 201

    return jsonify(response_object), 401


@bp.route('/login', methods=['POST'])
def login():
    response_object = {
        "status": "success",
        "auth": "fail"
    }

    error = False

    try:
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        user = get_user(username)
        if user is None:
            response_object['msg'] = 'Incorrect username.'
            error = True
        elif not check_password_hash(user.password, password):
            response_object['msg'] = 'Incorrect password.'
            error = True
    except Exception as e:
        response_object['msg'] = "Login Unsuccessful. Check Exceptions."
        response_object['exception'] = str(e)
        error = True

    if not error:
        response_object['msg'] = "Login Successful"
        token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
        response_object['token'] = token
        return jsonify(response_object), 201

    return jsonify(response_object), 401