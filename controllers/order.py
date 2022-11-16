from flask_sqlalchemy  import SQLAlchemy
from models.order import Order
from schemas.order_schema import OrderSchema
from entities.order import Order as OrderEntity 
from flask import make_response, jsonify, request
import json 

db = SQLAlchemy()

# GET Method / READ all orders
def index():
    get_orders = Order.query.all()
    order_schema = OrderSchema(many=True)
    orders = order_schema.dump(get_orders)
    order_entities = []

    for order in orders:
        print(order)
        order_entity = OrderEntity(order)
        order_entities.append(order_entity)     

    return make_response(jsonify({"order": [i.toJSON() for i in order_entities]}))

# GET Method / READ one order by ID
def get_by_id(order_id):
    get_order = Order.query.get(order_id)
    order_schema = OrderSchema()
    order = order_schema.dump(get_order)
    order_entity = OrderEntity(order)
    return make_response(jsonify({"order": order_entity.toJSON()}))

# PUT Method / UPDATE
def update_by_id(order_id):
    data = request.get_json()
    get_order = Order.query.get(order_id)

    if data.get('order_amount'):
        get_order.order_amount = data['order_amount']
    if data.get('client_id'):
        get_order.client_id = data['client_id']
    if data.get('ship_name'):
        get_order.ship_name = data['ship_name']
    if data.get('ship_adress'):
        get_order.ship_adress = data['ship_adress']
    if data.get('order_city'):
        get_order.order_city = data['order_city']
    if data.get('order_zip'):
        get_order.order_zip = data['order_zip']
    if data.get('order_country'):
        get_order.order_country= data['order_country'] 
    if data.get('order_phone'):
        get_order.order_phone= data['order_phone']
    if data.get('order_email'):
        get_order.order_email= data['order_email'] 
    if data.get('ordered_at'):
        get_order.ordered_at= data['ordered_at']  
    if data.get('shipped_at'):
        get_order.shipped_at= data['shipped_at']
    if data.get('tracking_number'):
        get_order.tracking_number= data['tracking_number']

    db.session.add(get_order)
    db.session.commit()
    order_schema = OrderSchema(only=['order_amount','client_id','ship_name','ship_adress', 'order_city', 'order_zip', 'order_country', 'order_phone', 'order_email', 'ordered_at','shipped_at', 'tracking_number'])
    order = order_schema.dump(get_order)
    return make_response(jsonify({"order": order}))

# POST Method / CREATE
def create():
    data = request.get_json()
    order_schema = OrderSchema()
    order = order_schema.load(data)
    result = order_schema.dump(order.create())
    return make_response(jsonify({"order": result}),200)

# DELETE Method / DELETE
def delete_by_id(order_id):
    get_order = Order.query.get(order_id)
    db.session.delete(get_order)
    db.session.commit()
    return make_response("",204)