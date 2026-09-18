from pymongo import AsyncMongoClient
import os

from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URI")

client = AsyncMongoClient(mongo_url)

database = client["smartspend"]

user_collection = database["users"]