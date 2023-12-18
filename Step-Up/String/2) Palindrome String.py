"""
Palindrome String

Easy

Given a string S, check if it is palindrome or not.

Example 1:
Input: S = "abba"
Output: 1
Explanation: S is a palindrome

Example 2:
Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome

Your Task:
You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.

Expected Time Complexity: O(Length of S)
Expected Auxiliary Space: O(1)

Constraints:
1 <= Length of S<= 2*10^5

"""

# SOLUTION

class Solution:
	def isPalindrome(self, S):
	    # Solution - 1
		
		n = len(S)
		l = 0
		r = n-1
		
		while l <= r:
		    if S[l] == S[r]:
		        l += 1
		        r -= 1
            else:
                return 0
        
        return 1
    

'''
Time Complexity:
    
The time complexity of the code is O(n), where n is the length of the input string S. 
The code uses a two-pointer approach (l and r) that starts from both ends of the string 
and moves towards the center until l is greater than r. In each iteration of the while loop, 
constant-time operations are performed (comparing characters and adjusting pointers), 
and the loop runs for at most n/2 iterations. Therefore, the overall time complexity is 
linear with respect to the size of the input string.


Space Complexity:
    
The space complexity of the code is O(1), indicating constant space usage. 
The only variables used are n, l, and r, which do not depend on the size of the input string. 
These variables are used to control the loop and keep track of the positions in the string, 
but their memory usage is constant regardless of the input size. The code does not use any 
additional data structures that scale with the input size, making it efficient in terms of space.

In summary, the code has a time complexity of O(n) and a space complexity of O(1), 
making it an efficient solution for checking if a string is a palindrome.
'''

# --------------------------------------------

# Solution - 2 

'''
n = len(S)

for i in range(n // 2):
    if S[i] != S[n - 1 - i]:
        return 0  # Not a palindrome

return 1  # Palindrome
'''