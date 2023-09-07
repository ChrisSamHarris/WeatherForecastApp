import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Weather Forecast", layout="centered", page_icon="🌦️")


st.title("Dynamic Weather Forecast")
loc = st.text_input("Location", placeholder="A beautiful place")
num_days = st.slider("Forecast Days",min_value=1, max_value=5, help="Select the number of days you want to forecast")
forecast_opt = st.selectbox("Data to view",('Temperature','Visibility'), help="Choose the temperature in °C or The visibility and sky conditions")

placeholder = st.empty()
placeholder.subheader("Forecast will apply once you submit your location!")
if loc is not '':
    placeholder.empty()
    if num_days > 1:
        placeholder.subheader(f"{forecast_opt} for the next {num_days} days in {loc.title()}")
    else:
        placeholder.subheader(f"{forecast_opt} for the next day in {loc.title()}")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['col1', 'col2', 'col3'])

    st.line_chart(
        chart_data,
        x = 'col1',
        y = ['col2', 'col3']
    )