import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#creating variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
#recording data in file name"datafile.txt"
with open("datafile.txt", "a") as f:
    f.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\nTemp: {}".format(str(temp_city)))
    f.write("\nWeather Desc: {} ".format(str(weather_desc)))
    f.write("\nHumidity: {} ".format(str(hmdt)))
    f.write(str("\nWind Speed: {} ".format(wind_spd)))
    f.close()

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print ("-----------------------------------------------------------")
#opening file
print ("-------------Opening 'Datafile.txt'----------")
with open("datafile.txt", "r" ) as h:
    print(h.read())
