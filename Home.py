import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from backend import get_data


st.set_page_config(page_title="Weather Forecast", layout="centered", page_icon="🌦️")


st.title("Dynamic Weather Forecast")
loc = st.text_input("Location", placeholder="A beautiful place")
num_days = st.slider("Forecast Days",min_value=1, max_value=5, help="Select the number of days you want to forecast")
forecast_opt = st.selectbox("Data to view",('Temperature','Visibility'), help="Choose the temperature in °C or The visibility and sky conditions")

placeholder = st.empty()
placeholder.info("Forecast will apply once you submit your location!")

if loc:
    placeholder.empty()
    try:
        if num_days > 1:
            placeholder.subheader(f"{forecast_opt} for the next {num_days} days in {loc.title()}")
        else:
            placeholder.subheader(f"{forecast_opt} for the next day in {loc.title()}")

        filtered_data = get_data(loc, num_days)

        if filtered_data != "Invalid Location Provided":
            dates = [dict["dt_txt"] for dict in filtered_data]

        if forecast_opt == "Temperature":
            temp_data_over_time = [round(dict['main']['temp'] - 273.15, 1) for dict in filtered_data]
            
            figure = px.line(x=dates, y=temp_data_over_time, labels={"x":"Date", "y":"Temperature °C"})
            st.plotly_chart(figure)


        if forecast_opt == "Visibility":
            vis_data_over_time = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {"Clear": "visibility_images/clear.png",
                    "Clouds": "visibility_images/cloud.png",
                    "Rain": "visibility_images/rain.png",
                    "Snow": "visibility_images/snow.png"}
            
            vis_image_paths = [images[condition] for condition in vis_data_over_time]
            st.image(vis_image_paths, width=115, caption=dates)
    
    except KeyError:
        placeholder.warning("Invalid Location provided!", icon="⚠️")

    except TypeError:
        placeholder.warning("Invalid Location provided!", icon="⚠️")
    
    except Exception as e:
        placeholder.warning("An error has occured, this has been reported internally. Please wait for this to be addressed.", icon="❗️")
        print(f"Error, likely an invalid response/ API timeout\nError: {e}")