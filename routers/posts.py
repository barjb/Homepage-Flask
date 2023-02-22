from flask import Blueprint
from ..controllers.posts import all, byid, bytag


bp = Blueprint('posts', __name__, url_prefix='/posts')

bp.route('/', methods=['GET', 'POST'])(all)
bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])(byid)
bp.route('/<string:tag>', methods=['GET'])(bytag)
