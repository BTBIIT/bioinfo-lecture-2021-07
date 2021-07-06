#! /usr/bin/env python

#name = input("이름 입력 : ") #input이 기본값은 string
#print("Hello %s." %name)



#print(f"Hello {name}.")

s = input("입력 : ")
if s.isalpha():   # type오류로 인해서 일어남.
    print("문자")
else:
    print("숫자")
