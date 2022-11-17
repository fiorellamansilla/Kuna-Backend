from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.client import client_bp
from routes.item import  item_bp
from routes.order import order_bp
from routes.order_item import order_item_bp

# Create an instance of the Flask App 
app = Flask(__name__)

# Routes
app.register_blueprint(client_bp, url_prefix='/client')
app.register_blueprint(item_bp, url_prefix='/item')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(order_item_bp, url_prefix='/order_item')

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/kuna_db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
