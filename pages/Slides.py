import streamlit as st

st.set_page_config(
    page_title='Team 8 - Slides',
    page_icon=':bar_chart:',
    layout="wide"
)
st.title('Team 8 Slides')

from PIL import Image
image = Image.open('slides\Cover.png')
st.image(image, caption='Team 8 - Cover Slide')

image = Image.open('./pages/Slide2.png')
st.image(image, caption='What effect did the COVID-19 Pandemic have on crime?')

image = Image.open('./pages/Slide3.png')
st.image(image, caption='Where did the most crime occur? (July 2019-June 2022)')

image = Image.open('./pages/Slide4.png')
st.image(image, caption='Reported Incidents – Top 5 Locations 2021')

image = Image.open('./pages/Slide5.png')
st.image(image, caption='Warmer weather, “Mad March”, and the holiday season')

image = Image.open('./pages/Slide6.png')
st.image(image, caption='Offence Count – Adelaide CBD (5000)')

image = Image.open('./pages/Slide7.png')
st.image(image, caption='Offences in 2022 – Adelaide CBD (5000)')

image = Image.open('./pages/Slide8.png')
st.image(image, caption='Number of "Acts intended to cause injury" - Adelaide CBD (5000)')

image = Image.open('./pages/Slide9.png')
st.image(image, caption='Number of “Thefts and Related Offences” – Adelaide CBD (5000)')

image = Image.open('./pages/Slide10.png')
st.image(image, caption='Number of reported incidents per weekday for Adelaide CBD (5000)')

image = Image.open('./pages/Slide11.png')
st.image(image, caption='Offence counts in areas with large shopping centres')

image = Image.open('./pages/Slide12.png')
st.image(image, caption='Conclusions')
