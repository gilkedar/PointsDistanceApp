import threading
from collections import OrderedDict


class LocalCache:
    """
    implement only simple lru cache using orderedDict for simplicity of running and debugging
    for production would use redis caching mechanism
    """
    def __init__(self, max_size=500):
        self.max_size = max_size
        self._db = OrderedDict()
        self.lock = threading.Lock()

    def insert(self, id, item):
        with self.lock:
            self._db[id] = item
            self._db.move_to_end(id)
            if len(self._db) > self.max_size:
                self._db.popitem(last=False)

    def get(self, id):
        with self.lock:
            if id not in self._db:
                return None
            else:
                self._db.move_to_end(id)
                return self._db[id]
