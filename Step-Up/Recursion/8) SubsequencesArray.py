def subSequences(idx, arr, arr1):
    if idx >= len(arr):
        res.append(arr1[:])
        return

    arr1.append(arr[idx])
    subSequences(idx+1,arr,arr1)

    arr1.pop()
    subSequences(idx+1,arr,arr1)

    return res


arr = [3, 1, 2]
res = []
print(subSequences(0, arr, []))
