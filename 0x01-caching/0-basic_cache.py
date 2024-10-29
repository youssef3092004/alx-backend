from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.

    This class is a basic implementation of a caching system where items can be added
    to the cache and retrieved from the cache.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
        else:
            return self.cache_data[key]
