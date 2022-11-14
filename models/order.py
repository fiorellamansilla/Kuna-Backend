from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import backref
from models.client import db
from models.item import Item
from models.order_item import order_item

class Order(db.Model):
    __tablename__ = "orders"
    order_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    order_amount = db.Column (db.Float, nullable=False, server_default="0")
    ship_name = db.Column(db.String(128), nullable=False)
    ship_address = db.Column (db.String(2024), nullable=False)
    order_city = db.Column (db.String(32), nullable=False )
    order_zip = db.Column (db.String(64), nullable=False )
    order_country = db.Column (db.String(32), nullable=False )
    order_phone = db.Column (db.String(32), nullable=False )
    order_email = db.Column (db.String(64), nullable=False )
    ordered_at = db.Column(db.DateTime(timezone = True), nullable=False, server_default=func.now())
    shipped_at = db.Column(db.DateTime(timezone = True), nullable=False,server_default=func.now() )
    tracking_number = db.Column (db.String(64), nullable=False )

    # One to Many relationship between Order and Client
    client_id = db.Column (db.Integer, db.ForeignKey("client.client_id", ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    client = db.relationship ('Client', backref ='orders')

    # Many to Many relationship between Order and Item
    items = db.relationship ('Item', secondary = order_item, back_populates="orders")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, client_id, order_amount, ship_name, ship_address,  order_city, order_zip, order_country, order_phone, order_email, ordered_at, shipped_at,  tracking_number): 
    
        self.client_id = client_id
        self.order_amount = order_amount
        self.ship_name = ship_name
        self.ship_address = ship_address
        self.order_city = order_city
        self.order_zip = order_zip
        self.order_country = order_country
        self.order_phone = order_phone
        self.order_email = order_email
        self.ordered_at = ordered_at
        self.shipped_at = shipped_at
        self.tracking_number = tracking_number

    def __repr__(self):
        return '' % self.order_id

db.create_all