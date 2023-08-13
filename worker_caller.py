from celery_worker import get_weather_data
import time

if __name__ == '__main__':
    while True:
        get_weather_data.delay()
        time.sleep(10)
