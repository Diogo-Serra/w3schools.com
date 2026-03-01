#!/usr/bin/env python3


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

print("\n")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
