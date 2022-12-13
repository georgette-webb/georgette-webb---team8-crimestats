import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Team 8 - Crime Statistics',
    page_icon=':bar_chart:',
    layout="wide"
)

st.title('Team 8 Crime Statistics Data Challenge APP')
st.markdown('In this Data Challenge Team 8 will be working with a SA Crime Dataset adapted from Crime Statistics 2021-22. Using this dataset, we aim to understand and explore the dataset in order to later investigate the different types of crimes and their differing characteristics to gain insights and solve problems to reduce the crime rate.The Members in Team 8 are: Giselle, Bruno, Luke, Georgette, Maryam1621 and Atousa')
st.markdown('The Mentor for Team 8 is: Malgorzata')


file_loaded = st.file_uploader('Upload you file here')

if file_loaded:
    df = pd.read_csv(file_loaded)

    st.header('Description of the dataset uploaded')
    st.markdown('This table is a description of the dataset uploaded')
    st.write(df.describe())
    #st.write(df.shape())

    st.header('Shape of the dataset uploaded')
    st.markdown('This table of the data uploaded shows the shape of the dataset uploaded. It shows the number of Rows and Columns')
    st.dataframe(df.shape)
    #####SS