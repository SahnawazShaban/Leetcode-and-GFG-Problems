def powerSet(idx, arr, arr1):
    # If the index is equal to or exceeds the length of the array, 
    # add the current subset to the result if it's not already present.
    if idx >= len(arr):
        if arr1[:] not in res:
            res.append(arr1[:])
        return

    # Include the current element in the subset and recursively generate subsets.
    arr1.append(arr[idx])
    powerSet(idx + 1, arr, arr1)

    # Exclude the current element from the subset and recursively generate subsets.
    arr1.pop()
    powerSet(idx + 1, arr, arr1)


arr = [2, 1, 3]
res = []  # List to store the power set
powerSet(0, arr, [])  # Start generating power set from index 0
print(res)
