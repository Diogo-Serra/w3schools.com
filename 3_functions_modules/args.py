#!/usr/bin/env python3
"""
*variable, allows us to pass any number
of same type arguments
"""


def my_function(*numbers):
    for number in numbers:
        print(number)


my_function(52, 2, 3, 12, 4)
