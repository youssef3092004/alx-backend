#!/usr/bin/python3
"""
Basic Cache implementation Class with FIFO (First-In-First-Out)
replacement policy.

This module defines a FIFOCache class that inherits from BaseCaching.
The cache stores items up to a specified limit (MAX_ITEMS). If the cache
exceeds this limit, it removes the oldest added item first (FIFO policy).
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherits from BaseCaching and implements a
    First-In-First-Out caching mechanism.
    """

    def __init__(self):
        """
        Initialize the FIFO cache system.

        Attributes:
        - order: A list to keep track of the order of inserted keys for
          efficient removal of the oldest item when capacity is exceeded.
        """
        super().__init__()
        self.order = []  # Keeps the order of cache keys

    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds MAX_ITEMS, remove
        the oldest item in the cache (FIFO).

        Parameters:
        - key: The key associated with the item to be added (cannot be None).
        - item: The item to be stored in the cache (cannot be None).

        Behavior:
        - If the key and item are valid, store the item in cache_data and
          add the key to the order list.
        - If the number of items in cache_data exceeds MAX_ITEMS, discard the
          oldest entry in cache_data, as per FIFO, and log the discarded item.
        """
        if key is not None and item is not None:
            self.order.append(key)
            self.cache_data[key] = item

            # Remove the oldest item if the cache exceeds the limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Parameters:
        - key: The key associated with the item to retrieve.

        Returns:
        - The item if it exists in cache_data, or None if the key is None
          or the key is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
