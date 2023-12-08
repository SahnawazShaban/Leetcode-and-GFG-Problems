# def gcd(a, b):
#     ans = 1
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             ans = i
#     return ans
#
#
# a = 8
# b = 12
# print(gcd(a, b))

## Recursive form

# gcd(a,b) = gcd(4,8)
#          = gcd(8,4%8)
#          = gcd(4,8%4)
#          = gcd(4,0)

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a, b = 4, 8
print(gcd(a, b))
