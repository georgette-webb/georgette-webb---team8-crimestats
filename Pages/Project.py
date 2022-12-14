import streamlit as st

st.markdown("# Page 2")
st.sidebar.markdown("# Page 2")

st.title('Team 3 - Crime Statisitcsvxcvx')

df = st.session_state['df']
st.header('Description of the dataset uploaded')
st.markdown('Description of the dataset uploaded')
st.write(df.describe())

st.markdown('Description of the dataset uploaded Transposed')
st.write(df.describe().T)