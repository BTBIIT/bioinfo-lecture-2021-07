#! /usr/bin/env python

s = dict()
a_1 = [3,1,1,2,0,0,2,3,3]

for i in a_1:
    if i not in s:
        s[i] = 0
    s[i] +=1
print(s)



