"""
162. Find Peak Element

Medium

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.

"""

# SOLUTION

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        ele = float('-inf')

        while left <= right:
            if nums[left] >= nums[right]:
                if ele < nums[left]:
                    ele = nums[left]
                    idx = left
                left += 1
            else:
                if ele < nums[right]:
                    ele = nums[right]
                    idx = right
                right -= 1
        return idx

        # -------------------------------------

        left =0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left ) //2
            if nums[mid] > nums[mid+1]: 
                # Find First True i.e first elem where this condition will be True
                right = mid # include mid # mid is potential solution 
            else:
                left = mid +1
        return left

        # -------------------------------------

        left =0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left + 1) //2 # Right biased mid as left = mid in else condition # prevent infinite loop
            if nums[mid] > nums[mid-1]: # True condition # go right # inc function # Last True 
                left = mid # mid is a potential elem
            else:
                right = mid -1
        return left

        # ---------------------------------------

        left =0
        right = len(nums)-1
        while(left < right):
            mid = left +(right-left)//2
            if nums[mid] <  nums[mid+1]: # False Condition # inc function # go right # Find First False
			# i.e. find First elem when this if will be false
                left = mid+1 # exclude mid 
            else: 
                right = mid
        return left

        # ----------------------------------------

        left =0
        right = len(nums)-1
        while(left < right):
            mid = left +(right-left+1)//2 # Right biased mid as left = mid in else condition # prevent infinite loop
            if nums[mid] < nums[mid-1]: # False condition # Dec function # go left # Find Last False i.e the Last elem for which this condition will be False 
                right = mid - 1
            else: # decreasing so peak will be before mid or it can be mid
                left = mid
        return left
