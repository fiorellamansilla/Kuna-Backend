from flask_sqlalchemy  import SQLAlchemy
from models.item import Item
from schemas.item_schema import ItemSchema
from entities.item import Item as ItemEntity
from flask import make_response, jsonify, request
import json


db = SQLAlchemy()

# GET Method / READ all items
def index():
    get_items = Item.query.all()
    item_schema = ItemSchema(many=True)
    items = item_schema.dump(get_items)
    item_entities = []

    for item in items:
        print(item)
        item_entity = ItemEntity(item)
        item_entities.append(item_entity)
        
    return make_response(jsonify({"item": [i.toJSON() for i in item_entities]}))

# GET Method / READ one item by ID
def get_by_id(item_id):
    get_item = Item.query.get(item_id)
    item_schema = ItemSchema()
    item = item_schema.dump(get_item)
    item_entity = ItemEntity(item)
    return make_response(jsonify({"item": item_entity.toJSON()}))

# PUT Method / UPDATE
def update_by_id(item_id):
    data = request.get_json()
    get_item = Item.query.get(item_id)

    if data.get('name_item'):
        get_item.name_item = data['name_item']
    if data.get('desc_item'):
        get_item.desc_item = data['desc_item']
    if data.get('size'):
        get_item.size = data['size']
    if data.get('color'):
        get_item.color = data['color']
    if data.get('price'):
        get_item.price= data['price'] 
    if data.get('discount'):
        get_item.discount= data['discount']
    if data.get('SKU'):
        get_item.SKU= data['SKU'] 
    if data.get('quantity_stock'):
        get_item.quantity_stock= data['quantity_stock']
    if data.get('image_path'):
        get_item.image_path= data['image_path']
    if data.get('created_at'):
        get_item.created_at= data['created_at']    
    if data.get('modified_at'):
        get_item.modified_at= data['modified_at']
    if data.get('deleted_at'):
        get_item.deleted_at= data['deleted_at'] 

    db.session.add(get_item)
    db.session.commit()
    item_schema = ItemSchema(only=['item_id', 'name_item', 'desc_item','size','color','price', 'discount', 'SKU', 'quantity_stock', 'image_path','created_at','modified_at','deleted_at'])
    item = item_schema.dump(get_item)
    return make_response(jsonify({"item": item}))

# POST Method / CREATE
def create():
    data = request.get_json()
    item_schema = ItemSchema()
    item = item_schema.load(data)
    result = item_schema.dump(item.create())
    return make_response(jsonify({"item": result}),200)

# DELETE Method / DELETE
def delete_by_id(item_id):
    get_item = Item.query.get(item_id)
    db.session.delete(get_item)
    db.session.commit()
    return make_response("",204)
