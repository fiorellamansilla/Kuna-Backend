from flask_sqlalchemy  import SQLAlchemy
from models.client import Client, ClientSchema
from entities.client import Client as ClientEntity 
from flask import make_response, jsonify, request
import json 

db = SQLAlchemy()

# GET Method / READ all clients
def index():
    get_clients = Client.query.all()
    client_schema = ClientSchema(many=True)
    clients = client_schema.dump(get_clients)
    client_entities = []

    for client in clients:
        print(client)
        client_entity = ClientEntity(client)
        client_entities.append(client_entity)     

    return make_response(jsonify({"client": [i.toJSON() for i in client_entities]}))

# GET Method / READ one client by ID
def get_by_id(client_id):
    get_client = Client.query.get(client_id)
    client_schema = ClientSchema()
    client = client_schema.dump(get_client)
    client_entity = ClientEntity(client)
    return make_response(jsonify({"client": client_entity.toJSON()}))

# PUT Method / UPDATE
def update_by_id(client_id):
    data = request.get_json()
    get_client = Client.query.get(client_id)

    if data.get('username'):
        get_client.username = data['username']
    if data.get('password_client'):
        get_client.password_client = data['password_client']
    if data.get('first_name'):
        get_client.first_name = data['first_name']
    if data.get('last_name'):
        get_client.last_name = data['last_name']
    if data.get('address_client'):
        get_client.address_client = data['address_client']
    if data.get('zip_code'):
        get_client.zip_code = data['zip_code']
    if data.get('city'):
        get_client.city= data['city'] 
    if data.get('country'):
        get_client.country= data['country']
    if data.get('phone'):
        get_client.phone= data['phone'] 
    if data.get('email'):
        get_client.email= data['email']
    if data.get('created_at'):
        get_client.created_at= data['created_at']  
    if data.get('modified_at'):
        get_client.modified_at= data['modified_at']

    db.session.add(get_client)
    db.session.commit()
    client_schema = ClientSchema(only=['client_id','username','password_client','first_name', 'last_name', 'address_client', 'zip_code', 'city', 'country', 'phone', 'email', 'created_at','modified_at'])
    client = client_schema.dump(get_client)
    return make_response(jsonify({"client": client}))

# POST Method / CREATE
def create():
    data = request.get_json()
    client_schema = ClientSchema()
    client = client_schema.load(data)
    result = client_schema.dump(client.create())
    return make_response(jsonify({"client": result}),200)

# DELETE Method / DELETE
def delete_by_id(client_id):
    get_client = Client.query.get(client_id)
    db.session.delete(get_client)
    db.session.commit()
    return make_response("",204)
