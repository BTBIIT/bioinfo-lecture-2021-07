#! /usr/bin/env python


class ValueCalculator:
    def __init__(self, val: str):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
##########################################
#print("hi")
class A:
    pass
if __name__ == "__main__":
    print("hi")
