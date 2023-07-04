#!/usr/bin/env python3
"""BaseCaching module.
"""


class BaseCaching():
    """BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initiliazes the cache.
        """
        self.cache_data = {}

    def print_cache(self):
        """Prints the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Adds an item in the cache.
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """Retrieves an item by key.
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
