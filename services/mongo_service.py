from pymongo import MongoClient

from config.settings import settings

client = MongoClient(
    settings.MONGO_URI
)

db = client[settings.DB_NAME]

reviews = db["reviews"]

def save_review(data):

    reviews.insert_one(data)