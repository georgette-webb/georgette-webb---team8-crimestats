import streamlit as st

df = st.session_state['df']

st.title('Team 8 Slides')

st.header('Description of the dataset uploaded')
st.markdown('Description of the dataset uploaded')
st.write(df.describe())

st.markdown('Description of the dataset uploaded Transposed')
st.write(df.describe().T)