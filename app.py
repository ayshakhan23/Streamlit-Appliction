import streamlit as st
import pickle

model = pickle.load(open("car_model.pkl","rb"))
le = pickle.load(open("label_encoder.pkl","rb"))


## for title - Heading
st.title("Car prediction app")

## dropdown for car models

with st.form("my_form"):
    text = st.text_input("Enter Your Name")
    submit = st.form_submit_button("Submit")

if submit:
    st.write("Hello:", text)
    st.empty()

car_model = st.selectbox("Select Car Model", le.classes_)

## User inputs
mileage = st.number_input("Enter mileage (in miles)", min_value=0)
age=st.slider("car age(years)",0,6)

##selected car model to encode
encoded_model= le.transform([car_model])[0]

if st.button("Predict price"):
    input_data =[[encoded_model,mileage,age]]
    predicted_price = model.predict(input_data)
    st.success(f"Estimated selling price: {predicted_price[0]}")

st.image("image.png", caption="My Image", width=300)

import pandas as pd
df = pd.DataFrame({"Name": ["A", "B"], "Age": [20, 30]})
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
