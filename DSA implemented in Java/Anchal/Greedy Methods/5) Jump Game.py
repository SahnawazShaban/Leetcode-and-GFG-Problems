"""
55. Jump Game

Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

"""

# SOLUTION

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Solution - 1
        
        n = len(nums)  # Length of the array
        goal = nums[0]  # Initial jump range from the first index

        # If there's only one element, we're already at the goal
        if n == 1:
            return True

        # Iterate through the array from index 1 to n-1
        for i in range(1, n):
            # If we can't make any more jumps (goal is 0), return False
            if goal == 0:
                return False

            # Decrement the jump range for the current position
            goal -= 1

            # Update the maximum reachable index (goal) based on the current jump length
            goal = max(goal, nums[i])

        # If we've reached this point without getting stuck, we can reach the last index
        return True
        

# Time Complexity: O(n)
# Space Complexity: O(1)

        # Solution - 2
        n = len(nums)
        goal = n-1

        if n == 1:
            return True

        for i in range(n-2, -1, -1):
            if i+nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        return False
