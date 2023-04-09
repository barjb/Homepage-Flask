from flask import Blueprint
from app.auth.service import login, refresh
bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.route('/login', methods=['POST'])(login)
bp.route('/refresh', methods=['GET'])(refresh)
