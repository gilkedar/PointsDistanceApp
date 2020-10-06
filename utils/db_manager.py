from utils.redis_cache import RedisCache
from utils.mongo_db import MongoDb

class DbManager:

    def __init__(self, item_type):
        self.item_type = item_type
        self._cache = RedisCache()
        self._remote = MongoDb()

    def insert(self):
        pass

    def get(self):
        pass
