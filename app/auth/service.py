from flask import request
from werkzeug.security import check_password_hash
from app.extensions import db
from app.models.user import User

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify


def login():
    login = request.json['login']
    password = request.json['password']

    user = db.session.execute(
        db.select(User).where(User.login == login)).scalar()
    if user is None:
        return jsonify({"msg": 'user does not exist'}), 401

    if check_password_hash(user.password, password):
        access_token = create_access_token(identity=login, fresh=True)
        refresh_token = create_refresh_token(identity=login)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"msg": 'passwords do not match'}), 401


@jwt_required(refresh=True)
def refresh():
    current = get_jwt_identity()
    access_token = create_access_token(identity=current, fresh=False)
    return jsonify(access_token=access_token)
