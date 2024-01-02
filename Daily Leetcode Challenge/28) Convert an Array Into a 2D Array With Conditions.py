"""
2610. Convert an Array Into a 2D Array With Conditions

Medium

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.


Example 1:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length
"""


# Solution 

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []  # List to store the result
        temp_dict = {}  # Dictionary to store the frequency of each value in nums

        # Count the frequency of each value in nums
        for val in nums:
            temp_dict[val] = temp_dict.get(val, 0) + 1

        # Continue until temp_dict is not empty
        while temp_dict:
            temp = []  # Temporary list for the current sublist

            # Iterate through temp_dict items
            for key, val in temp_dict.items():
                temp.append(key)  # Add 'key' to 'temp'

                temp_dict[key] -= 1  # Decrement the frequency of 'key'

            # Create a new dictionary without keys with frequency zero
            # temp_dict = {key: val for key, val in temp_dict.items() if val > 0}
            new_dict = {}
            for key, val in temp_dict.items():
                if val > 0:
                    new_dict[key] = val
            
            temp_dict = new_dict

            res.append(temp)  # Add the current sublist to the result list

        return res

'''
Overall: O(n * m), where n is the length of the input list nums and m is the maximum frequency of any value in nums.

Breakdown:
Counting frequencies in temp_dict: O(n)
while loop: Iterates at most m times (based on maximum frequency)
Each iteration involves:
Iterating over temp_dict items: O(m) (in the worst case)
Creating temp list: O(m)
Decrementing frequencies: O(m)
Recreating temp_dict: O(m)
Appending temp to res: O(1)


Space Complexity: O(n)
res list: Stores up to n elements in the worst case
temp_dict: Stores at most n elements (one for each unique value in nums)
temp list: Transient, doesn't contribute to overall space complexity

Key factors for time complexity:

The number of distinct values in nums influences the number of iterations of the while loop.
The maximum frequency of any value in nums determines the maximum number of key-value pairs in temp_dict, 
affecting the time spent iterating over it.

'''