from flask import Blueprint
from app.auth.service import login, logout, root, load_logged_in_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.route('/', methods=['GET'])(root)
bp.route('/login', methods=['POST'])(login)
bp.route('/logout', methods=['GET'])(logout)

bp.before_app_request(load_logged_in_user)
