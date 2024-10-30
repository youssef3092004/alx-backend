#!/usr/bin/python3
"""LIFO Cache implementation class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.

    This caching system follows the Last-In-First-Out (LIFO) replacement policy,
    where the most recently added item is the first to be discarded when the cache
    reaches its maximum capacity.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance, including the order list for
        tracking the insertion order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache, applying LIFO replacement if cache exceeds capacity.

        If the cache size exceeds `MAX_ITEMS`, the last recently added item
        before the new one is discarded following the LIFO policy.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            The item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
