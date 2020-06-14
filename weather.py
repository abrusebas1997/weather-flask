import requests, json

key = "d26252a76d0ae9c37b097c87d64c1e77"
weather_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name : ")
url = weather_url + "appid=" + key + "&q=" + city + "&units=metric"

res = requests.get(url)

formatted = res.json()
print("-----------------")
if res.status_code != 404:
	current = formatted["main"]
	currtemp = current["temp"]
	currpressure = current["pressure"]
	currhumidity = current["humidity"]
	describe = formatted["weather"]
	description = describe[0]["description"]

	print(f"temperature: {currtemp}°C\npressure: {currpressure} hPa\nhumidity: {currhumidity}%\ndescription: {description}")
else:
	print(" 404 - city was not found ")

print("-----------------")
your_mood = input("What mood does this weather make you feel? ")
print(f"I'd also feel {your_mood} if the temperature was {currtemp}°C")
print("-----------------")

def weather_here():
    ur_city = city
    tha_weather = f"temperature: {currtemp}°C   ||   pressure: {currpressure} hPa   ||   humidity: {currhumidity}%   ||   description: {description}"
    my_mood = f"I'd also feel {your_mood} if the temperature was {currtemp}°C"
    return "City: " + city + "   ||   " + "Weather: " + tha_weather + "   ||   " + "Mood: " + my_mood
