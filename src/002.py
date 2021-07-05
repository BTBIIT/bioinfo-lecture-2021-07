#! /usr/bin/env python
import math
import sys

#r = int(input("반지름 입력"))

#pie = math.pi

#print ("반지름이 {} 인 원의 넓이 : ".format(r) ,r*r*pie)


# sys 이용법
#r2 = int(sys.argv[1])
#print(r2**2*pie)


# 아무것도 입력 안했을때 메세지 출력
#if len(sys.argv) != 2:
#    print(f"#usage:python {sys.argv[0]} [num]")
#    sys.exit()

#r = int(sys.argv[1])
#pi = math.pi
#result = round(r**2 *pi, 2)
#
#print(result)


# 사칙연산 문제 풀기
#if len(sys.argv) != 3:
#    print(f"usage: python {sys.argv[0]} [n1] [n2]")
#    sys.exit()

#n1 = int(sys.argv[1])
#n2 = int(sys.argv[2])

#print(f" {n1} + {n2} = {n1+n2}")
#print(f" {n1} - {n2} = {n1-n2}")
#print(f" {n1} x {n2} = {n1*n2}")
#print(f" {n1} / {n2} = {n1/n2}")
#print(f" {n1} % {n2} = {n1%n2}")
#print(f" {n1} ** {n2} = {n1**n2}")



# 홀짝판별
#if len(sys.argv) !=2:
#    print(f"usage : python {sys.argv[0]} [num]")
#    sys.exit()

#num = int(sys.argv[1])
# 일반적으로 출력
#if num% 2 == 0 :
#    print("even")
#else:
#    print("odd")

# else안쓰고 print하는 방법
#result = "odd"
#if num % 2 == 0:
#    result ="even"
#print(result)


# 3의 배수 7의 배수 판별법
if len(sys.argv) != 2:
    print(f"usage : python {sys.argv[0]} [n1]")
    sys.exit()

n1 = int(sys.argv[1])

result = "neither 3,7"

if n1 % 3 == 0 and n1 % 7 == 0:
    result = "3,7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"

print(result)
