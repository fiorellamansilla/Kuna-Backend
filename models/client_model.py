from app import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Client(db.Model):
    __tablename__ = "clients"
    id_client = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False, unique=True )
    last_name = db.Column (db.String(64), nullable=False)
    address_client = db.Column (db.String(128), nullable=False)
    zip_code = db.Column (db.String(64), nullable=False)
    city = db.Column (db.String(32), nullable=False)
    country = db.Column (db.String(32), nullable=False)
    phone = db.Column (db.String(32), nullable=False)
    email = db.Column (db.String(64), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, first_name, last_name, address_client, zip_code, city, country, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address_client = address_client
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email

    def __repr__(self):
        return '' % self.id_client

db.create_all

class ClientSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Client
        load_instance = True
        sqla_session = db.session
    id_client = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    address_client = fields.String(required=True)
    zip_code = fields.String(required=True)
    city = fields.String(required=True)
    country = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    