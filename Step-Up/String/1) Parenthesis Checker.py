"""
Parenthesis Checker

Easy

Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Example 1:
Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of unbalanced bracket.

Example 2:
Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is present and in balanced way.

Example 3:
Input: 
([]
Output: 
false
Explanation: 
([]. Here square bracket is balanced but the small bracket is not balanced and 
Hence , the output will be unbalanced.

Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false. The printing is done automatically by the driver code.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 32000

"""

# SOLUTION

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # Solution - 1
        
        stack = []
        n = len(x)
        
        if n%2 == 1:
            return False
            
        if x[0] == ']' or x[0] == ')' or x[0] == '}':
            return False
        
        temp_dict = {']':'[', '}':'{', ')':'('}
        
        for i in x:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            else:
                if stack and temp_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if stack:
            return False
        return True
        
        
        # -----------------------------------------
        
        # Solution -2
        
        stack = []
        n = len(x)
    
        # Check if the length is odd (necessary check)
        if n % 2 == 1:
            return False
    
        temp_dict = {'[': ']', '{': '}', '(': ')'}
    
        # Check if the first character is a closing parenthesis
        if x[0] in temp_dict.values():
            return False
    
        for i in x:
            if i in temp_dict.keys():
                stack.append(i)
            else:
                if not stack or temp_dict[stack.pop()] != i:
                    return False
    
        # Check if the stack is empty after processing the string
        return not stack
        
        
        # --------------------------------------------
        
        # Solution -3 
        
        if len(s) % 2 != 0 or len(s) <= 1:
            return False

        temp_dict = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif not stack or stack.pop() != temp_dict[i]:
                return False
        
        return len(stack) == 0
        
        
        # -------------------------------------------
        
        # Solution - 4
        
        stack = [] # Initialize an empty stack to track open brackets
        closeToOpen = {'}':'{',']':'[',')':'('} # Mapping of closing brackets to their corresponding open brackets

        for i in s:
            if i in closeToOpen:  # If the character is a closing bracket
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop() # Matched an open bracket, so remove it from stack
                else:
                    return False # Mismatch or no open bracket to match
            else:
                stack.append(i) # Character is an open bracket, push it onto stack
        
        return True if not stack else False # If stack is empty, all brackets are matched and valid

        