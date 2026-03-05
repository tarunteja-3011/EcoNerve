import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# 1. Connect to Firebase using your secret key
cred = credentials.Certificate("service-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. Load your newly cleaned data
df = pd.read_csv("Cleaned_AshokVihar.csv")

# 3. Upload to Firebase
# We will upload the first 500 rows to make sure it works perfectly
collection_name = "delhi_aqi_data"
print("Starting upload to Firebase...")

for index, row in df.iterrows():
    # Convert row to a dictionary
    data = row.to_dict()
    # Firestore works best with strings or timestamps for dates
    data['Date'] = str(data['Date'])
    
    # Add to the 'delhi_aqi_data' collection
    db.collection(collection_name).add(data)

print(f"Success! 500 rows uploaded to the '{collection_name}' collection.")