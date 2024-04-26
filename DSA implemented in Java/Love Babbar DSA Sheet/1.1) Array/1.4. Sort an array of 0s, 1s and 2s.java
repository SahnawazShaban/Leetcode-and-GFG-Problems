/*
Sort an array of 0s, 1s and 2s
Medium
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated into ascending order.

Example 2:
Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated into ascending order.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10^6
0 <= A[i] <= 2
*/

// SOLUTION

class Solution {
    public static void swap(int a[], int l, int r) {
        int temp = a[l];
        a[l] = a[r];
        a[r] = temp;
    }

    public static void sort012(int a[], int n) {
        // DUTCH FLAG ALGORITHM
        int l = 0, m = 0, r = n - 1;

        while (m <= r) {
            if (a[m] == 0) {
                swap(a, l, m);
                l++;
                m++;
            } else if (a[m] == 1) {
                m++;
            } else {
                swap(a, m, r);
                r--;
            }
        }
    }
}
