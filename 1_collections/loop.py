#!/usr/bin/env python3

thislist = ["apple", "banana", "cherry"]
newlist = []
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

[print(x) for x in thislist]


for x in thislist:
    if "a" in x:
        newlist.append(x)
print(newlist)

for x in thislist:
    if "a" in x:
        x = x.upper()
        newlist.append(x)

print(newlist)


listnb = list(range(10))
print(listnb)
