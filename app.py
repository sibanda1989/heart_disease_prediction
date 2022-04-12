from crypt import methods
from flask import Flask, render_template, request
import jsonify
import requests
import joblib
import numpy as np
import sklearn
import pandas as pd



app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Age = int(request.form['Age'])

    return render_template("predict.html")    

