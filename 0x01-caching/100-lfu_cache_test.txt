#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> LFUCache = __import__('100-lfu_cache').LFUCache
>>> my_cache = LFUCache()
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

>>> print(my_cache.get("A"))
None

>>> print(my_cache.get("B"))
World

>>> print(my_cache.get("C"))
Street

>>> my_cache.put("F", "Mission")
DISCARD: D

>>> my_cache.print_cache()
Current cache:
B: World
C: Street
E: Battery
F: Mission

>>> my_cache.put("G", "San Francisco")
DISCARD: E

>>> my_cache.print_cache()
Current cache:
B: World
C: Street
F: Mission
G: San Francisco

>>> my_cache.put("H", "H")
DISCARD: F

>>> my_cache.print_cache()
Current cache:
B: World
C: Street
G: San Francisco
H: H

>>> my_cache.put("I", "I")
DISCARD: G

>>> my_cache.print_cache()
Current cache:
B: World
C: Street
H: H
I: I

>>> print(my_cache.get("I"))
I

>>> print(my_cache.get("H"))
H

>>> print(my_cache.get("I"))
I

>>> print(my_cache.get("H"))
H

>>> print(my_cache.get("I"))
I

>>> print(my_cache.get("H"))
H

>>> my_cache.put("J", "J")
DISCARD: B

>>> my_cache.print_cache()
Current cache:
C: Street
H: H
I: I
J: J

>>> my_cache.put("K", "K")
DISCARD: J

>>> my_cache.print_cache()
Current cache:
C: Street
H: H
I: I
K: K

>>> my_cache.put("L", "L")
DISCARD: K

>>> my_cache.print_cache()
Current cache:
C: Street
H: H
I: I
L: L

>>> my_cache.put("M", "M")
DISCARD: L

>>> my_cache.print_cache()
Current cache:
C: Street
H: H
I: I
M: M

"""
