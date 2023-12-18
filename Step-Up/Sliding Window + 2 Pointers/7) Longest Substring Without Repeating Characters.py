"""
3. Longest Substring Without Repeating Characters

Medium

Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

"""

# SOLUTION

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        temp_dict = {}
        max_len = 0
        while r < len(s):
            if s[r] in temp_dict:
                l = max(l, temp_dict[s[r]]+1)

            max_len = max(max_len, r-l+1)
            temp_dict[s[r]] = r
            r += 1
        return max_len



        # l, r = 0, 0   # Initialize two pointers, l and r, to the start of the string.
        # temp_dict = {}  # Initialize a dictionary to store the most recent index of each character.
        # max_len = 0    # Initialize a variable to keep track of the maximum length of the substring.

        # while r < len(s):  # Start a loop that will run until the right pointer reaches the end of the string.
        #     if s[r] in temp_dict:
        #         # If the character at the right pointer already exists in the dictionary, it means there's a repeat.
        #         # Move the left pointer (l) to the position after the previous occurrence of this character.
        #         l = max(l, temp_dict[s[r]] + 1)

        #     # Calculate the current length of the substring and update max_len if it's longer.
        #     max_len = max(max_len, r - l + 1)

        #     # Store the current index of the character in the dictionary.
        #     temp_dict[s[r]] = r

        #     # Move the right pointer to the next character in the string.
        #     r += 1

        # # Return the maximum length of a substring without repeating characters.
        # return max_len
    