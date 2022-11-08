from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.order import Order, db

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Order
        include_fk = True
        load_instance = True
        sqla_session = db.session
    order_id = fields.Integer(dump_only=True)
    client_id = fields.Integer(required=True)
    order_amount = fields.Float(required=True)
    ship_name = fields.String(required=True)
    ship_address = fields.String(required=True)
    order_city = fields.String(required=True)
    order_zip = fields.String(required=True)
    order_country = fields.String(required=True)
    order_phone = fields.String(required=True)
    order_email = fields.String(required=True)
    ordered_at = fields.DateTime(required=True)
    shipped_at = fields.DateTime(required=True)
    tracking_number = fields.String(required=True)