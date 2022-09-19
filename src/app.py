from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config
from validation import *
from controllers import ItemController

app = Flask(__name__)
connection = MySQL(app)

def page_not_found(error):
    return "<h1> La página que intentas buscar no existe. </h1>", 404
    
def index():
    return "Baby Kuna"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
 
