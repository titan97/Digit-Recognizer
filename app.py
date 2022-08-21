from urllib import response
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    response = "For ML Prediction"
    return response
