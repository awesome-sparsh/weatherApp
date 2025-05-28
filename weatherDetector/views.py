from django.shortcuts import render
import json
import urllib.request
import urllib.error
import socket

def index(request):
    if request.method=='POST':
        location = request.POST.get('location', '')     
        encoded_location = urllib.parse.quote(location)   
        url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_location}&APPID=53b519362c30616fca5d5102e899cbf1&units=metric'
        try:
            response = urllib.request.urlopen(url).read()
            jsonData = json.loads(response)
            weather_data = {
                "location" : location,
                "coordinates" :str(jsonData['coord']['lon']) + ", " + str(jsonData['coord']['lat']),
                "temperature" :str(jsonData['main']['temp']),
                "feels_like_temperature" :str(jsonData['main']['feels_like']),
                "minimum_temperature" :str(jsonData['main']['temp_min']),
                "maximum_temperature" :str(jsonData['main']['temp_max']),
                "humidity" :str(jsonData['main']['humidity']),
                "visibility" :str(jsonData['visibility']),
                "wind" :str(jsonData['wind']['speed']),
                "sunrise" :str(jsonData['sys']['sunrise']),
                "sunset" :str(jsonData['sys']['sunset']),
                "timezone" :str(jsonData['timezone']),
                "status" :str("success")
            }
        except urllib.error.URLError as e:
            if isinstance(e.reason, TimeoutError) or isinstance(e.reason, socket.timeout):
                # Handle timeout / connection failure specifically
                weather_data = {
                    "location": location,
                    "status": "server_fail"
                }
            else:
                weather_data = {
                    "location": location,
                    "status": "location_fail"
                }
        except Exception as ex:
            weather_data = {
                "location": location,
                "status": "server_fail"
            }
    else:
        weather_data=''
    return render(request, 'index.html', {'weather_data': weather_data})
