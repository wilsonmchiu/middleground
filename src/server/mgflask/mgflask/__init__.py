from . import news
from . import db
from . import newsapi
import os

from flask import Flask
from flask_cors import CORS


# configuration
DEBUG = True
cors = CORS()


from . import auth  # noqa: E731


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mgflask.sqlite'),
        SESSION_COOKIE_HTTPONLY=True,
        REMEMBER_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    cors.init_app(app, resources={r'/*': {'origins': '*'}},
                  expose_headers=["Content-Type", "X-CSRFToken"],
                  supports_credentials=True)

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
    app.register_blueprint(news.bp)

    return app
