from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from datetime import datetime
from sqlalchemy.sql import func


db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = "client"
    client_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True )
    password_client = db.Column (db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False, unique=True )
    last_name = db.Column (db.String(64), nullable=False)
    address_client = db.Column (db.String(128), nullable=False)
    zip_code = db.Column (db.String(64), nullable=False)
    city = db.Column (db.String(32), nullable=False)
    country = db.Column (db.String(32), nullable=False)
    phone = db.Column (db.String(32), nullable=False)
    email = db.Column (db.String(64), nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), nullable=False, server_default=func.now())
    modified_at = db.Column(db.DateTime(timezone = True), nullable=False, onupdate=func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, username, password_client, first_name, last_name, address_client, zip_code, city, country, phone, email, created_at, modified_at):
        self.username = username
        self.password_client = password_client
        self.first_name = first_name
        self.last_name = last_name
        self.address_client = address_client
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.created_at = created_at
        self.modified_at = modified_at

    def __repr__(self):
        return '' % self.client_id

db.create_all

class ClientSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Client
        load_instance = True
        sqla_session = db.session
    client_id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    password_client = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    address_client = fields.String(required=True)
    zip_code = fields.String(required=True)
    city = fields.String(required=True)
    country = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    