"""
205. Isomorphic Strings

Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

# SOLUTION

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp_dict_st = {}
        temp_dict_ts = {}

        for i in range(len(s)):
            
            if ((s[i] in temp_dict_st and temp_dict_st[s[i]] != t[i]) 
                or (t[i] in temp_dict_ts and temp_dict_ts[t[i]] != s[i])):
                return False
            
            temp_dict_st[s[i]] = t[i]
            temp_dict_ts[t[i]] = s[i]

        return True
