"""
2. Omitted Number
Easy
Given an array nums containing n distinct numbers taken from 0, 1, 2, ..., n, find the missing number.

Implement a function missingNumber(nums) that returns the missing number.

Example 1:
Input
3
3 0 1

Output
2

Explaination:

In the given example, the input array nums contains numbers from 0 to 3. The missing number is 2.

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= n
The array does not contain any duplicates.
Input Format:

An array nums containing n distinct numbers taken from 0, 1, 2, ..., n.

Output Format:

An integer representing the missing number.

"""


# Solution 

class Solution:
    def omittedNumber(self, nums: List[int]) -> int:
        total = 0
        sum_1ton = 0
        
        for val in nums:
            total += val
            
        for i in range(1,len(nums)+1):
            sum_1ton += i
            
        missing = sum_1ton - total
        
        return missing