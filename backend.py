import os
import requests

weather_api_key = os.getenv('WEATHER_API_KEY')

def get_data(location, forecast_days):
    """Weather forecast for 5 days with data every 3 hours by city name. 8 data points per day."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()
    
    forecast_days = int(forecast_days) * 8

    if data['cod'] == '404':
        print("Invalid Location Provided")
        return "Invalid Location Provided"

    else:
        filtered_data = data['list']
        filtered_data = filtered_data[:forecast_days]

    return filtered_data

if __name__ == "__main__":
    data = get_data(location="New York", forecast_days=2)
    print(data)
