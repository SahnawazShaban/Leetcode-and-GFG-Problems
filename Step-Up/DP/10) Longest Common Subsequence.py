"""
1143. Longest Common Subsequence (LCS)

Medium

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

"""

# SOLUTION

class Solution:
    def func(self, text1, text2, i, j, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.func(text1, text2, i-1, j-1, dp)
        else:
            dp[i][j] = 0 + max(self.func(text1, text2, i-1, j, dp), self.func(text1, text2, i, j-1, dp))

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1]*m for _ in range(n)]

        return self.func(text1, text2, n-1, m-1, dp)


'''
TC = O(n*m)
SC = O(n*m) + O(n+m) [auxilairy space (match or not match)]
'''
        
