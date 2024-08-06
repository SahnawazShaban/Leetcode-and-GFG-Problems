/*
Pick from both sides!

Given an integer array A of size N.

You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3

Input 2:
 A = [1, 2]
 B = 1


Example Output
Output 1:
 8

Output 2:
 2


Example Explanation
Explanation 1:
 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8

Explanation 2:
 Pick element 2 from end as this is the maximum we can get

*/

// SOLUTION

import java.util.*;

public class Solution {
    // Function to find the maximum sum of a subarray of length B
    public int solve(ArrayList<Integer> A, int B) {
        int n = A.size();
        int maxSum = 0;
        
        // Calculate the initial sum of the first B elements
        int currentSum = 0;
        for (int i = 0; i < B; i++) {
            currentSum += A.get(i);
        }
        maxSum = currentSum;
        
        // Iterate over the remaining elements and update the sum
        for (int i = 0; i < B; i++) {
            currentSum = currentSum - A.get(B - 1 - i) + A.get(n - 1 - i);
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }
    
    // Alternative method to solve the problem
    public int solveAlternative(ArrayList<Integer> A, int B) {
        int n = A.size();
        int[] suff = new int[n + 1];
        
        suff[n - 1] = A.get(n - 1);
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = A.get(i) + suff[i + 1];
        }
        
        int prefSum = 0;
        int ans = suff[n - B];
        for (int i = 0; i < B; i++) {
            prefSum += A.get(i);
            int suffSum = suff[n - B + i + 1];
            ans = Math.max(ans, prefSum + suffSum);
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        int B = 2;
        
        System.out.println(sol.solve(A, B));           // Output for first method
        System.out.println(sol.solveAlternative(A, B)); // Output for alternative method
    }
}
