/*
Reversing the equation
Easy
Given a mathematical equation that contains only numbers and +, -, *, /. Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros.

Example 1:
Input:
S = "20-3+5*2"
Output: 2*5+3-20
Explanation: The equation is reversed with
numbers remaining the same.

Example 2:
Input: 
S = "5+2*56-2/4"
Output: 4/2-56*2+5
Explanation: The equation is reversed with
numbers remaining the same.
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseEqn() which takes the string S representing the equation as input and returns the resultant string representing the equation in reverse.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).

Constraints:
1<=|S|<=10^5
The string contains only the characters '0' - '9', '+', '-', '*', and '/'.
*/

// SOLUTION

class Solution{
    String reverseEqn(String S){
        String temp = "";
        StringBuilder ans = new StringBuilder();
        int n = S.length();

        for (int i = n - 1; i >= 0; i--) {
            // isDigit(char ch) is a static method of the Character class. It checks whether the specified character is a digit (0-9). In the code snippet.
            // The isDigit method is used to check whether the character at index i of the string S is a digit. If it is, the corresponding code block is executed.
            if (Character.isDigit(S.charAt(i))) {
                temp = S.charAt(i) + temp;
            } 
            else {
                ans.append(temp);
                ans.append(S.charAt(i));
                temp = "";
            }
        }

        ans.append(temp);
        return ans.toString();
    }
}

/*
In Java, for example, when you concatenate strings using the + operator or String.concat(), 
each concatenation creates a new string object, which can be inefficient if done repeatedly, 
particularly in loops or when building long strings. This is because strings in Java are immutable, 
meaning they cannot be changed after they are created.

StringBuilder, however, provides a mutable sequence of characters, allowing you to efficiently append, 
insert, or delete characters from the sequence without creating new string objects each time. 
This can lead to significant performance improvements in scenarios where string manipulation is intensive.
 */
