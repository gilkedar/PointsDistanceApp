from utils.cache import LocalCache
from utils.mongo_db import MongoDb


class DbManager:

    def __init__(self, item_type):
        self.item_type = item_type
        self._cache = LocalCache()
        self._remote = MongoDb()

    def insert(self, item):
        if type(item) != self.item_type:
            return None
        id = self._remote.insert(item.toJSON())
        self._cache.insert(id, item)
        return id

    def get(self, id):
        item = self._cache.get(id)
        if not item:
            item = self._remote.get(id)
        return item


