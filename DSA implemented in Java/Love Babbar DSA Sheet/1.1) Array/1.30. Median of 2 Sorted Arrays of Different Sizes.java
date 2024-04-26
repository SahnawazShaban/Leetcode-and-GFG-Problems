/*
Median of 2 Sorted Arrays of Different Sizes
Hard
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.

Example 1:
Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5

Example 2:
Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median. 

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints: 
0 ≤ m,n ≤ 10^6
1 ≤ array1[i], array2[i] ≤ 10^9

Company Tags
Amazon, Microsoft, Samsung, Google
*/

// SOLUTION

class GFG {
    static double medianOfArrays(int n, int m, int a[], int b[]) {
        int[] temp = new int[n + m];

        int i = 0, j = 0;
        int idx = 0;

        while (i < n && j < m) {
            if (a[i] < b[j]) {
                temp[idx++] = a[i++];
            } else {
                temp[idx++] = b[j++];
            }
        }

        while (i < n) {
            temp[idx++] = a[i++];
        }

        while (j < m) {
            temp[idx++] = b[j++];
        }

        int len = temp.length - 1;
        double ans = 0;
        if (temp.length % 2 == 0) {
            ans = temp[len / 2] + temp[(len / 2) + 1];
            return ans / 2;
        }

        return temp[len / 2];
    }
}
