"""
992. Subarrays with K Different Integers

Hard

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length

"""

# SOLUTION

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Solution - 1:
        # MLE
        '''
        n = len(nums)
        ans = []

        for i in range(n):
            for j in range(i, n):
                temp = nums[i:j+1]
                ans.append(temp)

        count = 0
        for val in ans:
            if len(set(val)) == k:
                count += 1

        return count
        '''
        
    # ------------------------------------

    # Solution - 2:
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Count of subarrays with exactly k distinct
        # elements is equal to the difference of the
        # count of subarrays with at most K distinct
        # elements and the count of subarrays with
        # at most (K - 1) distinct elements
        return (self.exactlyK(nums, k) -
                self.exactlyK(nums, k - 1))

    def exactlyK(self, nums, k):
        n = len(nums)
        # To store the result
        count = 0

        # Left boundary of window
        left = 0

        # Right boundary of window
        right = 0

        # Map to keep track of the number of distinct
        # elements in the current window
        my_map = {}

        # Loop to calculate the count
        while(right < n):
            # Calculating the frequency of each
            # element in the current window
            # if nums[right] not in my_map:
            #     my_map[nums[right]] = 0

            
            # my_map[nums[right]] += 1

            # or 

            my_map[nums[right]] = my_map.get(nums[right], 0)+1

            # Shrinking the window from the left if the
            # count of distinct elements exceeds K
            while(len(my_map) > k):

                # if nums[left] not in my_map:
                #     my_map[nums[left]] = 0

                # my_map[nums[left]] -= 1

                # or 

                my_map[nums[left]] = my_map.get(nums[left], 0)-1

                if my_map[nums[left]] == 0:
                    del my_map[nums[left]]

                left += 1

            # Adding the count of subarrays with at most
            # K distinct elements in the current window
            count += right - left + 1
            right += 1

        return count
        

    '''
    Time Complexity:
    The outer while loop runs for each element once, contributing O(N).
    The inner while loop runs for each element at most once, contributing O(N) in total.
    Overall, the time complexity is O(N).
    
    Space Complexity:
    The my_map dictionary keeps track of distinct elements in the current window. In the worst case, it could contain all distinct elements, leading to a space complexity of O(K), where K is the number of distinct elements allowed in the window.
    '''

    # def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    #     # cnt is an array to count the occurrences of each element
    #     # res is the final result, l is the left pointer, and m is the main pointer
    #     cnt, res, l, m = [0] * (len(nums) + 1), 0, 0, 0
        
    #     # Iterate through the elements in nums
    #     for n in nums:
    #         # Increment the count of the current element
    #         cnt[n] += 1
            
    #         # If the count of the current element is 1 (first occurrence),
    #         # decrement the distinct element counter k
    #         if cnt[n] == 1:
    #             k -= 1
                
    #             # If k becomes negative, remove elements from the window
    #             if k < 0:
    #                 cnt[nums[m]] = 0  # Reduce count for the oldest element in the window
    #                 m += 1  # Move the main pointer to the next element
    #                 l = m  # Update the left pointer to the new starting position
            
    #         # If there are at least k distinct elements, count subarrays
    #         if k <= 0:
    #             while cnt[nums[m]] > 1:
    #                 cnt[nums[m]] -= 1
    #                 m += 1  # Move the main pointer to the next element
    #             res += m - l + 1  # Count subarrays with at most k distinct elements
        
    #     return res
                
'''
Time Complexity:
The time complexity is indeed O(N), where N is the length of the input array nums. Both pointers l and m move from left to right, and each element is processed at most twice, leading to a linear time complexity.

Space Complexity:
The space complexity is O(N) as well. The cnt array has a length of (N + 1), and additional variables (res, l, and m) are constant in terms of the input size.
'''

