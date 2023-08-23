#!/usr/bin/env python3
"""LRU Cache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The Basic Class of LRUCache"""
    def __init__(self):
        """class LRU Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Funtion that adds an item to the Cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_key = self.order.pop(0)
            self.cache_data.pop(removed_key)
            print("DISCARD:", removed_key)
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
