import json
import firebase_admin
from firebase_admin import db, credentials
 
cred = credentials.Certificate('./firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mxpert-reviews-default-rtdb.firebaseio.com/'
})

def lambda_handler(event, context):
    try:
        data = db.reference(event['garage']).get()
        return {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
        }
    except:
        return {
            'statusCode': 500,
            'body': 'ERROR',
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello Lambda!')
    # }
