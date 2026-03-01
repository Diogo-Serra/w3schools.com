#!/usr/bin/env python3

def my_function():
    print("Hello World")


my_function()
my_function()
my_function()


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(50))
print(type(fahrenheit_to_celsius(50)))
