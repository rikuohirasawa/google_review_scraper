from flask import Flask, request, jsonify
from flask_cors import CORS
from google_scraper import launchChrome
from db_handlers.db_get import db_get
import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate('firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mm-scraper-db-1f403-default-rtdb.firebaseio.com/'
})

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
