"""
1. Majority Element
Easy
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input
3
4 2 4

Output
4

Explaination:
4 is the majority element because it appears more than n/2 times (in this case, 2 out of 3 times).

Constraints:

1 <= n <= 10^5
-10^9 <= nums[i] <= 10^9

Input Format:
An array of integers

Output Format:
The majority element as an integer

"""


# Solution 

class Solution:
     def majorityElement(self, nums: List[int]) -> int:
        temp_dict = {}
        for val in nums:
            temp_dict[val] = temp_dict.get(val,0)+1
            
        maxi = 0
        for key,count in temp_dict.items():
            if count > maxi:
                maxi = count
                ans = key
            
        return ans