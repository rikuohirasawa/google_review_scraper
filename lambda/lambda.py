import json
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate('./firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mxpert-reviews-default-rtdb.firebaseio.com/'
})

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda!')
    }
