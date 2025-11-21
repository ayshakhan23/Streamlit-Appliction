import streamlit as st
import pickle

model=pickle.load (open("car_model.pkl","rb"))
le=pickle.load(open("label_encoder.pkl","rb"))

st.title("Car prediction App")

car_model=st.selectbox("select car model",le.classes_)
mileage=st.number_input("enter mileage(in miles)",min_value=0)

