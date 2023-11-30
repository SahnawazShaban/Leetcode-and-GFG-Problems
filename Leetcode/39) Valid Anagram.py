"""
242. Valid Anagram

Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

# SOLUTION

class Solution:
    def isAnagram(self, s: str, t: str) -> str:
        # Solution - 1
        '''
        if len(s) != len(t):
            return False

        n = len(t)
        temp_list = list(t)
        for i in range(n):
            if s[i] in temp_list:
                temp_list.remove(s[i])
            else:
                return False
        
        return True
        '''

        # Solution - 2
        '''
        temp_s, temp_t = {}, {}

        for char in s:
            temp_s[char] = temp_s.get(char,0)+1
        
        for char in t:
            temp_t[char] = temp_t.get(char,0)+1

        return temp_s == temp_t
        '''

        # Solution - 3

        # Try to solve 1 dictionary

        temp_dict = {}

        for i in s:
            temp_dict[i] += 1

        for i in t:
            temp_dict[i] -= 1

        for count in temp_values():
            if count != 0:
                return False
        
        return False
    

'''
Please refer to this link to learn more about it, like time and space complexity.
https://leetcode.com/problems/valid-anagram/solutions/4338104/valid-anagram-runtime-54-ms-2-python-solution/

'''
