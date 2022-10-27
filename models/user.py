from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True )
    password_hash = db.Column (db.String(64), nullable=False)
    email = db.Column (db.String(64), nullable=False)
    country = db.Column (db.String(32), nullable=False)
    is_blocked = db.Column(db.Boolean, nullable=False)
    is_approved = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone = True), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, username, password_hash, email, country, is_blocked, is_approved, creation_date):
        self.username = username
        self.country = country
        self.email = email
        self.password_hash = password_hash
        self.is_blocked = is_blocked
        self.is_approved = is_approved
        self.creation_date = creation_date

    def __repr__(self):
        return '' % self.id_client

db.create_all

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = User
        load_instance = True
        sqla_session = db.session
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password_hash = fields.String(required=True)
    email = fields.String(required=True)
    country = fields.String(required=True)
    is_blocked = fields.Boolean(required=True)
    is_approved = fields.Boolean(required=True)
    created_at = fields.DateTime(required=True)
