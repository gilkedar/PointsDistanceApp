import pymongo
from utils import config
from bson.objectid import ObjectId


class MongoDb:

    def __init__(self):
        self.client = pymongo.MongoClient(config.MONGO_URL)
        self.db = self.client[config.MONGO_DB_NAME]
        self.collection = self.db[config.MONGO_COLLECTION_NAME]

    def insert(self, data):
        x = self.collection.insert_one(data)
        return x.inserted_id

    def get(self, id):
        query = {"_id": ObjectId(id)}
        ans = self.collection.find_one(query)
        return ans
