"""
1392. Longest Happy Prefix

Hard

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

"""

# SOLUTION

class Solution:
    def longestPrefix(self, s: str) -> str:
        # Solution - 1

        '''
        temp1 = []
        temp2 = []

        preFix = ""
        sufFix = ""

        # I don't need the whole string in my list; therefore I write [len(s)-1]
        for i in range(len(s)-1):
            preFix += s[i]
            temp1.append(preFix)
        temp1 = temp1[::-1]
        
        # I don't need the whole string in my list; therefore, I write (start,end, step).
        # end as 0 (so it is not added as a whole reverse string).
        for i in range(len(s)-1,0,-1):
            sufFix += s[i]
            revSuffix = sufFix[::-1]
            temp2.append(revSuffix)
        
        i=0
        while i < len(temp1):
            if temp1[i] in temp2:
                return temp1[i]
            i += 1
        
        return ""
        '''

        # Solution - 2

        n = len(s)-1
        t = 0
        p = ""

        for i in range(n):
            if s[:i+1] == s[n-i:]:
                if i+1 > t:
                    p = s[:i+1]
                    t = i+1

        return p

