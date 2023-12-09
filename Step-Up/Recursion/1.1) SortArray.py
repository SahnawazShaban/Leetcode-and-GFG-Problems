def sortFun(num):
    if len(num) == 0:
        return
    temp = num[len(num)-1]
    num.pop()
    sortFun(num)
    insertSort(num,temp)


def insertSort(num,temp):
    if len(num) == 0 or num[len(num)-1] <= temp:
        num.append(temp)
        return
    val = num[len(num)-1]
    num.pop()
    insertSort(num,temp)
    num.append(val)


num = [4,2,5,8,1,5]
sortFun(num)

for i in num:
    print(i,end=" ")
