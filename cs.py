import urllib.request
import os
import requests
from datetime import date, timedelta

start_date = date(2020, 1, 22)
end_date = date(2020, 2, 4)

delta = timedelta(days=1)

while start_date <= end_date:
    # print(start_date.strftime("%Y-%m-%d"))
    key = 'UGp6h5TuBUbehJfCYqfQEuGbW8yk0932H4C1SkTC'
    params = {
        'date': start_date.strftime("%Y-%m-%d"),
        'hd': True,
        "api_key": key
    }
    r = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    r = r.json()
    urllib.request.urlretrieve(
        r['hdurl'], start_date.strftime("%Y-%m-%d")+'.jpg')
    print(r['date'], r['title'])
    start_date += delta
