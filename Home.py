import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from backend import get_data
import os


st.set_page_config(page_title="Weather Forecast", layout="centered", page_icon="🌦️")


st.title("Dynamic Weather Forecast")
loc = st.text_input("Location", placeholder="A beautiful place")
num_days = st.slider("Forecast Days",min_value=1, max_value=5, help="Select the number of days you want to forecast")
forecast_opt = st.selectbox("Data to view",('Temperature','Visibility'), help="Choose the temperature in °C or The visibility and sky conditions")

placeholder = st.empty()
placeholder.subheader("Forecast will apply once you submit your location!")

if loc != '':
    placeholder.empty()
    if num_days > 1:
        placeholder.subheader(f"{forecast_opt} for the next {num_days} days in {loc.title()}")
    else:
        placeholder.subheader(f"{forecast_opt} for the next day in {loc.title()}")

    data = get_data(loc, num_days, forecast_opt)
    
    d, t = get_data(num_days)

    figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature °C"})
    st.plotly_chart(figure)