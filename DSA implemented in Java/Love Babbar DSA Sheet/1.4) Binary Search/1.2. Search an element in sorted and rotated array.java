/*
Search an element in sorted and rotated array
Easy
Given a sorted and rotated array A of N distinct elements which are rotated at some point, and given an element K. The task is to find the index of the given element K in array A.

Example 1:
Input:
N = 9
A[] = {5,6,7,8,9,10,1,2,3}
K = 10
Output: 5
Explanation: 10 is found at index 5.

Example 2:
Input:
N = 3
A[] = {3,1,2}
K = 1
Output: 1
User Task:
Complete Search() function and return the index of the element K if found in the array. If the element is not present, then return -1.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 10^7
0 ≤ Ai ≤ 10^8
1 ≤ K ≤ 10^8
*/

// SOLUTION

class Solution {
    static int Search(int array[], int target) {
        int i = 0;
        int j = array.length - 1;
        int n = array.length;

        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (array[mid] == target)
                return mid;
            else if (array[mid] > array[n - 1]) {
                if (target >= array[i] && target < array[mid])
                    j = mid - 1;
                else
                    i = mid + 1;
            } else {
                if (target > array[mid] && target <= array[j])
                    i = mid + 1;
                else
                    j = mid - 1;
            }
        }
        return -1;
    } // 8 9 10 2 3 4 5 6 7
}
