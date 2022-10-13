from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    name_item = db.Column(db.String(128), nullable=False, unique=True )
    desc_item = db.Column (db.String(2024), nullable=False)
    size = db.Column (db.String(64), nullable=False)
    price = db.Column (db.Float, nullable=False, server_default="0")
    discount = db.Column (db.Float, nullable=False, server_default="0")
    SKU = db.Column (db.String(128), nullable=False)
    quantity_stock = db.Column (db.Integer, nullable=False, server_default="0")
    images = db.Column(db.String(256), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self,name_item,desc_item,size,price,discount,SKU,quantity_stock,images):
        self.name_item = name_item
        self.desc_item = desc_item
        self.size = size
        self.price = price
        self.discount = discount
        self.SKU = SKU
        self.quantity_stock = quantity_stock
        self.images = images

    def __repr__(self):
        return '' % self.item_id

db.create_all

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Item
        load_instance = True
        sqla_session = db.session
    item_id = fields.Number(dump_only=True)
    name_item = fields.String(required=True)
    desc_item = fields.String(required=True)
    size = fields.String(required=True)
    price = fields.Number(required=True)
    discount = fields.Number(required=True)
    SKU = fields.String(required=True)
    quantity_stock = fields.Number(required=True)
    images = fields.String(required=True)
    