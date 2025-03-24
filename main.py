key= "917f3e81cdc041caaf674930252103"
import requests
respond = requests.get("http://api.weatherapi.com/v1/forecast.json?key=917f3e81cdc041caaf674930252103&q=Liepaja&days=4&aqi=yes&alerts=yes")
data = respond.json()
#print(data)

maxtemp = data["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
print(maxtemp)



