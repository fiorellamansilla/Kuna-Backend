from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
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

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, username, password_client, first_name, last_name, address_client, zip_code, city, country, phone, email):
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

    def __repr__(self):
        return '' % self.id_client