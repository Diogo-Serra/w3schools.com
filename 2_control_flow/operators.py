#!/usr/bin/env python3

a = 200
b = 42
c = 500
if a > b and c > a:
    print("Both true")

if a > b or a > c:
    print("At least 1 true")

if not a < b:
    print("a is NOT greater than b")
