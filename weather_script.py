# Fetch weather data from OpenWeatherMap API
import requests
def fetch_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}
# Example usage
if __name__ == "__main__":
    API_KEY = "049e5b9c80e418f542fef3e7cc75e192"  # Replace with your OpenWeatherMap API key
    CITY = "London"  # Replace with the city you want to check
    weather_data = fetch_weather(API_KEY, CITY)
    print(weather_data) # Note: Make sure to install the requests library if you haven't already
