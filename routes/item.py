from flask import Blueprint
from controllers.item import create, index, get_by_id, update_by_id, delete_by_id

item_bp = Blueprint('item_bp', __name__)

item_bp.route('/', methods=['GET'])(index)
item_bp.route('/create', methods=['POST'])(create)
item_bp.route('/<item_id>', methods=['GET'])(get_by_id)
item_bp.route('/<item_id>', methods=['PUT'])(update_by_id)
item_bp.route('/<item_id>', methods=['DELETE'])(delete_by_id)
