/*
Parenthesis Checker

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
balanced pairs, with 0 number of 
unbalanced bracket.

Example 2:
Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.

Example 3:
Input: 
([]
Output: 
false
Explanation: 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.
Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false. The printing is done automatically by the driver code.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 32000

Company Tags
Flipkart, Amazon, Microsoft, OYO, Rooms, Snapdeal, Oracle, Walmart, Adobe, Google, Yatra.com
*/

// SOLUTION

class Solution {
    // Function to check if brackets are balanced or not.
    static boolean ispar(String x) {
        int n = x.length();
        if (n == 0 || n % 2 == 1) {
            return false;
        }

        Stack<Character> s = new Stack<>();

        for (int i = 0; i < n; i++) {
            char ch = x.charAt(i);

            if (s.isEmpty() || ch == '(' || ch == '[' || ch == '{') {
                s.push(ch);
            } else {
                // If the current character is a closing bracket, check if it matches with the
                // top of the stack.
                if ((ch == ')' && s.peek() == '(') || (ch == ']' && s.peek() == '[')
                        || (ch == '}' && s.peek() == '{')) {
                    s.pop(); // If it matches, pop the top element from the stack.
                } else {
                    return false; // If it doesn't match, the brackets are not balanced.
                }
            }
        }
        return s.isEmpty();
    }
}