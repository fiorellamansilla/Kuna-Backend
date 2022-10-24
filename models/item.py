from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from datetime import datetime
from sqlalchemy.sql import func


db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    name_item = db.Column(db.String(128), nullable=False, unique=True )
    desc_item = db.Column (db.String(2024), nullable=False)
    size = db.Column (db.String(64), nullable=False)
    color = db.Column (db.String(64), nullable=False )
    price = db.Column (db.Float, nullable=False, server_default="0")
    discount = db.Column (db.Float, nullable=False, server_default="0")
    SKU = db.Column (db.String(128), nullable=False)
    quantity_stock = db.Column (db.Integer, nullable=False, server_default="0")
    image_path = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), nullable=False, server_default=func.now())
    modified_at = db.Column(db.DateTime(timezone = True), nullable=False, onupdate=func.now())
    deleted_at = db.Column(db.DateTime(timezone = True), nullable=False, server_default=func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self,name_item,desc_item,size,color,price,discount,SKU,quantity_stock,image_path, created_at, modified_at, deleted_at):
        self.name_item = name_item
        self.desc_item = desc_item
        self.size = size
        self.color = color
        self.price = price
        self.discount = discount
        self.SKU = SKU
        self.quantity_stock = quantity_stock
        self.image_path = image_path
        self.created_at = created_at
        self.modified_at = modified_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return '' % self.item_id

db.create_all

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
    