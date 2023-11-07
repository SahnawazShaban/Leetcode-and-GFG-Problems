"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3


Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""

# SOLUTION

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp_dict = {}

        for i in nums:
            temp_dict[i] = temp_dict.get(i,0)+1

        max_count = 0
        for key, val in temp_dict.items():
            if val > max_count:
                max_count = val
                majority_val = key

        return majority_val

        # ------------------------------------------

        ## O(n log n)
        nums.sort()
        n = len(nums)
        return nums[n//2]

        # -----------------------------------------

        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

        # ---------------------------------
        from collections import defaultdict
        
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1
        
        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0
        
        
    