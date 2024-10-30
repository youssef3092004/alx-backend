#!/usr/bin/python3
"""LRU Cache implementation class"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.

    This class implements a Least Recently Used (LRU) caching system.
    It allows items to be added, retrieved, and automatically removes
    the least recently used item when the cache exceeds the maximum limit.
    """

    def __init__(self):
        """
        Initialize the LRUCache instance.

        This method initializes the parent class and creates an empty list
        to keep track of the order in which keys are used.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the key or item is None, this method does nothing. If the cache
        exceeds the maximum number of items defined in BaseCaching, it will
        discard the least recently used item.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    LRU_element = self.order.pop(0)
                    print(f"DISCARD: {LRU_element}")
                    del self.cache_data[LRU_element]
                self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by its key.

        If the key is None or does not exist in the cache, it returns None.
        If the key is found, it updates the order to mark it as recently used.

        Args:
            key (str): The key of the item to be retrieved.

        Returns:
            The item associated with the key if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
