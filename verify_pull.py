import firebase_admin
from firebase_admin import credentials, firestore

# Use your key with the 'double' name since we know it works!
if not firebase_admin._apps:
    cred = credentials.Certificate("service-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Pull the most recent entry to prove it works
docs = db.collection("delhi_aqi_data").limit(1).get()

print("--- CLOUD DATA PULL SUCCESS ---")
for doc in docs:
    print(f"Data Retrieved from Firebase: {doc.to_dict()}")