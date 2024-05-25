def sumOfNum(n):
    if n==0:
        return 0
    else:
        return n+sumOfNum(n-1)

print(sumOfNum(5))
