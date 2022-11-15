from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import backref
from models.client import db

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

    # Many to Many relationship between Item and Order
    # orders = db.relationship ('Order', secondary = order_item, back_populates="items")


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
