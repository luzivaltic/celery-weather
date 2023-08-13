from celery import Celery
import requests
import time
from celery.schedules import crontab
from datetime import timedelta

app = Celery('weather_worker', broker='redis://redis-server:6379/0')

@app.task
def get_weather_data():
    api_key = "bf086ec77e2c49bf82d104748231208"
    city = "Hanoi"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        # time.sleep(20)
        print(f"Weather in {city}: {temperature}°C, {condition}")
    else:
        print("Failed to fetch weather data.")


app.conf.beat_schedule = {
    'new-weather-each-10-seconds' : {
        'task': 'celery_worker.get_weather_data',
        'schedule': timedelta(seconds=10),  
    },
}