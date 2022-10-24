from flask import Blueprint
from controllers.client import create, index, get_by_id, update_by_id, delete_by_id

client_bp = Blueprint('client_bp', __name__)

client_bp.route('/', methods=['GET'])(index)
client_bp.route('/create', methods=['POST'])(create)
client_bp.route('/<client_id>', methods=['GET'])(get_by_id)
client_bp.route('/<client_id>', methods=['PUT'])(update_by_id)
client_bp.route('/<client_id>', methods=['DELETE'])(delete_by_id)
