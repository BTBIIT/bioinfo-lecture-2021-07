#! /usr/bin/env python


#문자열 n개씩 건너뛰며 출력하기

seq1 = "ATGTTATAG"

print(seq1[0::3])

for i in range(0,len(seq1),3):
    print(seq1[i])

# seq를 세개씩 출력


for i in range(0,len(seq1),3): # i = 0,3,6
    print(seq1[i:i+3]) # 0~3 4~6 7~9 이렇게 출력이 됨.

print()
seq_rev = seq1[::-1]
print(seq1[::-1])
print(seq1)

# 세로 출력

for i in range(len(seq1)):
    print(f"{seq1[i]}{seq_rev[i]}")



print()
print()

# seq1의 데이터 변환하기
comp_data = {"A":"T", "T":"A", "C":"G", "G":"C"}
comp_seq = ""
for s in seq1:
    comp_seq += comp_data[s]
print(seq1)
print(comp_seq)

for i in range(len(seq1)):
    s = seq1[i]
    cs = comp_seq[i]
    bond ="≡"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{cs}")


for i in range(len(seq1)):
    s = seq1[i:i+2]
    print(i, s, s=="TT")

print()
print()

s = "AA,AC,AG,AT"
data = s.split(",")
print(data)
data.append("CA")
print(data)
print(data[::-1])
