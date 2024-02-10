from datetime import datetime
import requests


def get_json(url) -> dict | None:
	response = requests.get(url)
	json = response.json()
	if str(json['cod'])[0] in ('4', '5'):
		return None
	return json


def get_weather_info(data: dict) -> dict:
	context = {}
	context['temp_min'] = data['main']['temp_min']
	context['temp_max'] = data['main']['temp_max']
	context['temp'] = data['main']['temp']
	context['visibility'] = data['visibility']
	context['wind_speed'] = data['wind']['speed']
	context['clouds'] = data['clouds']['all']
	context['sunrise'] = datetime.fromtimestamp(data['sys']['sunrise']).time()
	context['sunset'] = datetime.fromtimestamp(data['sys']['sunset']).time()
	context['city'] = data['name']
	return context
