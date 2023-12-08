def printName(str, n):
    if n == 0:
        return
    print(str)
    return printName(str, n - 1)


str = "Sahnawaz"
n = 5
print(printName(str, n))

# def print1to5(n):
#     if n == 6:
#         return
#     print(n)
#     return print1to5(n+1)
#
# n = 1
#
# print(print1to5(n))

# def printNto1(n):
#     if n == 0:
#         return
#     print(n)
#     return printNto1(n - 1)
#
#
# n = int(input("Enter the number : "))
# print(printNto1(n))

def SumNumber(i,s):
    if i < 1:
        print(s)
        return s
    return SumNumber(i-1,s+i)


n = int(input("Enter : "))
print(SumNumber(n,0))
