/*
907. Sum of Subarray Minimums

Medium

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.


Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

*/

// SOLUTION

import java.util.Stack;

class Solution {
    public int sumSubarrayMins(int[] arr) {
        // Add sentinel values to the array to handle edge cases
        int n = arr.length;
        int[] newArr = new int[n + 2];
        System.arraycopy(arr, 0, newArr, 1, n);
        newArr[0] = Integer.MIN_VALUE;
        newArr[n + 1] = Integer.MIN_VALUE;
        n += 2;

        Stack<Integer> st = new Stack<>(); // Monotonic stack to track indices
        long res = 0; // Variable to store the final result

        // Traverse the array
        for (int i = 0; i < n; i++) {
            // While the stack is not empty and the current element is less than the element at the top of the stack
            while (!st.isEmpty() && newArr[st.peek()] > newArr[i]) {
                int mid = st.pop(); // Pop the top of the stack
                int left = st.peek(); // The left boundary of the subarray
                int right = i; // The right boundary of the subarray

                // Calculate the contribution of the popped element to the result
                // The contribution is the product of the value of the popped element,
                // the distance between the popped element and the element to its left,
                // and the distance between the popped element and the current element.
                res += (long)newArr[mid] * (mid - left) * (right - mid);
            }

            st.push(i); // Push the current index onto the stack
        }

        // Return the result modulo 10^9 + 7
        return (int)(res % (1_000_000_007));
    }
}