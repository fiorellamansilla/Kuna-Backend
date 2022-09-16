from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

connection = MySQL(app)

 # GET Method for fetching all the items with their basic information

@app.route("/items", methods = ['GET'])
def list_items():
    try:
        cursor = connection.connection.cursor()
        sql =  "SELECT * FROM items"
        cursor.execute(sql)
        datos = cursor.fetchall()

        # Return data from database with JSON 

        items = []
        for fila in datos:
            item = {'item_id':fila[0], 'name_item':fila[1], 'desc_item':fila[2], 'size':fila[3], 'price':fila[4], 'discount':fila[5], 'SKU':fila[6], 'quantity_stock':fila[7]}
            items.append(item)
        return jsonify({'items': items, 'message': "Productos listados."})
    except Exception as ex:
        return jsonify ({'message': "Error"})

# GET Method / READ :  fetching only one item with its ID

@app.route("/items/<item_id>", methods = ['GET'])  
def read_item(item_id):
    try:
        cursor = connection.connection.cursor()
        sql =  "SELECT * FROM items WHERE item_id = '{0}'".format(item_id)
        cursor.execute(sql)
        datos = cursor.fetchone()

        if datos != None:
            item = {'item_id':datos[0], 'name_item':datos[1], 'desc_item':datos[2], 'size':datos[3], 'price':datos[4], 'discount':datos[5], 'SKU':datos[6], 'quantity_stock':datos[7]}
            return jsonify({'item': item, 'message': "Producto encontrado."})
        else:
            return jsonify({'message': "Producto no encontrado."})
    except Exception as ex:
        return jsonify ({'message': "Error"})

# POST Method / CREATE : for insert a new item into the database

@app.route("/items", methods = ['POST'])
def create_item():
    try:
        cursor = connection.connection.cursor()
        sql =  """INSERT INTO items (item_id, name_item, desc_item, size, price, discount,  SKU, quantity_stock) 
        VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, '{6}', {7})""".format(request.json['item_id'], request.json['name_item'], request.json['desc_item'], request.json['size'], 
        request.json['price'], request.json['discount'], request.json['SKU'], request.json['quantity_stock'])
        cursor.execute(sql)
        connection.connection.commit()
        return jsonify({'message': "Producto registrado."})
    except Exception as ex:
        return jsonify ({'message': "Error"})

# PUT Method / UPDATE data from an item into the database

@app.route("/items/<item_id>", methods = ['PUT'])
def update_item(item_id):
    try:
        cursor = connection.connection.cursor()

        sql = """UPDATE items SET name_item = '{0}', desc_item = '{1}', size = '{2}', price = {3}, discount = {4}, SKU = '{5}', quantity_stock = {6} 
        WHERE item_id = {7}""" .format (request.json['name_item'], request.json['desc_item'], request.json['size'], 
        request.json['price'], request.json['discount'], request.json['SKU'], request.json['quantity_stock'], item_id)
    
        cursor.execute(sql)
        connection.connection.commit()
        return jsonify({'message': "Producto actualizado."})
    except Exception as ex:
        return jsonify ({'message': "Error"})


# DELETE Method : eliminate an item from the database

@app.route("/items/<item_id>", methods = ['DELETE'])
def delete_item(item_id):
    try:
        cursor = connection.connection.cursor()
        sql = "DELETE FROM items WHERE item_id = '{0}'".format(item_id)
        cursor.execute(sql)
        connection.connection.commit()
        return jsonify({'message': "Producto eliminado."})
    except Exception as ex:
        return jsonify ({'message': "Error"})



def page_not_found(error):
    return "<h1> La página que intentas buscar no existe. </h1>", 404
    
def index():
    return "Baby Kuna"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
 
