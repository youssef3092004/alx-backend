#!/usr/bin/python3
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFU cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_count = min(self.count.values())
                keys = [k for k in self.count if self.count[k] == min_count]
                if len(keys) == 1:
                    del self.cache_data[keys[0]]
                    del self.count[keys[0]]
                    print(f"DISCARD: {keys[0]}")
                else:
                    for k in self.keys:
                        if k in keys:
                            del self.cache_data[k]
                            del self.count[k]
                            print(f"DISCARD: {k}")
                            break
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.count[key] = 0
            for k in self.count:
                self.count[k] += 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.count[key] += 1
        return self.cache_data[key]
