from flask import Flask, request, send_from_directory
from flask_cors import CORS
import json
import os
import requests
from main import analyze_trend
from get_tweets import get_trends

app = Flask(__name__,
            static_url_path='', 
            static_folder='../storage/results')
CORS(app)


@app.route('/analyze_trend')
def analyze_trend_api():
    trend = request.args.get('trend')
    data = analyze_trend(trend)

    return json.dumps(data)


@app.route('/trend_list')
def trend_list():
    trends = get_trends()
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../storage/trends.json', 'w') as file:
        json.dump(trends, file)
    
    return json.dumps([item["name"] for item in trends])


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../storage/results', path)


if __name__ == "__main__":
    ...