#! /usr/bin/env python

import sys


# 1 부터 10까지 숫자 합을 구하는 프로그램을 작성해보아라.

val = 0
for i in range(0,11): # 과거에는 range하면 리스트 객체가 나왔음.
    val = val+i # 같은 뜻으로 val += i 를 쓸 수 있음
print(val)

# 곱

val2 = 1

for i in range(1,11):
    val2 = val2*i

print(val2)

