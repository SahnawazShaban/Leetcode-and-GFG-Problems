/*
Kth element in Matrix
Medium
Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Example 1:
Input:
N = 4
mat[][] = 
        {{16, 28, 60, 64},
        {22, 41, 63, 91},
        {27, 50, 87, 93},
        {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
 

Example 2:
Input:
N = 4
mat[][] =     
        {{10, 20, 30, 40}
        {15, 25, 35, 45}
        {24, 29, 37, 48}
        {32, 33, 39, 50}}
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.


Your Task:
You don't need to read input or print anything. Complete the function kthsmallest() which takes the mat, N and K as input parameters and returns the kth smallest element in the matrix.
 

Expected Time Complexity: O(K*Log(N))
Expected Auxiliary Space: O(N)


Constraints:
1 <= N <= 50
1 <= mat[][] <= 10000
1 <= K <= N*N
*/

// SOLUTION

class Solution {
    public static int kthSmallest(int[][] mat, int n, int k) {
        // Solution - 1
        int[] arr = new int[n * n];

        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[idx++] = mat[i][j];
            }
        }

        Arrays.sort(arr);

        return arr[k - 1];

        // ......................................

        // Solution - 2 - Using Priority Queue

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                pq.offer(mat[i][j]);
                if (pq.size() > k) {
                    pq.poll();
                }
            }
        }

        return pq.peek();
    }
}