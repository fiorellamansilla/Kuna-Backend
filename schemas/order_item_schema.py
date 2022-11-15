from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.order_item import OrderItem, db

class OrderItemSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = OrderItem
        include_fk = True
        load_instance = True
        sqla_session = db.session
    order_item_id = fields.Integer(dump_only=True)
    order_id = fields.Integer(required=True)
    item_id = fields.Integer(required=True)
    quantity_ordered = fields.Integer(required=True)
    total_amount = fields.Float(required=True)