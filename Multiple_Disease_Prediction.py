#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:04:20 2025

@author: balogunishaq
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))

heart_disease_trained_model = pickle.load(open('heart_disease_trained_model.sav', 'rb'))

calorie_burn_trained_model = pickle.load(open('calorie_burn_trained_model.sav', 'rb'))


# sidebar to navigate
with st.sidebar:
    
    selected = option_menu('Multiple Disease Predictive System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Calorie Burn Prediction'],
                           
                           icons = ['activity','heart','person'],
                           default_index = 0) # the choses the 1st index file to load on the sidebar
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    
    # columns from the user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose Level")
        
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
        
    with col2:
        Insulin = st.text_input("Insulin Level")
        
    with col3:
        BMI = st.text_input("BMI value")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
        
    with col2:
        Age = st.text_input("Age of the person")
    
    # code for prediction
    
    diab_diagnosis = ''
    
    # creating button for prediction
    
    if st.button('Diabetes Test Result'):
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is not Diabetic' # this is not working
            
            
    st.success(diab_diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    
    # columns from the user
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of the Person")
        
    with col2:
        sex = st.text_input("Gender of the Person")
        
    with col3:
        cp = st.text_input("Chest Pain Type")
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
        
    with col2:
        chol = st.text_input("Serum Cholesterol")
        
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
        
    with col1:
        restecg = st.text_input("Resting Cardiographic Result")
        
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang = st.text_input("Exercise Induced Vagina")
        
    with col1:
        oldpeak = st.text_input("Depression Induced by Exercise")
        
    with col2:
        slope = st.text_input("Slope of the Peak Exercise")
        
    with col3:
        ca = st.text_input("Colored Flouroscopy")
        
    with col1:
        thal = st.text_input("Normal")
    
    # code for prediction
    
    heart_diagnosis = ''
    
    # creating button for prediction
    
    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	#oldpeak,
    
    if st.button('Heart Disease Test Result'):
        
        heart_prediction = heart_disease_trained_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'This person is having heart disease'
        else:
            heart_diagnosis = 'This person does not have any heart disease' # this is not working
            
            
    st.success(heart_diagnosis)
    
if (selected == 'Calorie Burn Prediction'):
    
    # Page title
    st.title('Calorie Burn Prediction using ML')
    
    # columns for user input
    col1, col2, col3 = st.columns(3)
    
    #with col1:
        #User_ID = st.text_input("User ID of an Individual")
        
    with col1:
        Gender = st.text_input("Gender of an Individual")
        
    with col2:
        Age = st.text_input("Age of an Individual")
        
    with col3:
        Height = st.text_input("Height of an Individual in (cm)")
        
    with col1:
        Weight = st.text_input("Weight of an Individual in (kg)")
        
    with col2:
        Duration = st.text_input("Duration of an Exercise of an Individual")
        
    with col3:
        Heart_Rate = st.text_input("Heart Rate of an Individual")
        
    with col1:
        Body_Temp = st.text_input("Body Temperature of an Individual")
    
    # code for prediction
    
    calorie_prediction = ''
    
    if st.button('Calorie Burn Prediction Result'):
        
        calorie_result = calorie_burn_trained_model.predict([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])
        
        if (calorie_result[0] == 1):
            print("High Calories")
        else:
            print("Low Calories")
            
    st.success(calorie_prediction)