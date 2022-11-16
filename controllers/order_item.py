from flask_sqlalchemy  import SQLAlchemy
from models.order_item import OrderItem
from schemas.order_item_schema import OrderItemSchema
from entities.order_item import OrderItemEntity
from flask import make_response, jsonify, request
import json 

db = SQLAlchemy()

# GET Method / READ all orders
def index():
    get_order_items = OrderItem.query.all()
    order_item_schema = OrderItemSchema(many=True)
    order_items = order_item_schema.dump(get_order_items)
    order_item_entities = []

    for order_item in order_items:
        print(order_item)
        order_item_entity = OrderItemEntity(order_item)
        order_item_entities.append(order_item_entity)     

    return make_response(jsonify({"order_item": [i.toJSON() for i in order_item_entities]}))

# GET Method / READ one order by ID
def get_by_id(order_item_id):
    get_order_item = OrderItem.query.get(order_item_id)
    order_item_schema = OrderItemSchema()
    order_item = order_item_schema.dump(get_order_item)
    order_item_entity = OrderItemEntity(order_item)
    return make_response(jsonify({"order_item": order_item_entity.toJSON()}))

# PUT Method / UPDATE
def update_by_id(order_item_id):
    data = request.get_json()
    get_order_item = OrderItem.query.get(order_item_id)

    if data.get('order_id'):
        get_order_item.order_id = data['order_id']
    if data.get('item_id'):
        get_order_item.item_id = data['item_id']
    if data.get('quantity_ordered'):
        get_order_item.quantity_ordered = data['quantity_ordered']
    if data.get('total_amount'):
        get_order_item.total_amount = data['total_amount']


    db.session.add(get_order_item)
    db.session.commit()
    order_item_schema = OrderItemSchema(only=['order_id','item_id','quantity_ordered','total_amount'])
    order_item = order_item_schema.dump(get_order_item)
    return make_response(jsonify({"order_item": order_item}))