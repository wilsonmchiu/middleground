import os

from flask import Flask
from flask_cors import CORS

from . import auth

# database
from . import db


# configuration
DEBUG = True
cors = CORS()

# app init


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mgflask.sqlite')
    )

    cors.init_app(app, resources={r'/*': {'origins': '*'}})

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # REGISTER IN FACTORY
    # --------------------
    app.register_blueprint(auth.bp)

    return app
