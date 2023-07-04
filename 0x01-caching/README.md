# Caching

This project contains tasks for learning to cache data.

## Tasks To Complete

+ [x] 0. **Basic dictionary**<br/>[0-basic_cache.py](0-basic_cache.py) contains a Python class `BasicCache` that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + This caching system doesn't have limit.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to `key`.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.

+ [x] 1. **FIFO caching**<br/>[1-fifo_cache.py](1-fifo_cache.py) contains a Python class `FIFOCache` that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
    + If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
      + You must discard the first item put in cache (FIFO algorithm).
      + You must print `DISCARD: ` with the key discarded and following by a new line.
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to `key`.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.

+ [x] 2. **LIFO Caching**<br/>[2-lifo_cache.py](2-lifo_cache.py) contains a Python class `LIFOCache` that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
    + If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
      + You must discard the last item put in cache (LIFO algorithm).
      + You must print `DISCARD: ` with the `key` discarded and following by a new line.
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to key.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.

+ [x] 3. **LRU Caching**<br/>[3-lru_cache.py](3-lru_cache.py) contains a Python class `LRUCache` that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
    + If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
      + You must discard the least recently used item (LRU algorithm).
      + You must print `DISCARD: ` with the `key` discarded and following by a new line.
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to `key`.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.

+ [x] 4. **MRU Caching**<br/>[4-mru_cache.py](4-mru_cache.py) contains a Python class `MRUCache` that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
    + If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
      + You must discard the most recently used item (MRU algorithm).
      + You must print `DISCARD: ` with the `key` discarded and following by a new line
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to `key`.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.

+ [x] 5. **LFU Caching**<br/>[100-lfu_cache.py](100-lfu_cache.py) contains a Python class LFUCache that inherits from [`BaseCaching`](base_caching.py) and is a caching system:
  + You must use `self.cache_data` - dictionary from the parent class [`BaseCaching`](base_caching.py).
  + You can overload `def __init__(self):` but don't forget to call the parent init: `super().__init__()`.
  + `def put(self, key, item):`:
    + Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
    + If `key` or `item` is `None`, this method should not do anything.
    + If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
      + You must discard the least frequency used item (LFU algorithm).
      + If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used.
      + You must print `DISCARD: ` with the `key` discarded and following by a new line.
  + `def get(self, key):`:
    + Must return the value in `self.cache_data` linked to `key`.
    + If `key` is `None` or if the `key` doesn't exist in `self.cache_data`, return `None`.
