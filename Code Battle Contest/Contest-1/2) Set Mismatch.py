"""
2. Set Mismatch
Easy
You have a set of integers nums that contains n unique integers from 1 to n.

Return the duplicate number and the missing number in nums. The duplicate number is the number that appears twice in nums and the missing number is the number that is missing from nums.

Example 1:
Input
4
1 2 2 4

Output
2 3

Explaination:

The input array nums is [1, 2, 2, 4].

The duplicate number in nums is 2 and the missing number is 3.

Constraints:

The length of nums is between 1 and 10^4.
Each integer in nums is between 1 and n.
nums contains exactly one duplicate number and exactly one missing number.

Input Format:
An array nums of length n (1 <= n <= 10^4) containing unique integers from 1 to n.

Output Format:
An array [duplicate, missing] containing two integers.

"""


# Solution 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        unique_ele = set(nums)
        sum_of_unique_ele = sum(unique_ele)
        
        max_sum = 0
        n = len(nums)
        for i in range(1,n+1):
            max_sum += i
        
        missing = max_sum - sum_of_unique_ele
        
        dict_temp = {}
        for val in nums:
            dict_temp[val] = dict_temp.get(val,0)+1
            
        twice = 0
        for key, count in dict_temp.items():
            if count > 1:
                twice = key
                
        return twice,missing