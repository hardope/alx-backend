#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> BasicCache = __import__('0-basic_cache').BasicCache
>>> my_cache = BasicCache()
>>> my_cache.print_cache()
Current cache:

>>> my_cache.put("A", "Hello")
>>> my_cache.put("B", "World")
>>> my_cache.put("C", "Holberton")
>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
C: Holberton

>>> print(my_cache.get("A"))
Hello

>>> print(my_cache.get("B"))
World

>>> print(my_cache.get("C"))
Holberton

>>> print(my_cache.get("D"))
None

>>> my_cache.print_cache()
Current cache:
A: Hello
B: World
C: Holberton

>>> my_cache.put("D", "School")
>>> my_cache.put("E", "Battery")
>>> my_cache.put("A", "Street")
>>> my_cache.print_cache()
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery

>>> print(my_cache.get("A"))
Street

"""
