from flask import Flask, request, send_from_directory
from flask_cors import CORS
import json
import os
from main import analyze_trend
from get_tweets import get_trends

app = Flask(__name__,
            static_url_path='',
            static_folder='../storage/results')
CORS(app)


# takes trendname and performs trend analysis
@app.route('/analyze_trend')
def analyze_trend_api():
    trend = request.args.get('trend')
    data = analyze_trend(trend)

    return json.dumps(data)


# return list of current top 50 trends
@app.route('/trend_list')
def trend_list():
    demo = request.args.get('demo')

    # return demo trends if site in demo mode := /trend_list?demo=True
    if demo == "True":
        with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/demo_trends.json', 'r') as file:
            trends = json.load(file)

        return json.dumps([item["name"] for item in trends])
    else:
        trends = get_trends()
        with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/trends.json', 'w') as file:
            json.dump(trends, file)

        return json.dumps([item["name"] for item in trends])


# makes files in /storage/results available via their name
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../storage/results', path)


if __name__ == "__main__":
    ...
