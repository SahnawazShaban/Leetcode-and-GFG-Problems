"""
81. Search in Rotated Sorted Array II

Medium

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.


Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 
Example 3:
Input: nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2
Output : true

Example 4:
Input: nums = [3,1], target = 1
Output : true

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
 

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

"""

# SOLUTION

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ## Brute Force
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
        '''
        # --------------------------------

        ## Optimal Approach - 1
        '''
        return target in nums
        '''

        # ----------------------------------

        ## Optimal Approach - 2
        
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[right]: # Fail to estimate which side is sorted
                right -= 1 # In worst case: O(n)

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return False

        # -------------------------------------------

        ## Optimal Approach - 3

        """
        Time: ~[O(n/2)+O(log(n/2))], where n is len(nums). n/2 since we keep reducing the 
        search space using nums[l] == nums[m] == nums[r] and we enter this condition by
        going through it every time we get duplicates. Still I am not sure about n/2.
        Space: O(1)

        Very similar to problem 33 (the first part). Just keep in mind of 
        nums[l] == nums[m] == nums[r] condition. We use this to shrink our search 
        space and continue to the next iteration.
        """
        '''
        l, r = 0, len(nums)-1

        while l <= r:
            m = r - (r-l)//2

            if target == nums[m]:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            # <= since nums[l] and nums[m] can be duplicates
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return False
        '''
        