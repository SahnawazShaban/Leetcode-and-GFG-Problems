/*
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

*/

// SOLUTION

import java.util.Stack;

class Solution {
    public String preToInfix(String pre_exp) {
        Stack<String> stack = new Stack<>();

        // Traverse the prefix expression in reverse order
        for (int i = pre_exp.length() - 1; i >= 0; i--) {
            char ch = pre_exp.charAt(i);

            // If the character is an operand (assuming it's an alphabet)
            if (Character.isLetter(ch)) {
                stack.push(ch + "");
            } else { // The character is an operator
                String a = stack.pop();
                String b = stack.pop();
                String result = "(" + a + ch + b + ")";
                stack.push(result);
            }
        }

        // The final element in the stack is the infix expression
        return stack.pop();
    }
}
 