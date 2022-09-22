from crypt import methods
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

# Create an instance of the Flask App 
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/kuna_db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
