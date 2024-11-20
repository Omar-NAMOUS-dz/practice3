from flask import Flask, jsonify
from random import randint

app = Flask(__name__)

@app.route('/')

def home():
    return str("Docker compose restart works!!!")

if __name__=="__main__":
    app.run(host = '0.0.0.0', port=5000)
