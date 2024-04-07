/*
Pascal Triangle
Easy
Given a positive integer N, return the Nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.
The elements can be large so return it modulo 109 + 7.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Example 1:
Input:
N = 4
Output: 
1 3 3 1
Explanation: 
4th row of pascal's triangle is 1 3 3 1.

Example 2:
Input:
N = 5
Output: 
1 4 6 4 1
Explanation: 
5th row of pascal's triangle is 1 4 6 4 1.
Your Task:
Complete the function nthRowOfPascalTriangle() which takes n, as input parameters and returns an array representing the answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(N^2)

Constraints:
1 ≤ N ≤ 10^3
*/

// SOLUTION

class Solution {
    ArrayList<Long> nthRowOfPascalTriangle(int n) {
        int mod = (int) 1e9 + 7;
        ArrayList<Long> list = new ArrayList<>();
        list.add(1L);

        if (n == 1) {
            return list;
        }

        ArrayList<Long> prev = nthRowOfPascalTriangle(n - 1);

        for (int i = 1; i < (n + 1) / 2; i++) {
            long val = (prev.get(i - 1) + prev.get(i)) % mod;
            list.add(val);
        }
        for (int i = n / 2 - 1; i >= 0; i--) {
            list.add(list.get(i));
        }
        return list;
    }
}
