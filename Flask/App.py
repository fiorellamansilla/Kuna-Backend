import string
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Baby Kuna'


if __name__ == '__main__':
    app.run(port=3000, debug=True)