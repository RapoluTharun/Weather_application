import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Metric units for temperature in Celsius
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    elif response.status_code == 404:
        print("City not found. Please check the name and try again.")
    else:
        print("An error occurred. Please try again later.")

def main():
    print("Welcome to the Weather App!")
    api_key = "  "  # OpenWeatherMap API key
    city = input("Enter the name of a city: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
