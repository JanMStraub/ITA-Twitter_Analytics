from flask import Flask, request, send_from_directory
from main import main
from flask_cors import CORS
import json

app = Flask(__name__,
            static_url_path='', 
            static_folder='../storage/results')
CORS(app)

@app.route('/init_analysis')
def init_analysis():
    trends = ["trend1", "trend2", "trend3"]
    # call main
    return json.dumps(trends)



@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../storage/results', path)

if __name__ == "__main__":
    send_png()