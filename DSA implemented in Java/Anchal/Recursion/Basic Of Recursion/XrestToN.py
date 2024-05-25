def xPowern(x, n):
    if n == 0:
        return 1
    else:
        return x * xPowern(x, n - 1)


print(xPowern(2, 5))
