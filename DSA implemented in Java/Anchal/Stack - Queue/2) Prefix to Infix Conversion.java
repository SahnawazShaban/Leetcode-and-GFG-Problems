// """
// Prefix to Infix Conversion
// Medium
// You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

// Example 1:
// Input: *-A/BC-/AKL
// Output: ((A-(B/C))*((A/K)-L))

// Explanation: 
// The above output is its valid infix form.

// Your Task:
// Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

// Expected Time Complexity: O(N).
// Expected Auxiliary Space: O(N).

// Constraints:
// 3<=|S|<=10^4
// """

// SOLUTION

import java.util.Stack;

class GFG {
    // Function to check if character
    // is operator or not
    static boolean isOperator(char x) {
        switch (x) {
            case '+':
            case '-':
            case '*':
            case '/':
            case '^':
            case '%':
                return true;
        }
        return false;
    }

    // Convert prefix to Infix expression
    public static String convert(String str) {
        Stack<String> stack = new Stack<>();
        int l = str.length();

        // Reading from right to left
        for (int i = l - 1; i >= 0; i--) {
            // to store the character and compare 
            char c = str.charAt(i);
            if (isOperator(c)) {
                String op1 = stack.pop();
                String op2 = stack.pop();

                // Concat the operands and operator
                String temp = "(" + op1 + c + op2 + ")";
                stack.push(temp);
            } else {
                // To make character to string
                stack.push(c + "");
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) {
        String exp = "*-A/BC-/AKL";
        System.out.println("Infix : " + convert(exp));
    }
}