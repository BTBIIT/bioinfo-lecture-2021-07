#! /usr/bin/env python

file_name = "read_sample.txt"
# 첫번째 방법
#ith open (file_name, "r") as handle:
#   for line in handle: # blood1 cancer1 한줄씩 출력
#       print(line, end="")



# 두번째 방법
#handle = open(file_name, "r")
#for line in handle:
#    print(line.strip()) #stirp을 해주어야 newline이 들어가지 않음
#handle.close() #close를 안써주면 파일이 제대로 안닫히기 때문에 파일이나 파이썬에 문제가 생김 따라서 항상 닫아주는 습관을 가져야 함.

# 세번째 방법
handle = open(file_name, "r")
lines = handle.readlines() #예전에는 readlines하면 리스트가 나왔지만 지금은 리스트 같은게 나옴 for문으로 넘겨서 진행.
for line in lines:
    print(line.strip())
handle.close()
