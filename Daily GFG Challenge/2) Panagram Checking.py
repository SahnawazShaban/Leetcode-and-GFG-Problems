"""
Panagram Checking

Easy

Given a string s check if it is "Panagram" or not.

A "Panagram" is a sentence containing every letter in the English Alphabet.

Example 1:
Input:
s = "Bawds jog, flick quartz, vex nymph"
Output: 
1
Explanation: 
In the given input, there
are all the letters of the English
alphabet. Hence, the output is 1.

Example 2:
Input:
s = "sdfs"
Output: 
0
Explanation: 
In the given input, there
aren't all the letters present in the English alphabet. Hence, the output is 0.

Your Task:
You do not have to take any input or print anything. You need to complete the function checkPangram() that takes a string as a parameter and returns true if the string is a Panagram, or else it returns false.

Expected Time Complexity: O( |s| )
Expected Auxiliary Space: O(1)
|s| denotes the length of the input string.

Constraints:
1 ≤ |s| ≤ 10^4
Both Uppercase & Lowercase are considerable

"""

'''
In Python, the ord() function is used to get the Unicode code point of a given character. 
The Unicode code point is an integer representation of a character in the Unicode standard. 

For example:
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97
print(ord('1'))  # Output: 49
'''

# Solution 

class Solution:
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        alpha_array = [0]*26
        
        for ch in s.lower():
            if ch.isalpha():
                alpha_array[ord(ch) - ord('a')] = 1
                
        
        for freq in alpha_array:
            if not freq:
                return False
        
        return True
    