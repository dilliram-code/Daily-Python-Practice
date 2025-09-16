import requests

API_KEY = "ca183214c2f4a0b88e9459245a1753fb"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name:")
url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
# print(data)

if data["cod"] == 200:
    main = data["main"]
    temp = main["temp"]
    humidity = main["humidity"]
    weather = data["weather"][0]["description"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
else:
    print("City not found.")
