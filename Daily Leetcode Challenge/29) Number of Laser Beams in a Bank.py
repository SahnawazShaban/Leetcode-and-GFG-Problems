"""
2125. Number of Laser Beams in a Bank

Medium

Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

 
Example 1:
Input: bank = [
                "011001",
                "000000",
                "010100",
                "001000"
                ]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
Example 2:


Input: bank = [
                "000",
                "111",
                "000"
                ]
Output: 0
Explanation: There does not exist two devices located on two different rows.
 

Constraints:

m == bank.length
n == bank[i].length
1 <= m, n <= 500
bank[i][j] is either '0' or '1'.

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