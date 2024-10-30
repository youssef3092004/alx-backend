#!/usr/bin/python3
''' MRU Cache '''
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    ''' MRU Cache class '''

    def __init__(self):
        ''' Constructor '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Add an item in the cache '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recently_used = self.order.pop()
                print(f"DISCARD: {most_recently_used}")
                del self.cache_data[most_recently_used]

    def get(self, key):
        ''' Get an item by key '''
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
