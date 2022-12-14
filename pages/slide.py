import streamlit as st

st.set_page_config(
    page_title='Team 8 - Slides',
    page_icon=':bar_chart:',
    layout="wide"
)
st.title('Team 8 Slides')

df = st.session_state['df']
st.header('Description of the dataset uploaded')
st.markdown('Description of the dataset uploaded')
st.write(df.describe())

st.markdown('Description of the dataset uploaded Transposed')
st.write(df.describe().T)