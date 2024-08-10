/*
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

*/

// SOLUTION

import java.util.Stack;

class Solution {
    // Function to convert an infix expression to a postfix expression.
    public String infixToPostfix(String exp) {
        StringBuilder output = new StringBuilder();
        Stack<Character> operator = new Stack<>();
        
        // Priority of operators
        int priority[] = new int[256];
        priority['('] = 0;
        priority['+'] = 1;
        priority['-'] = 1;
        priority['*'] = 2;
        priority['/'] = 2;
        priority['^'] = 3;

        for (char ch : exp.toCharArray()) {
            if (ch == '(') {
                operator.push(ch);
            } else if (ch == ')') {
                while (!operator.isEmpty() && operator.peek() != '(') {
                    output.append(operator.pop());
                }
                operator.pop();  // Remove the '(' from the stack
            } else if (priority[ch] > 0) { // If the character is an operator
                while (!operator.isEmpty() && priority[operator.peek()] >= priority[ch]) {
                    output.append(operator.pop());
                }
                operator.push(ch);
            } else { // If the character is an operand
                output.append(ch);
            }
        }

        // Pop all the remaining operators from the stack
        while (!operator.isEmpty()) {
            output.append(operator.pop());
        }

        return output.toString();
    }
}

    