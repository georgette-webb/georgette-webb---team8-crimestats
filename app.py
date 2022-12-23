import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Team 8 - Crime Statistics',
    page_icon=':bar_chart:',
    layout="wide"
)

st.title('Team 8 Crime Statistics Data Challenge APP')
st.markdown('Welcome to our presentation for Team 8. This team consists of Giselle, Bruno, Georgette, Maryam, Atousa and myself. My name is Luke , and for this Data Challenge, Team 8 will be working with SAPOL Crime Statistics Dataset from 2019-2022.')
st.markdown('The Members in Team 8 are: Giselle, Bruno, Luke, Georgette, Maryam and Atousa')
st.markdown('The Mentor for Team 8 is: Malgorzata')

file_loaded = st.file_uploader('Upload your CSV files here')

if file_loaded:
    df = pd.read_csv(file_loaded)    
    
    st.session_state['df'] = df

    st.header('Dataset displayed as a whole')
    st.dataframe(df)

    #st.header('Description of the dataset uploaded')
    #st.markdown('Description of the dataset uploaded')
    #st.write(df.describe())

    #st.markdown('Description of the dataset uploaded Transposed')
    #st.write(df.describe().T)

    #st.header('Shape of the dataset uploaded')
    #st.markdown('Shows the shape of the dataset uploaded. The number of Rows and Columns')
    #st.dataframe(df.shape)

    #st.header('Data Types of the dataset uploaded')
    #st.markdown('Shows the Data type of the dataset uploaded. ')
    #st.dataframe(df.dtypes)

    #st.header('Data displaying the Head of the Dataset, 1st 5 rows')
    #st.dataframe(df.head())

    #st.header('Data displaying the tail of the Dataset, last 3 rows')
    #st.dataframe(df.tail(3))



    #

