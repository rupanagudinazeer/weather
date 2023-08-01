import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"  # Replace with the actual API URL

def get_weather(date):
    params = {
        "location": "London",
        "date": date
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    temperature = data["temperature"]
    print(f"The temperature on {date} is {temperature}°C")

def get_wind_speed(date):
    params = {
        "location": "London",
        "date": date
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    wind_speed = data["wind"]["speed"]
    print(f"The wind speed on {date} is {wind_speed} m/s")

def get_pressure(date):
    params = {
        "location": "London",
        "date": date
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    pressure = data["pressure"]
    print(f"The pressure on {date} is {pressure} hPa")

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_weather(date)
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_wind_speed(date)
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            get_pressure(date)
        elif option == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
