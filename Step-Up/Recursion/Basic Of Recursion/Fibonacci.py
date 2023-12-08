# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))

def fibo(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibo_seq = fibo(n - 1)
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
        return fibo_seq


def printFibo(n):
    fibo_seq = fibo(n)
    for i in fibo_seq:
        print(i, sep=",")


printFibo(5)
