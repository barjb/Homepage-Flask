import os
from flask import Flask
from app.extensions import db
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

from config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)
    app.config.from_mapping(
        SECRET_KEY=Config.APP_SECRET_KEY,
        DATABASE=os.path.join(app.instance_path)
    )
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

    jwt = JWTManager(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.posts.api import bp as post_bp
    app.register_blueprint(post_bp)
    from app.auth.api import bp as auth_bp
    app.register_blueprint(auth_bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.POSTGRES_URL
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
