#! /usr/bin/env python

# 013 사용자로부터 값 받기 -하드코딩 피하기 94 - 95 page
# 사용자로부터 값을 입력받아 Hello [입력받은 값]을 출력 


# name =  input("이름을 입력해주세요. : ")
# print("Hello {}".format(name), "/", "마법의 중괄호 사용")
# print()
# print(f"Hello {name}", "/", "f-string 사용")
# print()
#######################################################

# 014 사용자로부터 한 글자를 입력받아, 입력받은 문자가 
# 숫자인지 문자인지 출력하는 프로그램 작성.
# 96 - 97 page
# unit = input("한 글자를 입력해 주세요. : ")
# if unit.isalpha() :
#     print(f"{unit}는 문자")
#velse:
#     print(f"{unit}는 숫자")


# 015 커맨드라인에서 argument 입력받기
# import sys
# s = sys.argv[1]
#print(f"Hello {s}.")

# 016 파일 읽기.
# f = open("read_sample.txt", "r")
# r = f.readlines()
# f.close()

# for s in r:
#     print(s.strip())


# 017 파일 쓰기.
# 다음 내용을 write_sample.txt 파일에 써보시오.

# f = open("write_sample.txt", "w")
# f.write("Hello\n")
# f.write("write_sample text file\n")
# f.close()


# ★★★ 019 예외 처리하기 (Debugging) ★★★
# with open ("noname.txt", "r") as fr: # with open은 close()를 따로 해주지 않아도 됨.]
#    read = fr.readlines() # 한줄씩 읽겠다. 

#print(read)

# try : 
#     with open ("noname.txt", "r") as fr:
#         read = fr.readlines()
#     print(read)

# except FileNotFoundError  as err:
#   print(err) 시  [Errno 2] No such file or directory: 'noname.txt'
#    print("파일이 없음")



