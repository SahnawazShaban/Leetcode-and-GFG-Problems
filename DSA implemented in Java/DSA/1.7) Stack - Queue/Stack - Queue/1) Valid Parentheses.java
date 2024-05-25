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

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.

"""

# SOLUTION

import java.util.HashMap;
import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        // Solution - 1
        if (s.length() % 2 != 0 || s.length() <= 1) {
            return false;
        }

        HashMap<Character, Character> temp_dict = new HashMap<>();
        temp_dict.put(')', '(');
        temp_dict.put('}', '{');
        temp_dict.put(']', '[');

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (stack.isEmpty() || stack.pop() != temp_dict.get(c)) {
                return false;
            }
        }

        return stack.isEmpty();

        // -------------------------------------

        // Solution - 2

        // Initialize an empty stack to track open brackets
        Stack<Character> stack2 = new Stack<>();
        // Mapping of closing brackets to their corresponding open brackets
        HashMap<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put('}', '{');
        closeToOpen.put(']', '[');
        closeToOpen.put(')', '(');

        for (char c : s.toCharArray()) {
            if (closeToOpen.containsKey(c)) { // If the character is a closing bracket
                if (!stack2.isEmpty() && stack2.peek() == closeToOpen.get(c)) {
                    stack2.pop(); // Matched an open bracket, so remove it from stack
                } else {
                    return false; // Mismatch or no open bracket to match
                }
            } else {
                stack2.push(c); // Character is an open bracket, push it onto stack
            }
        }

        return stack2.isEmpty(); // If stack is empty, all brackets are matched and valid
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String input = "(){}[]";
        System.out.println(solution.isValid(input)); // Output: true
    }
}
