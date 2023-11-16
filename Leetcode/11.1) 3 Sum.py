"""
15. 3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""

# SOLUTION

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## Brute Force 
        '''
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    ans = nums[i]+nums[j]+nums[k]
                    if ans == 0:
                        with_sorted = sorted([nums[i],nums[j],nums[k]])
                        if with_sorted not in res:
                            res.append(with_sorted)
        
        return res
        '''
        ## Better
        '''
        n = len(nums)
        res = []

        for i in range(n):
            temp_dict = {}
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in temp_dict:
                    ans = [nums[i],nums[j],third]
                    with_sorted = sorted(ans)
                    if with_sorted not in res:
                        res.append(with_sorted)
                temp_dict[nums[j]] = j

        return res
        '''

        ## Optimize - 1

        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1
            while j < k:
                temp_sum = nums[i]+nums[j]+nums[k]
                if temp_sum > 0:
                    k -= 1
                elif temp_sum < 0:
                    j += 1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                    j += 1
                    k -= 1

                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
        return res
        
        ## Optimize - 2

        '''
        result = []
        # 2 pointer approach
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]

                if temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result
        '''
        

        