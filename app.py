import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("car_model.pkl", "rb") as f:
    model = pickle.load(f)
    
st.subheader("created_LAVKESH")
st.title("🚗Price Prediction App")


# -------------------------------
# User Inputs
# -------------------------------

# Fuel type
fueltype = st.selectbox(
    "Fuel Type",
    options=["gas", "diesel"]
)

# Engine size
enginesize = st.slider(
    "Engine Size (cc)",
    min_value=50,
    max_value=500,
    value=150
)

# Cylinder number (single selection)
cylinder = st.selectbox(
    "Number of Cylinders",
    options=["two", "three", "four", "five", "six", "eight", "twelve"]
)

# -------------------------------
# One-Hot Encoding Cylinders
# -------------------------------

cylindernumber_two = 1 if cylinder == "two" else 0
cylindernumber_three = 1 if cylinder == "three" else 0
cylindernumber_four = 1 if cylinder == "four" else 0
cylindernumber_five = 1 if cylinder == "five" else 0
cylindernumber_six = 1 if cylinder == "six" else 0
cylindernumber_eight = 1 if cylinder == "eight" else 0
cylindernumber_twelve = 1 if cylinder == "twelve" else 0

# Encode fuel type (adjust if your model uses different encoding)
fueltype_encoded = 1 if fueltype == "diesel" else 0

# -------------------------------
# Create Input DataFrame
# -------------------------------

input_data = pd.DataFrame([{
    "fueltype": fueltype_encoded,
    "enginesize": enginesize,
    "cylindernumber_eight": cylindernumber_eight,
    "cylindernumber_five": cylindernumber_five,
    "cylindernumber_three": cylindernumber_three,
    "cylindernumber_four": cylindernumber_four,
    "cylindernumber_six": cylindernumber_six,
    "cylindernumber_twelve": cylindernumber_twelve,
    "cylindernumber_two": cylindernumber_two
}])

st.subheader("Input Features")
st.write(input_data)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    indianprice=prediction*(91.02)
    st.success(f"💰 Estimated Car Price: ₹{indianprice:,.2f}")
