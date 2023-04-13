import requests
import json
import datetime
import time


main_url = "http://localhost:5000/"
sub_url = "data"
URL = main_url + sub_url

r = requests.get(url=URL).text
response = json.loads(r)
print(response)
sub_url = "data_post"
URL = main_url + sub_url


for i in range(10):
    now = json.dumps(datetime.datetime.now(), default=str)
    payload = [{"id":"status", "stolen":False, "id": "location", "lat": 0, "lon": 0, "elev": 0, "time":now}]
    r_2 = requests.put(URL, json=payload).text
    print(r_2)
    time.sleep(1)
