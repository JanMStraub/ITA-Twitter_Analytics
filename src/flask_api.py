from flask import Flask
from flask_cors import CORS
from main import main
app = Flask(__name__)
CORS(app)

# need env var : export FLASK_APP=/path/to/flask_api.py

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    print("You are doing great! :)")