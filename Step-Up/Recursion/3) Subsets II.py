"""
90. Subsets

Medium

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

# SOLUTION

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def sets(nums,idx,temp):
            if idx == len(nums):
                if temp[:] not in res:
                    res.append(temp[:])
                return 

            # include
            temp.append(nums[idx])
            sets(nums,idx+1,temp)

            # exclude
            temp.pop()
            sets(nums,idx+1,temp)



        res = []
        nums.sort()
        sets(nums,0,[])

        return res
        
    
    