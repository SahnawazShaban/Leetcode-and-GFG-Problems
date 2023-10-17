"""
Sum of Digit is Pallindrome or not

Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.

Example 1:

Input:
N=56
Output:
1
Explanation:
The digit sum of 56 is 5+6=11.
Since, 11 is a palindrome number.Thus,
answer is 1.
Example 2:

Input:
N=98
Output:
0
Explanation:
The digit sum of 98 is 9+8=17.
Since 17 is not a palindrome,thus, answer
is 0.

Your Task:
You don't need to read input or print anything.Your Task is to complete the function isDigitSumPalindrome() which takes a number N as input parameter and returns 1 if the Digit sum of N is a palindrome.Otherwise it returns 0.


Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)

Constraints:
1<=N<=109

"""

# SOLUTION

class Solution:
    def isDigitSumPalindrome(self,N):
        temp = N
        ans = 0
        while temp != 0:
            digit = temp%10
            ans += digit
            temp = temp//10
            
        reverse_ans = ans
        res = 0
        while reverse_ans != 0:
            digit = reverse_ans%10
            res = res*10 + digit
            reverse_ans = reverse_ans//10
            
        if ans == res:
            return 1
        return 0