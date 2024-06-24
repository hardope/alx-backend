#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> MRUCache = __import__('4-mru_cache').MRUCache
>>> my_cache = MRUCache()
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

>>> print(my_cache.get("B"))
World

>>> my_cache.put("E", "Battery")
DISCARD: B

>>> my_cache.print_cache()
Current cache:
A: Hello
C: Holberton
D: School
E: Battery

>>> my_cache.put("C", "Street")
>>> my_cache.print_cache()
Current cache:
A: Hello
C: Street
D: School
E: Battery

>>> print(my_cache.get("A"))
Hello

>>> print(my_cache.get("B"))
None

>>> print(my_cache.get("C"))
Street

>>> my_cache.put("F", "Mission")
DISCARD: C

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
F: Mission

>>> my_cache.put("G", "San Francisco")
DISCARD: F

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco

>>> my_cache.put("H", "H")
DISCARD: G

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
H: H

>>> my_cache.put("I", "I")
DISCARD: H

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
I: I

>>> my_cache.put("J", "J")
DISCARD: I

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
J: J

>>> my_cache.put("K", "K")
DISCARD: J

>>> my_cache.print_cache()
Current cache:
A: Hello
D: School
E: Battery
K: K

"""
