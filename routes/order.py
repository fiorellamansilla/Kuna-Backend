from flask import Blueprint
from controllers.order import create, index, get_by_id, update_by_id, delete_by_id

order_bp = Blueprint('order_bp', __name__)

order_bp.route('/', methods=['GET'])(index)
order_bp.route('/create', methods=['POST'])(create)
order_bp.route('/<order_id>', methods=['GET'])(get_by_id)
order_bp.route('/<order_id>', methods=['PUT'])(update_by_id)
order_bp.route('/<order_id>', methods=['DELETE'])(delete_by_id)