"""
5. Longest Palindromic Substring

Medium

Given a string s, return the longest palindromic substring in s.

 
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

# SOLUTION

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute Force - TLE
        # Solution - 1
        
        n = len(s)
        if n <= 1:
            return s

        ans = s[0]

        for i in range(n-1):
            for j in range(i+1, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if len(s[i:j+1]) >= len(ans):
                        ans = s[i:j+1]

        return ans

    '''
    Complexity Analysis
    Time complexity : O(n^3). Assume that n is the length of the input string, there are a total of C(n, 2) = n(n-1)/2 substrings (excluding the trivial solution where a character itself is a palindrome). Since verifying each substring takes O(n) time, the run time complexity is O(n^3).

    Space complexity : O(1).
    '''

    # ----------------------------------------

    # Solution - 2
    # Better

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
        
        '''
        Complexity Analysis
        Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

        Space complexity : O(1).
        '''
        