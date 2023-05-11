from flask import Flask
from application import app
from flask import render_template
from flask import request
import requests

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    return render_template('convert.html')