"""
Reverse words in a given string

Easy

Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:
Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the wholestring(not individual words), the inputstring becomes
much.very.program.this.like.i

Example 2:
Input:
S = pqr.mno
Output: mno.pqr
Explanation: After reversing the whole string , the input string becomes
mno.pqr

Your Task:
You dont need to read input or print anything. Complete the function reverseWords() which takes string S as input parameter and returns a string containing the words in reversed order. Each word in the returning string should also be separated by '.' 


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)


Constraints:
1 <= |S| <= 10^5

"""

# SOLUTION

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # Solution - 1
        
        S1 = S.split('.')
        
        n = len(S1)
        j = 0
        l1 = []
        
        for i in range(n-1,-1,-1):
            l1.append(S1[i])
            j += 1
            
        return ".".join(l1)
        
        
        # Time and Space Complexity
        '''
        Time Complexity:

        The split() method has a time complexity of O(N), where N is the length of the input string.
        The loop runs in O(N) time because it iterates through each element in the list obtained from the split operation.
        
        The join() method has a time complexity of O(N), where N is the length of the resulting string.
        Therefore, the overall time complexity is O(N).
        
        
        Space Complexity:
        
        The S1 list stores the words obtained after splitting the string, which has a space complexity of O(N).
        
        The l1 list stores the reversed words, which also has a space complexity of O(N).
        Therefore, the overall space complexity is O(N).
        '''
                
        # ----------------------------------------
        
        # Solution - 2
        
        # Split the string into a list of words using dots as the delimiter
        words = S.split('.')
    
        # Reverse the list of words and join them using dots as the separator
        reversed_string = ".".join(reversed(words))
    
        return reversed_string
    