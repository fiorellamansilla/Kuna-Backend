from models.item import Item, ItemSchema
from flask import make_response, jsonify, request
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()

# GET Method / READ all items
def index():
    get_items = Item.query.all()
    item_schema = ItemSchema(many=True)
    items = item_schema.dump(get_items)
    return make_response(jsonify({"item": items}))

# GET Method / READ one item by ID
def get_by_id(item_id):
    get_item = Item.query.get(item_id)
    item_schema = ItemSchema()
    item = item_schema.dump(get_item)
    return make_response(jsonify({"item": item}))

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

    db.session.add(get_item)
    db.session.commit()
    item_schema = ItemSchema(only=['item_id', 'name_item', 'desc_item','size','price', 'discount', 'SKU', 'quantity_stock', 'image_path'])
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
