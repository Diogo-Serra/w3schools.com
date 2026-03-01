#!/usr/bin/env python3
"""
*variable, allows us to pass any number
of same type arguments
"""


def my_function(*numbers):
    for number in numbers:
        print(number)


# my_function(52, 2, 3, 12, 4)


def max_function(*numbers):
    if (len(numbers) == 0):
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


max = max_function(100, 4, 55, 21, 212)
print(max)
