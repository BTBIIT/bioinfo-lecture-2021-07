#!/BiO/Access/home/user15/miniconda3/bin/python
# import sys

fibo = [0, 1]
length = int(input("합산하고 싶은 번째의 숫자"))
for i in range(length):
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)


# n = int(sys.argv[1])

# def fib(n: int):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# print(fib(n))
