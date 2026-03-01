#!/usr/bin/env python3

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


print("\n---\n")


i = 0
while i < 6:
    i += 1
    if i == 3:
        break
    print(i)
