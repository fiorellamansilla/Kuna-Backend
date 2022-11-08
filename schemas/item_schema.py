from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.item import Item, db

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Item
        load_instance = True
        sqla_session = db.session
    item_id = fields.Integer(dump_only=True)
    name_item = fields.String(required=True)
    desc_item = fields.String(required=True)
    size = fields.String(required=True)
    color = fields.String(required=True)
    price = fields.Number(required=True)
    discount = fields.Integer(required=True)
    SKU = fields.String(required=True)
    quantity_stock = fields.Integer(required=True)
    image_path = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    modified_at = fields.DateTime(required=True)
    deleted_at = fields.DateTime(required=True)
    