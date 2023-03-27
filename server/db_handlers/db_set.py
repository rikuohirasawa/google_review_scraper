from firebase_admin import db

# cred = credentials.Certificate('firebase_credentials.json')

# default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://mm-scraper-db-1f403-default-rtdb.firebaseio.com/'
# })

def db_set(ref, data):
    try:
        db.reference(ref).set(data)
        print(f'db document {ref} updated')
    except Exception as err:
        print(type(err))
        print(err.args)
        print(err)
        