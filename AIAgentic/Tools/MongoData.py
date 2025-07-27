# Connect to MongoDB and run a query. Get the data in a DataFrame.
from pymongo import MongoClient
import pandas as pd

print("Connecting to MongoDB...")
client = MongoClient("mongodb://localhost:27017/")
db = client["product"]
collection = db["Sales"]

# Example function to retrieve data
def get_data():
    return list(collection.find({}))