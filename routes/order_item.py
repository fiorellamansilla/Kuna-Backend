from flask import Blueprint
from controllers.order_item import create, index, get_by_id, update_by_id, delete_by_id

order_item_bp = Blueprint('order_item_bp', __name__)

order_item_bp.route('/', methods=['GET'])(index)
order_item_bp.route('/create', methods=['POST'])(create)
order_item_bp.route('/<order_item_id>', methods=['GET'])(get_by_id)
order_item_bp.route('/<order_item_id>', methods=['PUT'])(update_by_id)
order_item_bp.route('/<order_item_id>', methods=['DELETE'])(delete_by_id)