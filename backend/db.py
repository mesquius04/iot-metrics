import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017") # Default as specified in docker-compose

client = MongoClient(MONGO_URI)

db = client["iot_metrics_db"]

measurements_collection = db["measurements"]
