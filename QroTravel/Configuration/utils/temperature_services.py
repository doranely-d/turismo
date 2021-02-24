from Configuration.models import Home
from django.utils import translation

import json
import urllib2

def load_temperature():
    try:
        translation.activate('es')
        configuration = Home.objects.get()
        response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily/?q=Queretaro,mx&appid=27ac04c3816a475a0625ede791c6dac4&units=metric&cnt=1')
        aux = json.load(response)
        configuration.min_temp = str(int(round(aux['list'][0]['temp']['min'])))
        configuration.max_temp = str(int(round(aux['list'][0]['temp']['max'])))
        configuration.weather_icon = str(aux['list'][0]['weather'][0]['icon'])
        configuration.save()
    except Exception as e:
        print 'ERROR', e
        pass
