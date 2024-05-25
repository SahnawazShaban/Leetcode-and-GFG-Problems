def reverseStr(str,i,n):
    if i >= n//2:
        return True
    if str[i] != str[n-i]:
        return False
    return reverseStr(str,i+1,n)


str = "ShaanaahjS"
str1 = str
print(reverseStr(str,0,len(str)-1))