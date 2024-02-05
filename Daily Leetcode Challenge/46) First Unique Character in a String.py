"""
387. First Unique Character in a String

Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 
Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 

Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.

"""


# SOLUTION

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_str = {}

        for char in s:
            dict_str[char] = dict_str.get(char, 0) + 1

        '''
        temp = {s[i]: i for i in range(len(s))}
        for key, val in dict_str.items():
            if val == 1:
                return temp[key]

        return -1
        '''

        # OR

        for i in range(len(s)):
            if dict_str[s[i]] == 1:
                return i

        return -1
    

'''
Time Complexity: O(n)
Space Complexity: O(d), d = number of distinct characters
'''
    