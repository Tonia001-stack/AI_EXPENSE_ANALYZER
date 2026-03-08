import streamlit as st
from model import predict_expense

#Page configuration
st.set_page_config(
    page_title= "Expense AI ANalyzer",
    page_icon="💰",
      layout="wide",
)
# App title
st.title("💰 Expense AI Analyzer")
#sidebar
st.sidebar.title("About")
st.sidebar.write("""
This AI tool classifies expense description into categories.

Model:
TF-IDF + Naibe Bayes

Categories:
-Food
-Bills
-Transport
-Shopping
-Others.""")                                                                                                                                                        


st.write(
    "Enter an expence description and the AI will predict its category."
)

#Text input
description = st.text_input(
        "Expense Description",
    placeholder="e.g Bought beans, paid electricity bill"
  )
# Predict button
predict_button = st.button("Predict Category")

st.divider()
  
#Prediction area
if predict_button:
    
      if description.strip() == "":
        st.warning("Please enter a valid expense description.")
      else:
        category, confidence = predict_expense(description)

        st.success(f"Predicted Category: **{category}**")

        st.write(f"Confidence: Level")
        st.progress(int(confidence))

        st.info(f"Model Confidence: {confidence}%")
