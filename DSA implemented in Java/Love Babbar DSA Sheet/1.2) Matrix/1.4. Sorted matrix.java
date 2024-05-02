/*
Sorted matrix
Basic
Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:
Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45] 
[27,29,37,48] 
[32,33,39,50]]
Output:
10 15 20 25 
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.

Example 2:
Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3 
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.


Expected Time Complexity:O(N^2LogN)
Expected Auxillary Space:O(N^2)


Constraints:
1<=N<=1000
1<=Mat[i][j]<=10^5

Company Tags:
Amazon, FactSet
*/

// SOLUTION

class Solution {
    int[][] sortedMatrix(int N, int Mat[][]) {

        ArrayList<Integer> list = new ArrayList<>();
        // NxN Matrix
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                list.add(Mat[i][j]);
            }
        }

        Collections.sort(list);
        int idx = 0;
        // NxN Matrix
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Mat[i][j] = list.get(idx++);
            }
        }
        return Mat;
    }
};
