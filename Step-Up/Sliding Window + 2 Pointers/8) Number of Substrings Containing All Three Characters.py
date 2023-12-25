"""
1358. Number of Substrings Containing All Three Characters

Medium

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.


Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

"""

# SOLUTION

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0  # Variable to store the result
        n = len(s)  # Length of the input string
        i, j = 0, 0  # Pointers for the sliding window
        d = {'a': 0, 'b': 0, 'c': 0}  # Dictionary to store counts of 'a', 'b', and 'c'

        while i + 3 <= n:  # Ensure the window size is at least 3
            if d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                # If the current window contains at least one 'a', 'b', and 'c'
                d[s[i]] -= 1  # Remove the initial element from the window
                ans += (n - j + 1)  # Update the answer with the count of valid substrings
                i += 1  # Move the window to the right
            else:
                if j <= n - 1:
                    d[s[j]] += 1  # Add the next element to the window
                    j += 1  # Move the window to the right
                else:
                    break  # Break if the end of the string is reached

        return ans  # Return the final result



'''
Time Complexity:
The time complexity of this solution is O(n), where n is the length of the input string s. Both pointers i and j traverse the string once, and each character is processed at most twice (once for updating j and once for updating i).

Space Complexity:
The space complexity is O(1). The dictionary d has a fixed size of 3, regardless of the length of the input string. The additional space used is constant.

Note:
The while condition (while i+3 <= n) ensures that the window size is always at least 3, as we are looking for substrings containing 'a', 'b', and 'c'.
The ans += (n-j+1) part calculates the number of substrings that end at the current position j and contain 'a', 'b', and 'c'. (n-j+1) is the number of substrings that can be formed by including the character at position j in the substring.
The loop breaks when the window cannot be expanded further, indicating that the end of the string has been reached.
Make sure to test the code with various inputs to ensure its correctness.
'''