"""
Implement Atoi

Medium

Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.

Example 1:
Input:
s = "-123"
Output: 
-123
Explanation:
It is possible to convert -123 into an integer 
and is so returned in the form of an integer

Example 2:
Input:
s = "21a"
Output: 
-1
Explanation: 
The output is -1 as, due to the inclusion of 'a',
the given string cannot be converted to an integer.
Your Task:
You do not have to take any input or print anything. Complete the function atoi() which takes a string s as an input parameter and returns an integer value representing the given string. If the conversion is not feasible, the function should return -1.

|s| = length of string str.
Expected Time Complexity: O( |s| ), 
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |s| ≤ 10

"""

'''
In Python, the ord() function is used to get the Unicode code point of a given character. 
The Unicode code point is an integer representation of a character in the Unicode standard. 

For example:
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97
print(ord('1'))  # Output: 49
'''

# Solution 

class Solution:
    
    def atoi(self,s):
        ans = 0
        sign = 1
    
        for i in range(len(s)):
            if s[i] == '-' and i == 0:
                sign = -1
            elif '0' <= s[i] <= '9':
                ans = ans * 10 + (ord(s[i]) - ord('0'))
            else:
                return -1
    
        ans = ans * sign
        return ans
    
    