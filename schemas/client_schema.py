
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.client import Client, db

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
    