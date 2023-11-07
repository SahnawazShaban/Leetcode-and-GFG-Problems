"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.


Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

# SOLUTION

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        maxLen = 0
        for i in range(n):
            maxLen += nums[i]
            
            if maxLen > maxSum:
                maxSum = maxLen

            if maxLen < 0:
                maxLen = 0

        return maxSum

        # ---------------------------------

        # maxSum = nums[0]
        # currentSum = nums[0]

        # for num in nums[1:]:
        #     currentSum = max(num, currentSum + num)
        #     maxSum = max(maxSum, currentSum)

        # return maxSum

        # ----------------------------------

        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i...
            # then its value should be the larger one between nums[i]...
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)...
            # calculate arr[0], arr[1]…, arr[n] while comparing each one with current largest sum...
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum...