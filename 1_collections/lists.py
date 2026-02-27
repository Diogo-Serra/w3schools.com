#!/usr/bin/env python3

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

print("All set")

thislist = ["Apple", "banana", "Cherry"]
print(thislist)

thislist = ["Apple", "Apple"]
print(thislist)

print(len(thislist))

list1 = ["abc", 35, True, 40, "Male"]
print(list1)

print(type(list1))

thislist = list(("apple", "Apple"))
print(thislist)

print(thislist[0])
print(thislist[-1])
