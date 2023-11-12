"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

# SOLUTION

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## APPROACH : KADANES ALGORITHM ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(1) ##

        # 1. Edge Case : Negative * Negative = Positive
        # 2. So we need to keep track of minimum values also, as they can yield maximum values.

        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            curr_min = min(prev_max * num, prev_min * num, num)
            curr_max = max(prev_max * num, prev_min * num, num)
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max

# -----------------------------------------------

        ## TLE

        '''
        n = len(nums)
        max_pro = float('-inf')
        for i in range(n):
            pro = 1
            for j in range(i,n):
                pro *= nums[j]
            
                max_pro = max(max_pro,pro)

        return max_pro
        '''

        