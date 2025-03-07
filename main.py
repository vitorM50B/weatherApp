from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "b69bec2b622000d8c55417a830f7c68a" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    print(f"Fetching weather for: {city}") 
    print(f"Request URL: {BASE_URL} with {params}")  

    response = requests.get(BASE_URL, params=params)
    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {response.text}") 
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return {"error": "City not found"}
