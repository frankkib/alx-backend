#!/usr/bin/env python3
"""Python caching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The basicCache class"""
    def put(self, key, item):
        """adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
