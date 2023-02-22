from .routers import posts
from flask import Flask, url_for

app = Flask(__name__)


app.register_blueprint(posts.bp)


@app.route('/')
def site_map():
    routes = []
    print(app.url_map)
    iter = app.url_map.iter_rules()
    for rule in iter:
        routes.append({'url': str(rule), 'methods': str(
            rule.methods), 'endpoint': rule.endpoint})
    return routes
