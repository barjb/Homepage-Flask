from flask import Blueprint
from app.posts.service import get_all, create, get_id, put_id, delete_id, patch_id, get_tag
from app.posts.service import del_phantom, tags, phantoms


bp = Blueprint('posts', __name__, url_prefix='/posts')

bp.route('/', methods=['GET'])(get_all)
bp.route('/', methods=['POST'])(create)

bp.route('/<int:id>', methods=['GET'])(get_id)
bp.route('/<int:id>', methods=['PUT'])(put_id)
bp.route('/<int:id>', methods=['DELETE'])(delete_id)
bp.route('/<int:id>', methods=['PATCH'])(patch_id)

bp.route('/<string:tag>', methods=['GET'])(get_tag)

bp.route('/tags', methods=['GET'])(tags)
bp.route('/deletephantom', methods=['GET'])(del_phantom)
bp.route('/phantoms', methods=['GET'])(phantoms)
