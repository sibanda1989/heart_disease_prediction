from crypt import methods
from mmap import mmap
from flask import Flask, render_template, request
import jsonify
import requests
import joblib
import numpy as np
import sklearn
import pandas as pd

model = joblib.load("heart_disease_model.pkl")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Age = int(request.form['Age'])
        RestingBP = int(request.form['RestingBP'])
        Cholesterol = int(request.form['Cholesterol'])
        FastingBS = int(request.form['FastingBS'])
        MaxHR = int(request.form['MaxHR'])
        OldPeak = int(request.form['OldPeak'])

        Sex = request.form['Sex']
        if Sex == 'Male':
            Sex_M = 1
        else:
            Sex_M = 0

        ChestPainType = request.form['ChestPainType']
        if ChestPainType == 'ATA':
            ChestPainType_ATA = 1
            ChestPainType_NAP = 0
            ChestPainType_TA = 0

        elif ChestPainType == 'NAP':                
            ChestPainType_ATA = 0
            ChestPainType_NAP = 1
            ChestPainType_TA = 0

        elif ChestPainType == 'TA':                
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 1

        else:
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA = 0

        RestingECG = request.form['RestingECG']
        if RestingECG == 'Normal':
            RestingECG_Normal = 1
            RestingECG_ST = 0

        elif RestingECG == 'ST':
            RestingECG_Normal = 0
            RestingECG_ST = 1

        else:
            RestingECG_Normal = 0
            RestingECG_ST = 0

        ExerciseAngina = request.form['ExerciseAngina']
        if ExerciseAngina == 'Y':
            ExerciseAngina_Y = 1

        else:
            ExerciseAngina_Y = 0

        ST_Slope = request.form['ST_Slope']
        if ST_Slope == "Flat":
            ST_Slope_Flat = 1
            ST_Slope_Up = 0

        elif ST_Slope == "Up":
            ST_Slope_Flat = 0
            ST_Slope_Up = 1

        else:
            ST_Slope_Flat = 0
            ST_Slope_Up = 0
                        

        prediction = model.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex_M, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST, ExerciseAngina_Y, ST_Slope_Flat, ST_Slope_Up]])
        output = prediction[0]

        if output == 0:
            return render_template('index.html', prediction_texts="Patient is unlikely to have Heart Disease")

        else:
            return render_template('index.html', prediction_texts="Patient is highly likely to have Heart Disease")    

    else: 
        return render_template("index.html")    


if __name__=="__main__":
    app.run(debug=True)
