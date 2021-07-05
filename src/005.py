#! /usr/bin/env python
import sys


#n = int(sys.argv[1])

#val = 1

#while n>0:
#    val *=n
#    n -= 1
#print(val)


def greet():
    print("Hello, Bioinformatics")

def greet1(name: str) -> None:
    print(f"Hello, {name}")

def greet2(num: int) ->int :
    return num *2

greet()
greet1("Ken")
print()
ret1 = greet1("Ken")
print(ret1)
print()
ret2 = greet2(3)
print(ret2)
