#!/usr/bin/python3
""" MRU Cache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache class that inherits from BaseCaching. """

    def __init__(self):
        """ Constructor for the MRUCache class. """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache. """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]

    def get(self, key):
        """ Get an item by key. """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]
