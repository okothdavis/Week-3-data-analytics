import requests
import pandas as pd
from datetime import datetime

API_KEY = '287f91e2115f4378829180513241510'  # Replace with your weather API key
CITIES = ['Nairobi', 'Mombasa', 'Kisumu', 'Eldoret', 'Nakuru', 'Garissa', 'Turkana']  # List of cities to fetch data for

# Base URL for the Weather API
base_url = "https://api.weatherapi.com/v1/current.json"

# List to store weather data for all cities
weather_data_list = []

# Loop through each city and get the weather data
for city in CITIES:
    # Construct the API request URL
    url = f"{base_url}?key={API_KEY}&q={city}"
    
    # Send GET request to the API
    response = requests.get(url)
    
    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        
        # Check if the 'location' and 'current' data exist in the response
        if 'location' in data and 'current' in data:
            city_name = data['location']['name']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            pressure = data['current']['pressure_mb']
            wind_speed = data['current']['wind_kph'] / 3.6  # Convert kph to m/s
            weather_description = data['current']['condition']['text']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Store the city's weather data in a dictionary
            city_weather_data = {
                'City': city_name,
                'Temperature (C)': temperature,
                'Humidity (%)': humidity,
                'Pressure (hPa)': pressure,
                'Wind Speed (m/s)': wind_speed,
                'Weather Description': weather_description,
                'Timestamp': timestamp
            }
            
            # Append the city's data to the list
            weather_data_list.append(city_weather_data)
    else:
        print(f"Failed to get data for {city}, Status Code: {response.status_code}")

# Convert the list of weather data to a Pandas DataFrame
if weather_data_list:
    weather_df = pd.DataFrame(weather_data_list)
    
    # Save the DataFrame to a CSV file
    weather_df.to_csv("weather_data.csv", index=False)
    
    print("Weather data saved as weather_data.csv")
else:
    print("No data to save")
