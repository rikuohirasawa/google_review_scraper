from flask import Flask, request, jsonify
from flask_cors import CORS
from google_scraper import launchChrome, db_get

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return ('hello world')

@app.route('/api/get-reviews', methods=['GET'])
def get_reviews():
    response = jsonify(launchChrome())
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/garage-reviews', methods=['GET'])
def garage_reviews():
    ref = request.args.get('ref')
    response = jsonify(db_get(ref))
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()