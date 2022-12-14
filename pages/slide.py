import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Team 8 - Slides',
    page_icon=':bar_chart:',
    layout="wide"
)
st.title('Team 8 Slides')

from PIL import Image
image = Image.open('Cover_Page.jpg')

st.image(image, caption='Team 8 - Cover Page Slide')

