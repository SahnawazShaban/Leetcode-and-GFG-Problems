"""
424. Longest Repeating Character Replacement

Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

"""

# SOLUTION

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}  # Dictionary to store the count of characters in the current window
        res = 0  # Variable to store the length of the longest valid substring
        l = 0  # Left pointer for the sliding window

        # Iterate through the string with the right pointer (r)
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1  # Update the count of the current character

            # Check if the length of the current window minus the max frequency is greater than k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # Move the left pointer and update the count accordingly
                l += 1

            # Update the length of the longest valid substring
            res = max(res, r - l + 1)

        return res

'''
Time Complexity: O(N)
- The algorithm iterates through the string once with the right pointer.
- Each character is processed in constant time, and the while loop ensures that the left pointer moves within the window.

Space Complexity: O(1)
- The space used is constant because the count dictionary only stores the count of characters in the current window.
- The size of the dictionary is determined by the number of unique characters in the input string, which is typically small.
'''
