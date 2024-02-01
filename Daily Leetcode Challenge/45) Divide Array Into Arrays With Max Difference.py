"""
2966. Divide Array Into Arrays With Max Difference

Medium

You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

Example 1:
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.

Example 2:
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
 

Constraints:

n == nums.length
1 <= n <= 10^5
n is a multiple of 3.
1 <= nums[i] <= 10^5
1 <= k <= 10^5

"""


# SOLUTION

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []

        nums.sort()
        n = len(nums)
        i = 2

        while i < n:
            if nums[i] - nums[i-2] <= k:
                res.append([nums[i-2], nums[i-1], nums[i]])
            else:
                return []

            i += 3

        return res
    

'''
Time Complexity:
The nums.sort() operation takes O(n log n) time, where n is the length of the input list nums.
The while loop iterates through the sorted array once, and since i increments by 3 in each iteration, it runs in O(n/3) = O(n) time.
The overall time complexity is dominated by the sorting operation, so the final time complexity is O(n log n).

Space Complexity:
The space complexity is O(1) because the additional space used by the algorithm is constant, regardless of the size of the input. The most significant space usage is for the result list res, which is not dependent on the input size.

In summary:
Time Complexity: O(n log n)
Space Complexity: O(1)
'''
    