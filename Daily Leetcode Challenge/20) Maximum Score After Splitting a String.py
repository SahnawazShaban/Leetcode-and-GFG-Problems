"""
4. Maximum Score After Splitting a String

Easy

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.


Example 1:
Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.


For more understanding:

Initial State:
String: 01110
Initial left value: -1
Initial zeroes count: 0
Initial ones count: 0

Iteration 1:
Current character: 0
Increment zeroes: 1
Update left with max(-1, 1-0) = 1

Iteration 2:
Current character: 1
Increment ones: 1
Update left with max(1, 1-1) = 1

Iteration 3:
Current character: 1
Increment ones: 2
Update left with max(1, 1-2) = 1

Iteration 4:
Current character: 1
Increment ones: 3
Update left with max(1, 1-3) = 1

Iteration 5:
Current character: 0
Increment zeroes: 2
Update left with max(1, 2-3) = 1

Final State:
String: 01110
Final left value: 1
Final zeroes count: 2
Final ones count: 3

Answer 👍
ones += s[-1] == '1'
Ones + left + 

"""


# Solution 

class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize counters for the number of '0's and '1's
        zeroes = 0
        ones = 0

        # Variable to store the maximum score for the left part
        left = -1

        # Iterate through the string up to the second-to-last character
        for i in range(len(s)-1):
            # Increment the counters based on the current character
            if s[i] == '0':
                zeroes += 1
            else:
                ones += 1

            # Update the 'left' variable with the maximum difference between '0's and '1's
            left = max(left, zeroes - ones)

        # Update the 'ones' count for the last character if it is '1'
        ones += s[-1] == '1'

        # Return the maximum score, which is the sum of 'left' and the updated 'ones' count
        return left + ones
        