from flask import Flask
from application import app

@app.route('/', methods=['GET'])
def home():
    return("no2")