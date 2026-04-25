import requests

def get_weather(city):
    API_KEY = 'b1dcad75438d36684bdf8fe61748b147'
    # URL = f'api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={API_KEY}'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = requests.get(URL)
        data = response.json()
        if response.status_code == 200:
            print(f"Weather in {data['name']}, {data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f" Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print(f"City not found. Please check and try again.")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)