/*
Smallest subarray with sum greater than x
Easy
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

Example 1:
Input:
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
Explanation:
Minimum length subarray is 
{4, 45, 6}

Example 2:
Input:
A[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Explanation:
Minimum length subarray is {10}
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function smallestSubWithSum() which takes the array A[], its size N and an integer X as inputs and returns the required ouput.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, x ≤ 10^5
0 ≤ A[] ≤ 10^4
*/

// SOLUTION

class Solution {

    public static int smallestSubWithSum(int a[], int n, int x) {

        int sum = 0, res = Integer.MAX_VALUE;
        int j = 0;

        for (int i = 0; i < n; i++) {
            sum += a[i];

            while (sum > x && j <= i) {
                res = Math.min(res, i - j + 1);
                sum -= a[j];
                j++;
            }
        }
        if (res == Integer.MAX_VALUE) {
            res = 0;
        }
        return res;
    }
}
