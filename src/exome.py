
# BED (Browser Extensible Data) 포맷은 유전체를
# 구간별로 나누어 각 구간의 특징을 표기
# 077.bed파일의 경우 첫 번째 열에는 chr21이 들어가 있음.
# 두번째 열에는 start열
# 세번째 열에는 끝나는 열
# 1열을 제외한 2열 3열의 합을 구하여
# 우측에 표기하라.


bed = "077.bed"
result = 0
with open(bed, 'r') as handle:
    for line in handle:
        data = line.strip().split("\t")
        #int(data[2]) - int(data[3]) <- 이렇게 해도 됨.
        chrom, start, end = data
        length = int(end) - int(start)
        result += length

print(result) #29681