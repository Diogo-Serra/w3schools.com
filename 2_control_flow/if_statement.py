#!/usr/bin/env python3
"""
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
"""


a = input("Insert number: ")
b = input("Insert number: ")


def if_statement():
    if (b > a):
        print(f"{b} is greater then {a}")
    else:
        print(f"{a} is greater then {b}")
    if ((int)(a) > 0):
        print(f"{a} is a positive number")
    elif ((int)(a) < 0):
        print(f"{a} is a negative number")
    else:
        print(f"{a} is 0")


# This part will run first
score = 75

if (score >= 90):
    print("Grade A")
elif (score >= 80):
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Not good")


if_statement()
