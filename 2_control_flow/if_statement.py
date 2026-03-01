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


if_statement()
