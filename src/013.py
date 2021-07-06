#! /usr/bin/env python

# 문자열 더하기.

var1 = "Bio"
var2 = "Informatics"
var3 = var1 + var2
print(var3)
print()


class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
    def __mul__(self, other):
        return "__mul__"
    

a1 = A("a")
a2 = A("b")

print(a1.val + a2.val)# def init 부분
print()
print(a1 + a2)# def add 부분
print(a1 * a2)# def mul 부분


