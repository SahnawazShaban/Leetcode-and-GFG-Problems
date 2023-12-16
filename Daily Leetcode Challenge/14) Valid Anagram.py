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

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""


# Solution 

class Solution:
    def isAnagram(self, s: str, t: str) -> str:
        # Solution - 1

        '''
        temp = list(t)
        if len(s) == len(t):
            for i in range(len(t)):
                if s[i] in temp:
                    temp.remove(s[i])
                else:
                    return False
            return True
        else:
            return False

        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        The outer loop runs len(t) times because for i in range(len(t)): iterates over each character in string t.

        In each iteration of the loop, the line if s[i] in temp: checks if the current character in string s is present in the list temp. The in operator on a list has a time complexity of O(n) in the worst case, where n is the length of the list.

        If the character is found in the list, the line temp.remove(s[i]) removes that character from the list temp. The remove method has a worst-case time complexity of O(n) because it may need to shift elements after the removal.

        The worst-case scenario is when, for each character in t, the entire temp list needs to be searched, and elements need to be removed. This results in a total time complexity of O(n^2), where n is the length of the strings s and t.
        '''

        # Solution - 2
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

        # Solution - 3
        '''
        temp_s, temp_t = {}, {}

        for char in s:
            temp_s[char] = temp_s.get(char,0)+1
        
        for char in t:
            temp_t[char] = temp_t.get(char,0)+1

        return temp_s == temp_t
        '''

        # Solution - 4
        '''
        Try to solve 1 dictionary

        temp_dict = {}

        for i in s:
            temp_dict[i] = temp_dict.get(i,0)+1

        for i in t:
            temp_dict[i] = temp_dict.get(i,0)-1

        for count in temp_dict.values():
            if count != 0:
                return False
        
        return True

        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        Time Complexity:
        The first two loops iterate over each character in strings s and t, respectively. Both loops have a linear time complexity of O(n), where n is the length of the longer string between s and t.

        The third loop iterates over the values in temp_dict, which has at most 2n distinct characters (the union of characters in s and t). Therefore, this loop also has a linear time complexity of O(n).

        Overall, the time complexity is O(n), where n is the length of the longer string between s and t.

        Space Complexity:
        The space complexity is O(n), where n is the total number of distinct characters in strings s and t. The temp_dict dictionary stores the count of each character, and in the worst case, it could have at most 2n entries (the union of characters from s and t).
        '''

        # -------------------------

        # Solution - 5
        
        if len(s) != len(t):
            return False

        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True 
        
