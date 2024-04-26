/*
Sum of Digit is Pallindrome or not
School
Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.

Note: A Palindrome number is a number that stays the same when reversed. Example- 121 , 131 , 7 etc.

Example 1:
Input:
n = 56
Output: 1
Explanation:
The digit sum of 56 is 5+6=11.Since, 11 is a palindrome number.Thus, answer is 1.

Example 2:
Input:
n = 98
Output: 0
Explanation:
The digit sum of 98 is 9+8=17. Since 17 is not a palindrome,thus, answer is 0.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function isDigitSumPalindrome() which takes a number n as input parameter and returns 1 if the Digit sum of n is a palindrome. Otherwise, it returns 0.

Expected Time Complexity: O(log(n))
Expected Auxillary Space: O(1)

Constraints:
1 <= n <= 10^9
*/

// SOLUTION

class Solution {
    int isDigitSumPalindrome(int n) {
        int ans = 0;
        
        while (n != 0){
            int digit = n%10;
            ans += digit;
            n /= 10;
        }
        
        int temp = ans;
        int ans1 = 0;
        
        while (temp != 0){
            int digit = temp%10;
            ans1 = (ans1*10) + digit;
            temp /= 10;
        }
        
        if (ans == ans1){
            return 1;
        }
        return 0;
    }
}