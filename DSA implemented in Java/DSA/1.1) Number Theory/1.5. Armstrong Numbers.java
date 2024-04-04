/*
Armstrong Numbers

For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. Return "Yes" if it is a armstrong number else return "No".
NOTE: 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371

Example 1:

Input: N = 153
Output: "Yes"
Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153.
Hence answer is "Yes".
Example 2:

Input: N = 372
Output: "No"
Explanation: 372 is not an Armstrong number since 3^3 + 7^3 + 2^3 = 378.
Hence answer is "No".

Your Task:  
You dont need to read input or print anything. Complete the function armstrongNumber() which takes n as input parameter and returns "Yes" if it is a armstrong number else returns "No"..

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
100 ≤ n <1000
*/

// SOLUTION

class Solution {
    static String armstrongNumber(int n){
        int temp = n;
        // int t1 = n;
        int ans = 0;
        int count = 0;
        
        // If N digit Number
        // while (t1 != 0){
        //     t1 = t1/10;
        //     count++;
        // }
        
        while (temp != 0){
            int digit = temp%10;
            ans += (digit*digit*digit);
            temp /= 10;
        }
        
        if (n == ans){
            return "Yes";
        }
        return "No";
    }
}

