#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import joblib


# In[2]:


# Title
st.header("Iris Classifier App")

# Input bar 1
sepal_l = st.number_input("Enter Mileage")

# Input bar 2
sepal_w = st.number_input("Enter Liter")

# Input bar 3
petal_l = st.number_input("Enter Liter")

# Input bar 4
petal_w = st.number_input("Enter Liter")

# If button is pressed
if st.button("See your species"):
    
    # Unpickle classifier
    regmodel = joblib.load("iris_classer.pkl")
    
    # Store inputs into dataframe
    x = pd.DataFrame([[sepal_l, sepal_w, petal_l, petal_w]], columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"])
     
    # Get prediction
    prediction = iris_classer.predict(x)
    
    # Output prediction
    st.text(f"The price is {prediction}")

