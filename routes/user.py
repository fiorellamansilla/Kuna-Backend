from flask import Blueprint
from controllers.user import create, index, get_by_id, update_by_id, delete_by_id

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(create)
user_bp.route('/<item_id>', methods=['GET'])(get_by_id)
user_bp.route('/<item_id>', methods=['PUT'])(update_by_id)
user_bp.route('/<item_id>', methods=['DELETE'])(delete_by_id)
