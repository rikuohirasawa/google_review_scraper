from firebase_admin import credentials, db
import firebase_admin
from datetime import datetime

cred = credentials.Certificate('/Users/Rikuo/Desktop/google_review_scraper-1/server/mxpert-reviews-firebase-adminsdk-l1xld-a440394582.json')

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mxpert-reviews-default-rtdb.firebaseio.com/'
})
date = datetime.today()

date_dict = {
        f'{date.year}-{date.month}-{date.day}': 'success'
    }
db.reference('/dates').set(date_dict)


# dates = db.reference("/dates").update({'test': 'success'})
# print(db.reference("/dates").get())