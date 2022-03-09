# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:58:39 2022

@author: parth
"""


#import pandas as pd
#import numpy as np
import pickle
import streamlit as st
#from PIL import Image
  
# loading in the model to predict on the data
 #pickle_in = open('randomforest.pkl', 'rb')
#randomforestclassifier = pickle.load(pickle_in)
model=pickle.load(open('randomforest.pkl', 'rb'))
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(number, incident_state, opened_by, opened_at, sys_updated_by,
       sys_updated_at, subcategory, resolved_by, resolved_at, closed_at):  
   
    prediction = model.predict(
        [[number, incident_state, opened_by, opened_at, sys_updated_by,
       sys_updated_at, subcategory,resolved_by, resolved_at, closed_at]])
    print(prediction)
    return prediction
      
  def fun1(incident_state):
    if incident_state=='Active':
        return 1
    elif incident_state=='Awaiting Evidence':
        return 2
    elif incident_state=='Awaiting Problem':
        return 3
    elif incident_state=='Awaiting User info':
        return 4
    elif incident_state=='Awaiting Vendor':
        return 5
    elif incident_state=='Closed':
        return 6
    elif incident_state=='New':
        return 7
    elif incident_state=='Resolved':
        return 8
    return 0

subcat=['Subcategory '+str(i) for i in range(2,254,1)]
value3=np.array([[j] for j in range(0,254,1)])
value3=scaler.fit_transform(value3)
dic3={ i:j for i,j in zip(subcat,value3) }

def fun7(subcategory):
    if subcategory in dic3.keys():
        subcategory=dic3[subcategory]
        return subcategory
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Incident Predictions")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Predict the Impact of Incidents </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    number = st.text_input("number", "Type Here")
    incident_state=st.selectbox("what is the incident state ?",('Active','Awaiting Evidence','Awaiting Problem','Awaiting User info','Awaiting Vendor','Closed','New','Resolved','Not Available'))
    opened_by = st.input_number("opened_by", min_value=0,step=1)
    opened_at= st.input_number("opened_at", min_value=0,step=1)
    sys_updated_by= st.input_number("sys_updated_by", min_value=0,step=1)
    sys_updated_at= st.input_number("sys_updated_at", min_value=0,step=1)
    subcategory=st.selectbox("Subcategory ?",(['Subcategory '+str(i) for i in range(2,254,1)]))
    resolved_at= st.input_number("resolved_at", min_value=0,step=1)
    resolved_by= st.input_number("resolved_by", min_value=0,step=1)
    closed_at= st.input_number("closed_at", min_value=0,step=1)
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(number, incident_state, opened_by, opened_at, sys_updated_by,
        sys_updated_at, subcategory, resolved_by, resolved_at, closed_at)
    st.success('The output is {}'.format(result))
               
if __name__=='__main__':
    main()