"""
20. Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# SOLUTION

class Solution:
    def isValid(self, s: str) -> bool:
        # Solution - 1
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

        # -------------------------------------

        # Solution - 2

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

        