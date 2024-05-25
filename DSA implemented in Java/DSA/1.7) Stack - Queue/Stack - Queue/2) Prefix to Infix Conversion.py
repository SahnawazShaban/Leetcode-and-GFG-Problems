"""
Prefix to Infix Conversion

Medium

You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

Example 1:
Input: *-A/BC-/AKL
Output: ((A-(B/C))*((A/K)-L))

Explanation: 
The above output is its valid infix form.

Your Task:
Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
3<=|S|<=10^4

"""

# SOLUTION

class Solution:
    def preToInfix(self, pre_exp):
        stack = []
        # operators = set(['+', '-', '*', '/'])
    
        for char in pre_exp[::-1]:
            if char.isalpha():
                stack.append(char)
            else:
                a=stack.pop()
                b=stack.pop()
                stack.append("("+a+char+b+")")

        return stack[0]
    