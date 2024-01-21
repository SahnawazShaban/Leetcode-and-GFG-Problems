"""
198. House Robber

Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""


# SOLUTION

# Recursion
class Solution:
    def func(self, idx, nums):
        if idx == 0:
            return nums[0]
        if idx < 0: 
            return 0

        pick = nums[idx] + self.func(idx-2, nums)
        notpick = 0 + self.func(idx-1, nums)

        return max(pick, notpick)

    def rob(self, nums: List[int]) -> int:
        # Recursion
        n = len(nums)
        return self.func(n-1, nums)

# Memoization
class Solution:
    def func(self, idx, nums, dp):
        if idx == 0:
            return nums[0]
        if idx < 0: 
            return 0

        # Memoization
        if dp[idx] != -1: # if those states have already called, there is no need to further recursion call
            return dp[idx]

        pick = nums[idx] + self.func(idx-2, nums, dp)
        notpick = 0 + self.func(idx-1, nums, dp)

        dp[idx] = max(pick, notpick)

        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        # Recursion
        n = len(nums)
        dp = [-1]*(n)
        return self.func(n-1, nums, dp)
       
        
'''
Recursion:
Time Complexity: Exponential, O(2^n), due to repeated computations.
Space Complexity: O(n), where 'n' is the maximum depth of the recursion stack.

Memoization:
Time Complexity: O(n)
Space Complexity: O(n) [stack space] + O(n) [array space] = O(n)
'''
