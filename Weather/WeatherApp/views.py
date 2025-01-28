from django.shortcuts import render
import requests
import datetime
import json
from django.contrib import messages

# Create your views here.


def Weather(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "Chandigarh"

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"YourAPIKEY"}'
    PARAMS = {'units':'metric'}

    data = requests.get(url, PARAMS).json()

    description = data.get('weather', [{}])[0].get('description', 'No description available')
    icon = data.get('weather', [{}])[0].get('icon', 'No icon available')
    temperature = data.get('main', {}).get('temp')

    # day = datetime.date.today()
    time = datetime.datetime.now()

    return render(request, 'weather.html',{'city':city,'description':description, 'icon':icon, 'temp':temperature, 'time':time})
