from models.item_model import *
from settings import *

# GET Method / READ all items

@app.route('/items', methods = ['GET'])
def index_items():
    get_items = Item.query.all()
    item_schema = ItemSchema(many=True)
    items = item_schema.dump(get_items)
    return make_response(jsonify({"item": items}))

# GET Method / READ one item by ID

@app.route('/items/<item_id>', methods = ['GET'])
def get_item_by_id(item_id):
    get_item = Item.query.get(item_id)
    item_schema = ItemSchema()
    item = item_schema.dump(get_item)
    return make_response(jsonify({"item": item}))

# PUT Method / UPDATE

@app.route('/items/<item_id>', methods = ['PUT'])
def update_item_by_id(item_id):
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

    db.session.add(get_item)
    db.session.commit()
    item_schema = ItemSchema(only=['item_id', 'name_item', 'desc_item','size','price', 'discount', 'SKU', 'quantity_stock'])
    item = item_schema.dump(get_item)
    return make_response(jsonify({"item": item}))

# POST Method / CREATE

@app.route('/items', methods = ['POST'])
def create_item():
    data = request.get_json()
    item_schema = ItemSchema()
    item = item_schema.load(data)
    result = item_schema.dump(item.create())
    return make_response(jsonify({"item": result}),200)

# DELETE Method / DELETE

@app.route('/items/<item_id>', methods = ['DELETE'])
def delete_item_by_id(item_id):
    get_item = Item.query.get(item_id)
    db.session.delete(get_item)
    db.session.commit()
    return make_response("",204)

if __name__ == "__main__":
    app.run(debug=True)