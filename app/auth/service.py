from flask import session, request, g
from werkzeug.security import check_password_hash
from app.extensions import db
from app.models.user import User
import functools


def root():
    if 'user_id' in session:
        return f'Loggged in as {session["user_id"]}'
    return f'Not Loggged in'


def login():
    login = request.json['login']
    password = request.json['password']

    user = db.session.execute(
        db.select(User).where(User.login == login)).scalar()
    if user is None:
        return 'user does not exist'
    if check_password_hash(user.password, password):
        session.clear()
        session['user_id'] = user.id
        return 'ok'
    else:
        return 'passwords do not match'


def logout():
    session.pop('user_id', None)
    return 'ok'


def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = db.session.execute(
            db.select(User).where(User.id == user_id)).scalar()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return 'denied', 400
        return view(**kwargs)
    return wrapped_view
