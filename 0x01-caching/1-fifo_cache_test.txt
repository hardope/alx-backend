#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> FIFOCache = __import__('1-fifo_cache').FIFOCache
>>> my_cache = FIFOCache()
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
DISCARD: A

>>> my_cache.print_cache()
Current cache:
B: World
C: Holberton
D: School
E: Battery

>>> my_cache.put("C", "Street")
>>> my_cache.print_cache()
Current cache:
B: World
C: Street
D: School
E: Battery

>>> my_cache.put("F", "Mission")
DISCARD: B

>>> my_cache.print_cache()
Current cache:
C: Street
D: School
E: Battery
F: Mission

>>> print(my_cache.get(None))
None

>>> print(my_cache.get("microsoft_build"))
None

"""
