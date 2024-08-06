/*
Sort array with squares!

Problem Description

Given a sorted array A containing N integers both positive and negative.
You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.
Try to this in O(N) time.


Problem Constraints
1 <= N <= 10^5.
-10^3 <= A[i] <= 10^3


Input Format
First and only argument is an integer array A.

Output Format
Return a integer array as described in the problem above.


Example Input
Input 1:
 A = [-6, -3, -1, 2, 4, 5]

Input 2:
 A = [-5, -4, -2, 0, 1]


Example Output
Output 1:
 [1, 4, 9, 16, 25, 36]

Output 2:
 [0, 1, 4, 16, 25]

*/

// SOLUTION

import java.util.*;

public class Solution {
    // Function to return the sorted squares of the elements of the array
    public ArrayList<Integer> solve(ArrayList<Integer> A) {
        int n = A.size();
        ArrayList<Integer> result = new ArrayList<>(Collections.nCopies(n, 0));
        int left = 0, right = n - 1;
        int index = n - 1;

        while (left <= right) {
            int leftSquare = A.get(left) * A.get(left);
            int rightSquare = A.get(right) * A.get(right);

            if (leftSquare > rightSquare) {
                result.set(index, leftSquare);
                left++;
            } else {
                result.set(index, rightSquare);
                right--;
            }

            index--;
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(-4, -1, 0, 3, 10));
        System.out.println(sol.solve(A));  // Output: [0, 1, 9, 16, 100]
    }
}
