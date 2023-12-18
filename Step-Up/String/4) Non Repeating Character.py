"""
Non Repeating Character

Easy

Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.

Example 1:
Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.

Example 2:
Input:
S = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is
the character which is non-repeating. 

Your Task:
You only need to complete the function nonrepeatingCharacter() that takes string S as a parameter and returns the character. If there is no non-repeating character then return '$' .

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |S|

Constraints:
1 <= N <= 10^5

"""

# SOLUTION

class Solution:
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        temp_dict = {}
        
        for ch in s:
            temp_dict[ch] = temp_dict.get(ch, 0)+1
            
        # for key, value in temp_dict.items():
        #     if value == 1:
        #         return key
        
        for ch in s:
            if temp_dict[ch] == 1:
                return ch
            
        return '$'
        
        # Time and Space Complexity
        
        '''
        Time Complexity:

        The first loop that counts the occurrences of each character runs in O(N), 
        where N is the length of the input string s.
        The second loop that iterates through the string to find the first non-repeating character 
        also runs in O(N).
        Therefore, the overall time complexity is O(N).
        
        Space Complexity:
        
        The space complexity is O(K), where K is the number of distinct characters in the input string. 
        In the worst case, K can be 26 for an English alphabet.
        
        In summary, your code has a time complexity of O(N) and a space complexity of O(K), 
        where N is the length of the input string and K is the number of distinct characters. 
        These complexities meet the expected requirements based on the provided constraints.
        '''
    