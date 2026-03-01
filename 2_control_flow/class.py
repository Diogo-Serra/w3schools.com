#!/usr/bin/env python3

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


person1 = Person("Diogo", 35, 1.80)
print(f"{person1.age}")
