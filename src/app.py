from flask import Flask, jsonify
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
            item = {'item_id':fila[0], 'name_item':fila[1], 'desc_item':fila[2], 'size':fila[3], 'price':fila[4], 'SKU':fila[5], 'quantity_stock':fila[6]}
            items.append(item)
        return jsonify({'items': items, 'message': "Productos listados."})

    except Exception as ex:
        return jsonify ({'message': "Error"})

# GET Method for fetching only one item with its ID
@app.route("/items/<item_id>", methods = ['GET'])  
def read_items(item_id):
    try:
        cursor = connection.connection.cursor()
        sql =  "SELECT * FROM items WHERE item_id = '{0}'".format(item_id)
        cursor.execute(sql)
        datos = cursor.fetchone()

        if datos != None:
            item = {'item_id':datos[0], 'name_item':datos[1], 'desc_item':datos[2], 'size':datos[3], 'price':datos[4], 'SKU':datos[5], 'quantity_stock':datos[6]}
            return jsonify({'item': item, 'message': "Item encontrado."})
        else:
            return jsonify({'message': "Item no encontrado."})

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
 
