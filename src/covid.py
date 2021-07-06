#! /usr/bin/env python
import gzip
# file_name = "covid19.fasta.gz"
# import로 넣을 경우 file_name을 설정해서 확인하고
# with gzip.open으로 파일을 여는 것으로 바꾸고 읽는 명령어를 r이 아닌 rt로 rb 즉 바이너리로 읽을 경우 utf-8으로 읽는 다는 것을 추가해주어야 함. 나머지 코드는 똑같음
file_name =  "covid19.fasta" # 경로명임 , 절대경로 상대경로 둘다 가능 현재의 경우에는 현재 디렉토리 안에 있기 때문에...

data = dict() # data = {}랑 같은말 /변수에 공간을 만들어둠. # 딕셔너리 형태로 초기화
# data = {"A":0, "T":0.....} 이렇게 저장을 해도 됨.
with open(file_name, 'r') as handle: # with open으로 파일을 열음
    for line in handle: # 한줄씩 넘어오게 함. # covid 바이러스 쌍을
        if line.startswith(">"): # 파일의 읽는 시작위치 헤더라인을 지우기위해 >는 헤더의 특징. > 이문자로 시작을 하면
            continue #continue를 하겠다 라는 뜻. 즉 그냥 넘어가겠다.
        for base in line.strip(): # continue다음의 줄부터 for문을 적용하여하는데 strip으로 enter들을 날려버림. 염기서열이여러 줄로 출력됨으로 엔터들이 들어가 있음
            if base not in data: # base가 data라는 dictionary에 들어있지 않다면 data{"base":0}이 됨. 
                data[base] = 0 # base가 존재하지 않으면 dictionary에 들어가며 0으로 카운트 이후 바로 밑 코드 실행
            data[base] += 1 # 0인 염기는 +1이 되며 1이 카운트 이후 not in 이 아니므로 +1이 됨.
print(data)
# dictionary로 된 것을 출력해서 확인함.


