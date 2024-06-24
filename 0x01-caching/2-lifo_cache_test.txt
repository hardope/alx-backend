#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> LIFOCache = __import__('2-lifo_cache').LIFOCache
>>> my_cache = LIFOCache()
>>> my_cache.put("A", "Hello")
>>> my_cache.put("B", "World")
>>> my_cache.put("C", "Holberton")
>>> my_cache.put("D", "School")
>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
C: Holberton
D: School

>>> my_cache.put("E", "Battery")
DISCARD: D

>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
C: Holberton
E: Battery

>>> my_cache.put("C", "Street")
>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
C: Street
E: Battery

>>> my_cache.put("F", "Mission")
DISCARD: C

>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
E: Battery
F: Mission

>>> my_cache.put("G", "San Francisco")
DISCARD: F

>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco

"""
