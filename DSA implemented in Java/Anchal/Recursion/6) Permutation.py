def permutation(nums, arr, freq):
    if len(arr) == len(nums):
        ans.append(arr[:])
        return

    for i in range(len(nums)):
        if not freq[i]:
            freq[i] = True  # pick
            arr.append(nums[i])
            permutation(nums, arr, freq)
            arr.pop()
            freq[i] = False  # non pick


nums = [1, 2, 3]
ans = []
permutation(nums, [], [False]*len(nums))
print(ans)

# Refer Recursion notes for better understanding
