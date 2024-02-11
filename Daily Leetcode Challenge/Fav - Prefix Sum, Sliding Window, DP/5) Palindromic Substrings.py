"""
647. Palindromic Substrings

Medium

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.


Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

"""


# SOLUTION
class Solution:
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        t = [[False] * n for _ in range(n)]
        # t[i][j] = true : s[i:j] is a substring where i and j are inclusive indices

        count = 0

        for L in range(1, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if i == j:
                    t[i][i] = True  # Single characters are palindrome
                elif i + 1 == j:
                    t[i][j] = s[i] == s[j]  # Strings of 2 Length
                else:
                    t[i][j] = s[i] == s[j] and t[i + 1][j - 1]

                count += t[i][j]

        return count
        

'''
# Approach-1 (Simply check all substrings possible)
# T.C : O(n^3)
# S.C : O(1)
class Solution:
    def check(self, s: str, i: int, j: int) -> bool:
        if i >= j:
            return True

        if s[i] == s[j]:
            return self.check(s, i + 1, j - 1)

        return False

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s, i, j):
                    count += 1
        return count


# Approach-2 (Memoize the approach above)
# T.C : O(n^2) - Every subproblem is being computed only once and after that it's being reused
# S.C : O(n^2)
class Solution:
    def __init__(self):
        self.t = [[-1] * 1001 for _ in range(1001)]

    def check(self, s: str, i: int, j: int) -> bool:
        if i >= j:
            return True

        if self.t[i][j] != -1:
            return self.t[i][j]

        if s[i] == s[j]:
            return self.check(s, i + 1, j - 1)

        return False

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s, i, j):
                    count += 1
        return count


# Approach-3(Bottom Up - My Favourite Blue Print of Palindrome Qns)
# T.C : O(n^2)
# S.C : O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        t = [[False] * n for _ in range(n)]
        # t[i][j] = true : s[i:j] is a substring where i and j are inclusive indices

        count = 0

        for L in range(1, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if i == j:
                    t[i][i] = True  # Single characters are palindrome
                elif i + 1 == j:
                    t[i][j] = s[i] == s[j]  # Strings of 2 Length
                else:
                    t[i][j] = s[i] == s[j] and t[i + 1][j - 1]

                count += t[i][j]

        return count


# Approach-4 (Smart approach)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def __init__(self):
        self.count = 0

    def check(self, s: str, i: int, j: int, n: int) -> None:
        while i >= 0 and j < n and s[i] == s[j]:
            self.count += 1
            i -= 1  # expanding from center
            j += 1  # expanding from center

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.count = 0

        """
    Every single character in the string is a center for possible odd-length palindromes: check(s, i, i);
    Every pair of consecutive characters in the string is a center for possible even-length palindromes: check(s, i, i+1);
        """
        for i in range(n):
            self.check(s, i, i, n)
            self.check(s, i, i + 1, n)
        return self.count

'''
