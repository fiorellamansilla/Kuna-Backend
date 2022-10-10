from models.client import *
from app import *

# GET Method / READ all clients

@app.route('/clients', methods = ['GET'])
def index_clients():
    get_clients = Client.query.all()
    client_schema = ClientSchema(many=True)
    clients = client_schema.dump(get_clients)
    return make_response(jsonify({"client": clients}))

# GET Method / READ one client by ID

@app.route('/clients/<id_client>', methods = ['GET'])
def get_client_by_id(id_client):
    get_client = Client.query.get(id_client)
    client_schema = ClientSchema()
    client = client_schema.dump(get_client)
    return make_response(jsonify({"client": client}))

# PUT Method / UPDATE

@app.route('/clients/<id_client>', methods = ['PUT'])
def update_client_by_id(id_client):
    data = request.get_json()
    get_client = Client.query.get(id_client)

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

    db.session.add(get_client)
    db.session.commit()
    client_schema = ClientSchema(only=['id_client', 'first_name', 'last_name', 'address_client', 'zip_code', 'city', 'country', 'phone', 'email'])
    client = client_schema.dump(get_client)
    return make_response(jsonify({"client": client}))

# POST Method / CREATE

@app.route('/clients', methods = ['POST'])
def create_client():
    data = request.get_json()
    client_schema = ClientSchema()
    client = client_schema.load(data)
    result = client_schema.dump(client.create())
    return make_response(jsonify({"client": result}),200)

# DELETE Method / DELETE

@app.route('/clients/<id_client>', methods = ['DELETE'])
def delete_client_by_id(id_client):
    get_client = Client.query.get(id_client)
    db.session.delete(get_client)
    db.session.commit()
    return make_response("",204)

if __name__ == "__main__":
    app.run(debug=True)