import streamlit as st 

st.title("Calculate your BMI")
wt = st.number_input("Enter your Weight in kg:")
h = st.number_input("Enter your Height in m:")
if h == 0:
    st.error("Height cannot be zero")
bmi = wt/h**2
st.success(f"Your BMI is {bmi}KG/m^2")
