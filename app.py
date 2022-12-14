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
st.markdown('In this Data Challenge Team 8 will be working with a SA Crime Dataset adapted from Crime Statistics 2021-22. Using this dataset. We aim to demonstrate our newly acquired data science skills and use them to inform how Local Government, or the South Australian Police (SAPOL) can improve the safety of their State. We aim to understand and explore the dataset in order to investigate the different types of crimes and their differing characteristics to gain insights and solve problems to reduce the crime rate.')
st.markdown('The Members in Team 8 are: Giselle, Bruno, Luke, Georgette, Maryam1621 and Atousa')
st.markdown('The Mentor for Team 8 is: Malgorzata')

file_loaded = st.file_uploader('Upload your CSV files here')

if file_loaded:
    df = pd.read_csv(file_loaded)
    st.session_state['df'] = df

    st.header('This is the dataset displays as a whole')
    st.dataframe(df)

    st.header('Description of the dataset uploaded')
    st.markdown('Description of the dataset uploaded')
    st.write(df.describe())

    st.markdown('Description of the dataset uploaded Transposed')
    st.write(df.describe().T)

    st.header('Shape of the dataset uploaded')
    st.markdown('This table of the data uploaded shows the shape of the dataset uploaded. It shows the number of Rows and Columns')
    st.dataframe(df.shape)

    st.header('Data displaying the Head of the Dataset')
    st.dataframe(df.head())

    st.header('Data displaying the tail of the Dataset')
    st.dataframe(df.tail(3))

    

   



