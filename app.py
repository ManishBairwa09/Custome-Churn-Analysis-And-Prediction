#Gender -> 1 is female and 0 is male
#Churn -> 1 is yes and 0 is no
#Scaler is exported a scaler.pkl
# model is exported as model.pkl
# order of the x 'Age', 'Gender', 'Tenure', 'MonthlyCharges' #

import numpy as np 
import streamlit as st 
import joblib

st.title("Churn Prediction")
st.divider()

st.write("Plese enter the values and hit the predict button for getting a prediction ")
st.divider()

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

age = st.number_input("Enter your age " ,min_value=10 , max_value=100 , value=30)

tenure = st.number_input("Enter tenure" , min_value=0 ,max_value=130, value=10)

monthly_charges = st.number_input("Enter Monthly Charges" , min_value=30 , max_value=150)

gender = st.selectbox("Enter your gender ", ["Male" , "Feamale"])
st.divider()

predict_button = st.button("Predict!")
st.divider()

if predict_button:
    gender_selected = 1 if gender == "Female" else 0
    X = [age , gender_selected , tenure , monthly_charges ]
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]

    predicted = "Yes" if prediction == 1 else "No"
    st.balloons()
    st.write(f"Predicted :{predicted}")


else:
    print("Please enter the values and then hit the predict button ")    
