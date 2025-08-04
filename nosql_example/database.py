from pymongo import MongoClient

client = MongoClient("mongodb://root:toor@localhost:27017/")
database = client.mydatabase

user_collection = database["users"]
