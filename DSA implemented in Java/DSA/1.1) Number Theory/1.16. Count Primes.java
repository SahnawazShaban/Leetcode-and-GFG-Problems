/*
204. Count Primes
Medium
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
 
Constraints:
0 <= n <= 5 * 10^6
*/

// SOLUTION

class Solution {
    public int countPrimes(int n) {
        // Solution - 1 - TLE
        /*
         * int count = 0;
         * 
         * for (int i=2; i<n; i++){
         * boolean flag = true;
         * for (int j = 2; j<i; j++){
         * if (i%j == 0){
         * flag = false;
         * break;
         * }
         * }
         * 
         * if (flag){
         * count++;
         * }
         * }
         * return count;
         */

        // Solution - 2

        boolean[] arr = new boolean[n];

        int ans = 0;

        for (int i = 2; i < n; i++) {
            if (arr[i]) {
                continue;
            }
            ans += 1;

            for (long j = (long) i * i; j < n; j += i) {
                arr[(int) j] = true;
            }
        }
        return ans;
    }
}
