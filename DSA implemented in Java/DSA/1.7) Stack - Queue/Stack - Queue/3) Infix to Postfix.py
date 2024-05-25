"""
Infix to Postfix

Medium

Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.

Example 1:
Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-

Example 2:
Input: str = "A*(B+C)/D"
Output: ABC+*D/
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be ABC+*D/
 
Your Task:
This is a function problem. You only need to complete the function infixToPostfix() that takes a string(Infix Expression) as a parameter and returns a string(postfix expression). The printing is done automatically by the driver code.

Expected Time Complexity: O(|str|).
Expected Auxiliary Space: O(|str|).

Constraints:
1 ≤ |str| ≤ 10^5

"""

# SOLUTION

class Solution:
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        output = []
        operator = []
        priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

        for ch in exp:
            if ch == '(':
                operator.append(ch)
            elif ch == ')':
                while operator and operator[-1] != '(':
                    ele = operator.pop()
                    output.append(ele)
                operator.pop()  # Remove the '(' from the stack
            elif ch in priority:
                while operator and priority[operator[-1]] >= priority[ch]:
                    ele = operator.pop()
                    output.append(ele)
                operator.append(ch)
            else:
                output.append(ch)

        while operator:
            ele = operator.pop()
            output.append(ele)

        return "".join(output)
    