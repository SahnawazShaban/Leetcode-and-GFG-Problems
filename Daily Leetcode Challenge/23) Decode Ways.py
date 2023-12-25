"""
91. Decode Ways

Medium

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.


Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

"""


# Solution 

class Solution:
    # Recursive Approach:
    '''
    def numDecodings(self, s: str) -> int:
        def helper(index):
            # If reached the end of the string, there is one way to decode
            if index == len(s):
                return 1
            # If the current digit is zero, it cannot be decoded
            if s[index] == '0':
                return 0

            ways = helper(index + 1)
            # Check if the combination of current and next digits forms a valid two-digit number
            if index < len(s) - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] <= '6')):
                ways += helper(index + 2)

            return ways

        return helper(0)
    '''
    # Time Complexity: Exponential (worst case), as it recalculates many values repeatedly
    # Space Complexity: O(n) (recursion call stack)

    # ----------------------------------------------------------------

    # Memoization (Top-Down Dynamic Programming):
    
    def numDecodings(self, s: str) -> int:
        memo = {}

        def helper(index):
            # If reached the end of the string, there is one way to decode
            if index == len(s):
                return 1
            # If the current digit is zero, it cannot be decoded
            if s[index] == '0':
                return 0

            if index not in memo:
                ways = helper(index + 1)
                # Check if the combination of current and next digits forms a valid two-digit number
                if index < len(s) - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] <= '6')):
                    ways += helper(index + 2)
                memo[index] = ways

            return memo[index]

        return helper(0)
    

    # Time Complexity: O(n)
    # Space Complexity: O(n) (additional space for memoization)

    # ----------------------------------------------------------

    # Tabulation (Bottom-Up Dynamic Programming):
    '''
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            # If the current digit is zero, it cannot be decoded
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i + 1]
                # Check if the combination of current and next digits forms a valid two-digit number
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    dp[i] += dp[i + 2]

        return dp[0]
    Time Complexity: O(n)
    Space Complexity: O(n) (additional space for the dynamic programming table)
    '''

    # --------------------------------------------------------------------

    # Space Optimization (Tabulation with O(1) Space):
    '''
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b = 0, 1

        for i in range(n - 1, -1, -1):
            current_ways = 0
            # If the current digit is not zero, add the ways from the previous step
            if s[i] != '0':
                current_ways += b
                # Check if the combination of current and next digits forms a valid two-digit number
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    current_ways += a
            a, b = b, current_ways

        return b
    '''

    # Time Complexity: O(n)
    # Space Complexity: O(1) (constant space, as it only uses two variables)

