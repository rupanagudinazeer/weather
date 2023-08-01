import requests

API_ENDPOINT = "https://samples.openweathermap.org/data/2.5/forecast/hourly?appid=b6907d289e10d714a6e88b30761fae22"

def get_weather(date):
    response = requests.get(API_ENDPOINT, params={"q": f"London,us&dt={date}"})
    data = response.json()
    temperature = data["list"][0]["main"]["temp"]
    return temperature

def get_wind_speed(date):
    response = requests.get(API_ENDPOINT, params={"q": f"London,us&dt={date}"})
    data = response.json()
    wind_speed = data["list"][0]["wind"]["speed"]
    return wind_speed

def get_pressure(date):
    response = requests.get(API_ENDPOINT, params={"q": f"London,us&dt={date}"})
    data = response.json()
    pressure = data["list"][0]["main"]["pressure"]
    return pressure

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather(date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature} degrees Celsius.")
            else:
                print("No data available for the given date.")
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} km/h.")
            else:
                print("No data available for the given date.")
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
            else:
                print("No data available for the given date.")
        elif option == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
