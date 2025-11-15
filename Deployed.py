import streamlit as st
import numpy as np
import pandas as pd 
import joblib


# load the transformer and model
with open('transformer.joblib','rb') as file:
    transformer = joblib.load(file)
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)

st.title("INN HOTEL GROUP")
st.header(":blue[This application will predict the chance of cancellation of booking]")
#lets take input from user
amnth = st.slider("Arrival Month",min_value=1,max_value=12)
wkd_lambda = (lambda x:0 if x=='Mon'else
       1 if x=='Tue'else
       2 if x=='Wed'else
       3 if x=='Thu'else
       4 if x=='Fri'else
       5 if x=='Sat'else 6)
awkd = wkd_lambda(st.selectbox("Arrival Weekday",options=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
dwkd = wkd_lambda(st.selectbox("Departure Weekday",options=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
wkend = st.number_input("Enter hoe many Weekend Nights are there in stay",min_value=0)
wk = st.number_input("Enter how many Week Nights are there in Stay",min_value=0)
totn = wkend + wk
mkt = (lambda x:0 if x=='Offline' else 1)(st.selectbox("mode of booking",options=['Offline','Online']))
lt = st.number_input("How many days prior the booking was made",min_value=0)
price = st.number_input("Enter the average price per night",min_value=0.0)
adults = st.number_input(" How many Number of adults",min_value=0)
spcl = st.number_input("How many Special Requests were made",min_value=0)
park = (lambda x: 0 if x == 'No' else 1)(
    st.selectbox("Parking required or not", options=['No', 'Yes'])
)

# Trasnform the input data
lt_t,price_t = transformer.transform([[lt,price]])[0]

#create the input_list
input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth,awkd,totn,dwkd]

# Make Prediction
prediction = model.predict_proba([input_list])[:,1][0]

# lets shoe the probability
if st.button("Predict Cancellation Probability"):
    st.success(f"The probability of cancellation is : {round(prediction,4)*100} %")