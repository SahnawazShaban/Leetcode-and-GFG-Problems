/*
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
*/

// SOLUTION

// Brute force Approach

public class LongestPalindromicSubstring {

    // Helper function to check if a string is a palindrome
    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    // Function to find the longest palindromic substring
    public static String longestPalindromicSubstring(String s) {
        String longestPalindrome = "";
        int maxLength = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String substr = s.substring(i, j);
                if (isPalindrome(substr) && substr.length() > maxLength) {
                    maxLength = substr.length();
                    longestPalindrome = substr;
                }
            }
        }

        return longestPalindrome;
    }

    // Main method for testing
    public static void main(String[] args) {
        String s = "babadajajdbdhansdhdsna";
        System.out.println("Longest palindromic substring: " + longestPalindromicSubstring(s));
    }
}

// o/p: Longest palindromic substring: ansdhdsna

// -----------------------------------------------------

// Optimal Approach

class Solution {
    public String longestPalindrome(String s) {
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandPalindrome(s, i, i + 1);
            int len2 = expandPalindrome(s, i, i);

            int len = Math.max(len1, len2);

            if (end - start < len) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    int expandPalindrome(String s, int i, int j) {
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        return j - i - 1;
    }
}
