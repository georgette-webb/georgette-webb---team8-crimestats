import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Team 8 - Crime Statistics',
    page_icon=':bar_chart:',
    layout="wide"
)

st.title('Team 8 - Crime Statistics')

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
    ####