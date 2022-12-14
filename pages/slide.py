import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Team 8 - Slides',
    page_icon=':bar_chart:',
    layout="wide"
)
st.title('Team 8 Slides')

df = st.session_state['df']
st.line_chart(df, x=None, y=None, width=0, height=0, use_container_width=True)