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
# class의 매직 메서드 참조 __init__ 이나 __add__나 등등 여러개가 있음.  # 아까 실수로 return __mul__에서 뒤에 언더바2개 생략후 코드return "__mul"  실행했을 때 오류떳음 이상하게 __mul__이라 입력하니 잘돌아감 이유는 까먹고 못물어봄  

a1 = A("a")
a2 = A("b")

print(a1.val + a2.val)# def init 부분
print()
print(a1 + a2)# def add 부분
print(a1 * a2)# def mul 부분


