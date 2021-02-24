import requests
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
response = requests.request('GET', "http://localhost:5000/trend_list")

l = response.json()

print(l)

for trend in l:

    with open(current_dir + '/storage/trends.json') as trends:
        for trend_dict in json.load(trends):
            if trend_dict["name"] == trend:
                trend = trend_dict
                break
    print(trend["query"])
    requests.get("http://localhost:5000/analyze_trend?trend=" + trend["query"])
    