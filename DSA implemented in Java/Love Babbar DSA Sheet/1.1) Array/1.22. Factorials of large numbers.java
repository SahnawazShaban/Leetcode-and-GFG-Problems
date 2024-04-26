/*
Factorials of large numbers
Medium
Given an integer N, find its factorial. return a list of integers denoting the digits that make up the factorial of N.

Example 1:
Input: N = 5
Output: 120
Explanation : 5! = 1*2*3*4*5 = 120

Example 2:
Input: N = 10
Output: 3628800
Explanation :
10! = 1*2*3*4*5*6*7*8*9*10 = 3628800

Your Task:
You don't need to read input or print anything. Complete the function factorial() that takes integer N as input parameter and returns a list of integers denoting the digits that make up the factorial of N.

Expected Time Complexity : O(N2)
Expected Auxilliary Space : O(1)

Constraints:
1 ≤ N ≤ 1000
*/

// SOLUTION

class Solution {
    static ArrayList<Integer> factorial(int N) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(1); // add 1 to the ans array
        int carry = 0; // initilize carry as 0

        for (int i = 2; i <= N; i++) { // outer loop for all numbers till N
            for (int j = 0; j < ans.size(); j++) { // inner loop for logic
                int t = ans.get(j) * i + carry; // multiply and add carry
                ans.set(j, (t % 10)); // last digit to be stored at ans
                carry = t / 10; // remaining stored at carry
            }
            while (carry != 0) { // if carry is left add it to the ans
                ans.add(carry % 10);
                carry = carry / 10;
            }
            carry = 0; // make carry 0 for outer loop
        }

        Collections.reverse(ans); // reverse the ans for correct output
        return ans;
    }
}
