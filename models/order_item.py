from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from models.client import db

class OrderItem(db.Model):
    __tablename__ = "order_item"
    order_item_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    order_id = db.Column (db.Integer, db.ForeignKey ("orders.order_id", ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    item_id = db.Column (db.Integer, db.ForeignKey ("item.item_id", ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    quantity_ordered = db.Column (db.Integer, nullable = False, server_default="0")
    total_amount = db.Column (db.Float, nullable = False, server_default="0")

    # Many to Many relationship between Order and Item
    orders = db.relationship ('Order', backref='items')

    # Many to Many relationship between Item and Order
    items = db.relationship ('Item', backref='orders')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, order_id, item_id, quantity_ordered, total_amount): 

        self.order_id = order_id
        self.item_id = item_id
        self.quantity_ordered = quantity_ordered
        self.total_amount = total_amount
 
    def __repr__(self):
        return '' % self.order_item_id

db.create_all

