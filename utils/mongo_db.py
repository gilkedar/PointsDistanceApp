import pymongo
from utils import config


class MongoDb:

    def __init__(self):
        self.client = pymongo.MongoClient(config.MONGO_URL)
        self.db = self.client[config.MONGO_DB_NAME]
        self.collection = self.db[config.MONGO_COLLECTION_NAME]

    def insert(self, data):
        x = self.collection.insert_one(data)
        return x.inserted_id

    def get(self, id):
        query = {"_id": id}
        ans = self.collection.find(query)
        return ans
