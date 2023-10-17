"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""

# SOLUTION

class Solution:
    def addDigits(self, num: int) -> int:
        # TLE

        # if 0 <= num <= 9:
        #     return num

        # ans = 0
        # while num != 0:
        #     digit = num%10
        #     ans += digit
        #     num = num//10

        #     if ans >= 10 and num == 0:
        #         num = ans

        # return ans

        # ----------------------------------

        """
        WRONG ANSWER : So I add 
        ________________
        if num % 9 == 0:
            return 9
        ^^^^^^^^^^^^^^^^
        Input
        num =
        18

        Use Testcase
        Output
        0
        Expected
        9
        """

        # if 0 <= num <= 9:
        #     return num
        # elif num % 9 == 0:
        #     return 9
        # else:
        #     return num % 9


        # ----------------------------------
        # Recursive Approach
        
        if num < 10:
            return num
        else:
            new_num = 0
            while num > 0:
                new_num += num % 10
                num //= 10
            return self.addDigits(new_num)