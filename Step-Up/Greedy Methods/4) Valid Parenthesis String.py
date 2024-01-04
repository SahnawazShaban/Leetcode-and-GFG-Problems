"""
678. Valid Parenthesis String

Medium

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.

"""

# SOLUTION

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Solution - 1 : Using Stack
        stack = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while len(stack) > 0:
            if len(star) == 0:
                return False
            elif star[-1] > stack[-1]: # *(, if * = ) or ( , thatw why top element index must greater
                star.pop()
                stack.pop()
            else:
                return False
        
        return True
        

        # Solution - 2
    
        leftmin = leftmax = 0  # Initialize counters for left parentheses
        for c in s:
            if c == "(":  # If character is '(', increase both leftmin and leftmax
                leftmax += 1
                leftmin += 1
            if c == ")":  # If character is ')', decrease leftmax and update leftmin (cannot be negative)
                leftmax -= 1
                leftmin = max(0, leftmin - 1)
            if c == "*":  # If character is '*', it can be treated as '(' or ')' or empty, so adjust both leftmax and leftmin
                leftmax += 1
                leftmin = max(0, leftmin - 1)
            if leftmax < 0:  # If at any point leftmax goes negative, it means there are more ')' than '(' or '*' before it
                return False
        if leftmin == 0:  # If leftmin is 0, it means all '(' can be balanced with either ')' or '*' at some position
            return True
        else:
            return False  # If leftmin is not 0, it means some '(' cannot be balanced
            