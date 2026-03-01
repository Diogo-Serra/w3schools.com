#!/usr/bin/env python3

def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())
