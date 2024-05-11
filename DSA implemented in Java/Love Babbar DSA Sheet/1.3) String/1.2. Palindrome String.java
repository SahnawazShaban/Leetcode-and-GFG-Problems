/*
Palindrome String
Easy
Given a string S, check if it is palindrome or not.

Example 1:
Input: S = "abba"
Output: 1
Explanation: S is a palindrome

Example 2:
Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome
Your Task:
You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.

Expected Time Complexity: O(Length of S)
Expected Auxiliary Space: O(1)

Constraints:
1 <= Length of S<= 2*10^5
*/

// SOLUTION

class Solution {
    int isPalindrome(String S) {
        int n = S.length();
        int s = 0, e = n - 1;

        while (s < e) {
            if (S.charAt(s) == S.charAt(e)) {
                s++;
                e--;
            } else {
                return 0;
            }
        }
        return 1;

        // ................................

        for (int i = 0; i < S.length() / 2; i++) {
            if (S.charAt(i) != S.charAt(S.length() - i - 1)) {
                return 0;
            }
        }
        return 1;

        // ................................

        StringBuilder reversed = new StringBuilder();

        // Reverse the string
        for (int i = S.length() - 1; i >= 0; i--) {
            reversed.append(S.charAt(i));
        }

        // Compare original string with reversed string
        if (S.equals(reversed.toString())) {
            return 1; // Palindrome
        } else {
            return 0; // Not a palindrome
        }
    }
};
