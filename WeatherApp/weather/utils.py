from datetime import datetime

import requests


def get_json(url) -> dict | None:
	json = None
	try:
		response = requests.get(url)
		response.raise_for_status()
		json = response.json()
	except requests.exceptions.HTTPError as e:
		print(e)
	except requests.excpetions.Timeout as e:
		print(e)
	return json


def get_weather_info(data: dict) -> dict:
	weather_info = {}
	try:
		weather_info['temp_min'] = data['main']['temp_min']
		weather_info['temp_max'] = data['main']['temp_max']
		weather_info['temp'] = data['main']['temp']
		weather_info['visibility'] = data['visibility']
		weather_info['wind_speed'] = data['wind']['speed']
		weather_info['clouds'] = data['clouds']['all']
		weather_info['sunrise'] = datetime.fromtimestamp(data['sys']['sunrise']).time()
		weather_info['sunset'] = datetime.fromtimestamp(data['sys']['sunset']).time()
		weather_info['city'] = data['name']
	except KeyError as e:
		print(f"Missing key in JSON data: {e}")
	return weather_info
