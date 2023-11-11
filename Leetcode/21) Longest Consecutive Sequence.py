"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLen = 0
        for val in nums:
            if val - 1 not in nums:
                temp = val + 1
                while temp in nums:
                    temp += 1
                maxLen = max(maxLen, temp - val)
        return maxLen



        ## TLE

        '''
        maxLen = 0
        
        for val in nums:
            temp = val
            count = 0
            while temp in nums:
                temp += 1
                count += 1
            maxLen = max(maxLen, count)
        
        return maxLen
        '''

        '''
        Time Complexity:

        Converting the nums list to a set takes O(n) time, where n is the length of the list.
        The outer loop runs through each unique element in the set once, so its time complexity is O(n).
        The inner while loop, in the worst case, runs O(n) times overall because each element is processed at most once.
        Therefore, the overall time complexity is O(n).

        Space Complexity:

        The additional space used is primarily for the set (num_set), which can have a maximum size of O(n) in the worst case if all elements are unique.
        Other than that, the space used for variables (val, current_num, current_len, max_len) is constant.
        Therefore, the overall space complexity is O(n).

        In summary, the optimized solution has a time complexity of O(n) and a space complexity of O(n), providing a more efficient algorithm compared to the original solution, especially for large input arrays.
        '''