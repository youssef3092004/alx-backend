#!/usr/bin/env python3
""" LFU Cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class that inherits from BaseCaching. """

    def __init__(self):
        """ Constructor for the LFUCache class. """
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache. """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.count[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_count = min(self.count.values())
                    keys_to_discard = [
                        k for k in self.count if self.count[k] == min_count]
                    key_to_discard = keys_to_discard[0]
                    del self.cache_data[key_to_discard]
                    del self.count[key_to_discard]
                    print(f"DISCARD: {key_to_discard}")
                self.cache_data[key] = item
                self.count[key] = 1
                self.keys.append(key)

    def get(self, key):
        """ Get an item by key. """
        if key is None or key not in self.cache_data:
            return None
        self.count[key] += 1
        return self.cache_data[key]
