import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Team 8 - Slides',
    page_icon=':bar_chart:',
    layout="wide"
)
st.title('Team 8 Slides')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)