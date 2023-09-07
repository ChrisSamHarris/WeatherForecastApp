import os
import requests
import json
import datetime

weather_api_key = os.getenv('WEATHER_API_KEY')

def get_data(location, forecast_days, kind=None):
    """Weather forecast for 5 days with data every 3 hours by city name. 8 data points per day."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()

    forecast_days = int(forecast_days) * 8
    filtered_data = data['list']
    filtered_data = filtered_data[:forecast_days]

    # date_time = datetime.datetime.fromtimestamp(data['list'][0]['dt'])  
    # print(data['list'][0]['dt'])
    # print(str(date_time)[:10])

    human_readable_data = json.dumps(data, indent =4 )

    if kind == "Temperature":
        filt_data_over_set_time = [dict['main']['temp'] for dict in filtered_data]
    
    if kind == "Visibility":
        filt_data_over_set_time = [dict['weather'][0]['main'] for dict in filtered_data]
    
    print(filt_data_over_set_time)
    return filt_data_over_set_time

if __name__ == "__main__":
    get_data(location="Manchester", forecast_days=3, kind="Visibility")