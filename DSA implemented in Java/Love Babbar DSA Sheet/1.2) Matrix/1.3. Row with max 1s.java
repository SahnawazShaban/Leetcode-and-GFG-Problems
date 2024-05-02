/*
Row with max 1s
Medium
Given a boolean 2D array of n x m dimensions, consisting of only 1's and 0's, where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:
Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based indexing).

Example 2:
Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:  
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.
 

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, M ≤ 10^3
0 ≤ Arr[i][j] ≤ 1

// ----------------------------------------------------------

2643. Row With Maximum Ones
Easy
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.

Example 1:
Input: mat = [[0,1],[1,0]]
Output: [0,1]
Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. 

Example 2:
Input: mat = [[0,0,0],[0,1,1]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer is [1,2].

Example 3:
Input: mat = [[0,0],[1,1],[0,0]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].
 

Constraints:
m == mat.length 
n == mat[i].length 
1 <= m, n <= 100 
mat[i][j] is either 0 or 1.
*/

// SOLUTION

class Solution {
    int rowWithMax1s(int arr[][], int n, int m) {
        // Solution - 1 - Brute Force

        int count = 0;
        int maxi_ones = 0;
        int row = -1;

        for (int i = 0; i < n; i++) {
            count = 0;
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 1) {
                    count++;
                }
            }
            if (count > maxi_ones) {
                maxi_ones = count;
                row = i;
            }
        }
        return row;

        // -----------------------------

        // Solution - 2 - Optimal

        int row = 0, col = m - 1;
        int maxRowIndex = -1;

        while (row < n && col >= 0) {
            if (arr[row][col] == 1) {
                maxRowIndex = row;
                col--;
            } else {
                row++;
            }
        }
        return maxRowIndex;
    }
}

// ----------------------------------------------

class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int count = 0;
        int maxi_ones = 0;
        int row = -1;

        int[] ans = new int[2];
        for (int i = 0; i < n; i++) {
            count = 0;
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == 1) {
                    count++;
                }
            }
            if (count > maxi_ones) {
                maxi_ones = count;
                row = i;
                ans[0] = row;
                ans[1] = maxi_ones;
            }
        }
        return ans;
    }
}
