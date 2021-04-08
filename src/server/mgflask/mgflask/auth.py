

from flask import (
    Blueprint,
    request,
    session,
    jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from mgflask.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {
        "insert_status": "success",
        "msg": "registration successful",
    }

    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        username = post_data['name']
        password = post_data['password']

        db = get_db()
        error = False
        user_found = db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)).fetchone()

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

        print(error)
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
        post_data = request.get_json()
        username = post_data['name']
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
            session.clear()
            session['user_id'] = user['id']
            response_object['msg'] = "Login Successful"
            response_object['auth'] = "success"

    return jsonify(response_object)
