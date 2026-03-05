import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

# Use your existing service key
if not firebase_admin._apps:
    cred = credentials.Certificate("service-key.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://delhi-aqi-6ed7a-default-rtdb.firebaseio.com/'
    })

# Point to the 'environment' node seen in your image
ref = db.reference('environment/historical_data')

df = pd.read_csv("Cleaned_AshokVihar.csv")

# Upload the data
for index, row in df.head(100).iterrows():
    ref.push(row.to_dict())
print("Historical data linked to Realtime Database!")