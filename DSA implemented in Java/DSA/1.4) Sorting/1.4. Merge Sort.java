/*
Merge Sort
Medium
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.

Example 1:
Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9

Example 2:
Input:
N = 10
arr[] = {10 9 8 7 6 5 4 3 2 1}
Output:
1 2 3 4 5 6 7 8 9 10

Your Task:
You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

Expected Time Complexity: O(nlogn) 
Expected Auxiliary Space: O(n)

Constraints:
1 <= N <= 10^5
1 <= arr[i] <= 10^5
*/

// SOLUTION

class Solution {
    void merge(int arr[], int l, int m, int r) {
        int[] ans = new int[r - l + 1];

        int idx1 = l;
        int idx2 = m + 1;

        int x = 0;

        while (idx1 <= m && idx2 <= r) {
            if (arr[idx1] <= arr[idx2]) {
                ans[x++] = arr[idx1++];
            } else {
                ans[x++] = arr[idx2++];
            }
        }

        // individual sub-array

        while (idx1 <= m) {
            ans[x++] = arr[idx1++];
        }

        while (idx2 <= r) {
            ans[x++] = arr[idx2++];
        }

        // copy ans array to main array

        for (int i = 0; i < ans.length; i++) {
            arr[i + l] = ans[i];
        }
    }

    void mergeSort(int arr[], int l, int r) {
        if (l >= r) {
            return;
        }

        int mid = l + (r - l) / 2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}
