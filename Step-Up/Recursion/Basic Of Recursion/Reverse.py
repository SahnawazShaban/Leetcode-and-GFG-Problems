# def reverseArray(arr, l, r):
#     if l >= r:
#         return arr
#     arr[l], arr[r] = arr[r], arr[l]
#
#     return reverseArray(arr, l+1, r-1)
#
#
# arr = [2, 4, 5, 1, 6, 7]
# print(reverseArray(arr, 0, len(arr) - 1))


def reverseArray1(arr, i, n):
    if i > n // 2:
        return arr
    arr[i], arr[n - i] = arr[n - i], arr[i]
    return reverseArray1(arr, i + 1, n)


arr = [2, 4, 5, 1, 6, 7]
print(reverseArray1(arr, 0, len(arr) - 1))
