from crypt import methods
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/kuna_db'
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column (db.Integer, autoincrement = True, nullable =False, primary_key=True)
    name_item = db.Column(db.String(128), nullable=False, unique=True )
    desc_item = db.Column (db.String(2024), nullable=False)
    size = db.Column (db.String(64), nullable=False)
    price = db.Column (db.Float, nullable=False, server_default="0")
    discount = db.Column (db.Float, nullable=False, server_default="0")
    SKU = db.Column (db.String(128), nullable=False)
    quantity_stock = db.Column (db.Integer, nullable=False, server_default="0")

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self,name_item,desc_item,size,price,discount,SKU,quantity_stock):
        self.name_item = name_item
        self.desc_item = desc_item
        self.size = size
        self.price = price
        self.discount = discount
        self.SKU = SKU
        self.quantity_stock = quantity_stock

    def __repr__(self):
        return '' % self.item_id

db.create_all

class ItemSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Item
        load_instance = True
        sqla_session = db.session
    item_id = fields.Number(dump_only=True)
    name_item = fields.String(required=True)
    desc_item = fields.String(required=True)
    size = fields.String(required=True)
    price = fields.Number(required=True)
    discount = fields.Number(required=True)
    SKU = fields.String(required=True)
    quantity_stock = fields.Number(required=True)

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

    
