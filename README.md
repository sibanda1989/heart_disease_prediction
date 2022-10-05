# Heart Disease Prediction
This is a Machine Learning application developed in Python to predict whether a patient is likely to have a heart disease or not from a series of patient record features like Age, Blood Pressure, Sex etc.

## How it works
In the background the application uses a Machine Learning model *heart_disease_model.pkl* to predict heart disease from values entered in the from provided to the user on the home page.

## The Machine Learning model
This is a Random Forest model arrived upon as the best performing model using the Recall metric. The process taken to train the model are documented in the python notebook *heart_predHS100421*. A set of values,in *heart.csv*, sourced from [Kaggle](https://www.kaggle.com/) was used to train the model.