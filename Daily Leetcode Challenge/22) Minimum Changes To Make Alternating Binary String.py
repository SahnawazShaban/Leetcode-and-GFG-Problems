"""
1758. Minimum Changes To Make Alternating Binary String

Easy

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.


Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 10^4
s[i] is either '0' or '1'.

------------------------------------------------

Same pattern:
^^^^^^^^^^^^

2957. Remove Adjacent Almost-Equal Characters

Medium

You are given a 0-indexed string word.

In one operation, you can pick any index i of word and change word[i] to any lowercase English letter.

Return the minimum number of operations needed to remove all adjacent almost-equal characters from word.

Two characters a and b are almost-equal if a == b or a and b are adjacent in the alphabet.


Example 1:

Input: word = "aaaaa"
Output: 2
Explanation: We can change word into "acaca" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 2:
Input: word = "abddez"
Output: 2
Explanation: We can change word into "ybdoez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.

Example 3:
Input: word = "zyxyxyz"
Output: 3
Explanation: We can change word into "zaxaxaz" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.


Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.

"""


# Solution 

class Solution:
    def minOperations(self, s: str) -> int:
        # Initialize counters for '0' and '1'
        zero = 0
        one = 0

        # Iterate through the characters of the string
        for i in range(len(s)):
            # Check if the index is even
            if i % 2 == 0:
                # If the character is '0' at even index, increment 'one'
                if s[i] == "0":
                    one += 1
                # If the character is '1' at even index, increment 'zero'
                else:
                    zero += 1
            else:
                # If the character is '1' at odd index, increment 'one'
                if s[i] == "1":
                    one += 1
                # If the character is '0' at odd index, increment 'zero'
                else:
                    zero += 1

        # Return the minimum of 'zero' and 'one'
        return min(zero, one)
    
# -------------------------------------------
    
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        # Get the length of the input string
        n = len(word)

        # Initialize the count of pairs with almost equal characters
        count = 0

        # Start iterating from the second character
        i = 1

        # Iterate through the characters of the string
        while i < n:
            # Check if the absolute difference in ASCII values is less than or equal to 1
            if abs(ord(word[i-1]) - ord(word[i])) <= 1:
                # Increment the count if the condition is met
                count += 1
                # Move to the next pair by skipping one character
                i += 1

            # Move to the next character for the next iteration
            i += 1

        # Return the final count
        return count
        