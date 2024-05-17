# Simple Weather App 

## How to use

1. Install project with 
```
git clone https://github.com/KERELKO/Django-weather-app
```
2. Activate your virtual environment and install requirements,
example:
```
python3 -m venv venv
source venv/bin/activate
pip instal -r requirements.txt
```
3. Take your OpenWeather API key and put in the variable
that located in settings.py (./WeatherApp/WeatherApp/settings.py)
```
OPEN_WEATHER_API_KEY = 'your key'
```
4. Go to directory with manage.py and run
```
python manage.py runserver
```
5. In your browser go to **http://127.0.0.1:8000/weather** and you will see:
![image](https://github.com/KERELKO/Weather-App/assets/89779202/492c9079-7ccf-4a11-8920-e470db3b05e0)
![image](https://github.com/KERELKO/Weather-App/assets/89779202/1ecf27b6-a513-4e9e-8c0a-d353ecd243f1)
![image](https://github.com/KERELKO/Weather-App/assets/89779202/d004c70c-e5dd-498f-a4eb-417b629a5ef2)
