from flask import Flask, jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

connection = MySQL(app)

@app.route("/items", methods = ['GET'])
def list_items():
    try:
        # Create connection with SQL database and GET Method

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
    
def page_not_found(error):
    return "<h1> La página que intentas buscar no existe. </h1>"
    
def index():
    return "Baby Kuna"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
 
