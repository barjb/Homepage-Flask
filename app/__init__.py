import os
from flask import Flask
from app.extensions import db
from config import Config
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path)
    )
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

    @app.route('/')
    def site_map():
        routes = []
        print(app.url_map)
        iter = app.url_map.iter_rules()
        for rule in iter:
            routes.append({'url': str(rule), 'methods': str(
                rule.methods), 'endpoint': rule.endpoint})
        return routes

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.POSTGRES_URL
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
