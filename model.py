import joblib
import numpy as np

#Load the model once
model = joblib.load("expense_model.pkl")

def predict_expense(description: str):
    prediction = model.predict([description])[0]
    probabilities = model.predict_proba([description])[0]
    confidence = np.max(probabilities)

    return prediction, round(confidence * 100, 2)



   
