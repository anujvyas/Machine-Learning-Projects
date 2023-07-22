# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:34:58 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open("D:\Supervised Machine Learning with Python (Streamlit Deployed)\Water Quality Analysis\Trained_model.sav",'rb'))

#creating a function for prediction
def water_quality_analyser(input_data):
    #changing the input_data to numpy data
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return prediction

def main():
    #giving the title
    st.title('Water Quality Analysis and Prediction Web App')
    
    #getting input from user
    ph = st.text_input('pH Value of water : ')
    Hardness = st.text_input('Capacity of water to precipitate soap in mg/L(Hardness) : ')
    Solids = st.text_input('Total dissolved solids in ppm : ')
    Chloramines = st.text_input('Amount of Chloramines in ppm : ')
    Sulfate = st.text_input('Amount of Sulfates dissolved in mg/L : ')
    Conductivity = st.text_input('Electrical conductivity of water in μS/cm : ')
    Organic_carbon = st.text_input('Amount of organic carbon in ppm : ')
    Trihalomethanes = st.text_input('Amount of Trihalomethanes in μg/L : ')
    Turbidity = st.text_input('Measure of light emiting property of water in NTU : ')
   
    
    #code for prediction
    water_potability = ''
    
    #getting input data from the user
    if st.button('Predicted POTABILITY OF Water : '):
        water_potability = water_quality_analyser([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(water_potability)

if __name__ == '__main__':
    main()