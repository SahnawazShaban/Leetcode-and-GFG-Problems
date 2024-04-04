/*
258. Add Digits
Easy
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
 
Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
 
Constraints:
0 <= num <= 2^31 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
*/

// SOLUTION

class Solution {
    public int addDigits(int num) {
        // Solution - 1
        /*
        if (num >= 0 && num <= 9){
            return num;
        }
        else if (num % 9 == 0){
            return 9;
        }
        else {
            return num % 9;
        }
        */

        // Solution - 2 (Recursive Approach)
        if (num < 10){
            return num;
        }

        int ans = 0;

        while (num > 0){
            ans += (num % 10);
            num /= 10;
        }

        return addDigits(ans);
    }
}
