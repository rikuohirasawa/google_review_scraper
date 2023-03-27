from datetime import datetime
from firebase_admin import db

def db_update_date(msg):
    date = datetime.today()
    date_dict = {
            f'{date.year}-{date.month}-{date.day}': msg
        }
    db.reference('/dates').set(date_dict)