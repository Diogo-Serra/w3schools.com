#!/usr/bin/env python3
"""
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
"""


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


def greeting():
    return "Hello"


message = greeting()
print(message)
