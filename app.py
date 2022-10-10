from flask import Flask

# Create an instance of the Flask App 
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/kuna_db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run()
