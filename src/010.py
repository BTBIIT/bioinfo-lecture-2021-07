#! /usr/bin/env python


file_name = "write_sample.txt"

handle = open(file_name, "w") # 쓰기모드로 덮어씀
handle.write("Hello\n")
handle.write("Bioinformatics\n")

with open(file_name, "a") as handle: #a는 append 로 파일내용에다가 추가를 함.
    handle.write ("Ken\n")

s = "s1,s2,s3" #csv
data = s.split(",")
print(data) # ['s1', 's2', 's3']


with open(file_name, "a") as handle:
    handle.write("\t".join(data)+"\n")#""안의 것으로 합쳐지게 됨. 예를 들어서 \t이 아닌 **이면 s1**s2**s3 라는 데이터가 만들어짐. # cat으로 출력하면 마지막 출력 후 주소가 옆으로 붙으므로 뉴라인을 추가한다.
