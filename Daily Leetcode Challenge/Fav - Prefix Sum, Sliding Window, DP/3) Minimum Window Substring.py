"""
76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""


# SOLUTION
# Refer Notes no.: 5
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        mp = {}
        for char in t:
            mp[char] = mp.get(char, 0) + 1

        l = 0
        have, need = 0, len(t)
        window_len = float("inf")
        res = [0, 0]

        for r in range(len(s)): 
            if s[r] in mp:
                mp[s[r]] -= 1
                if mp[s[r]] >= 0:
                    have += 1

            while have == need:
                if s[l] in mp:
                    if mp[s[l]] == 0:
                        have -= 1
                    mp[s[l]] += 1

                if (r - l + 1) < window_len:
                    window_len = r - l + 1
                    res = [l, r]
                l += 1

        l, r = res

        return s[l:r + 1] if window_len != float("inf") else ""
        
'''
Time Complexity:
The time complexity of this solution is O(M + N), where M is the length of string s and N is the length of string t. The for loop that initializes the mp dictionary has a time complexity of O(N), and the main loop that iterates through the characters of string s has a time complexity of O(M).

Space Complexity:
The space complexity of this solution is O(N), where N is the length of string t. The space complexity is determined by the mp dictionary, which stores the frequency of characters in string t. The space required for other variables like l, temp_dict, have, need, maxAns, and res is constant and does not depend on the input size.
'''
