from flask import (
    Blueprint,
    request,
    jsonify
)

from flask_login import (
    UserMixin,
)

from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf.csrf import generate_csrf

from mgflask.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


class User(UserMixin):
    ...


"""
@bp.route("/getcsrf", methods=["GET"])
def get_csrf():
    token = generate_csrf()
    response = jsonify({"detail": "CSRF cookie set"})
    response.headers.set("X-CSRFToken", token)
    return response
"""


def get_user(id):
    db = get_db()
    if(isinstance(id, int)):
        user = db.execute(
            'SELECT username FROM user WHERE id = ?', (id)).fetchone()
    if(isinstance(id, str)):
        user = db.execute(
            'SELECT id FROM user WHERE username = ?', (id,)).fetchone()
    return user


def user_loader(id):
    user = get_user(id)
    if user:
        user_model = User()
        user_model.id = user["id"]
        return user_model
    return None


@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {
        "insert_status": "success",
        "msg": "registration successful",
    }

    if request.method == 'POST':
        if not request.get_json() or not request.get_json()['username'] or not request.get_json()['password']:
            response_object['msg'] = 'Missing username or password'
            return jsonify(response_object)
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']

        db = get_db()
        error = False
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

        if not error:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()

    return jsonify(response_object)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    response_object = {
        "status": "success",
        "auth": "fail"
    }

    if request.method == 'POST':
        if not request.get_json() or not request.get_json()['username'] or not request.get_json()['password']:
            response_object['msg'] = 'Missing username or password'
            return jsonify(response_object)
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']

        db = get_db()
        error = False
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            response_object['msg'] = 'Incorrect username.'
            error = True
        elif not check_password_hash(user['password'], password):
            response_object['msg'] = 'Incorrect password.'
            error = True

        # proper auth
        if not error:
            response_object['msg'] = "Login Successful"
            response_object['auth'] = "success"
            response_object['token'] = generate_csrf()

    return jsonify(response_object)


