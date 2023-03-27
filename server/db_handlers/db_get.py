from firebase_admin import credentials, db
import firebase_admin

# cred = credentials.Certificate('firebase_credentials.json')

# default_app = firebase_admin.initialize_app(cred, {
  #   'databaseURL': 'https://mm-scraper-db-1f403-default-rtdb.firebaseio.com/'
# })

def db_get(ref):
    return db.reference(ref).get()

# print(db_get('/kings_bridge_auto'))
