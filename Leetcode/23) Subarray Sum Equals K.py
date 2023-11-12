"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2


Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

# SOLUTION

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, prefix_sum, d = 0, 0, {0: 1}
        for num in nums:
            prefix_sum += num
            key = prefix_sum - k
            if key in d:
                ans += d[key]
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
        return ans

        # -------------------------------

        ## TLE
        '''
        n = len(nums)
        count = 0

        for i in range(n):
            k_sum = 0
            for j in range(i,n):
                k_sum += nums[j]
                if k_sum == k:
                    count += 1
        
        return count
        '''

        