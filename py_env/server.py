from flask import Flask, request, jsonify
from flask_cors import CORS
from google_scraper import launchChrome

app = Flask(__name__)
CORS(app)

@app.route('/api/get-reviews', methods=['GET'])
def get_reviews():
    response = jsonify(launchChrome())
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)