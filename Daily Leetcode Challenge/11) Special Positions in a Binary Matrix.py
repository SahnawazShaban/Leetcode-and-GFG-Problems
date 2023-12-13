"""
1582. Special Positions in a Binary Matrix

Easy

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).


Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.

"""


# Solution 

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def col_sum(col_idx):
            return sum(row[col_idx] for row in mat)

        count = 0

        # traverse row index
        for row in mat:
            if sum(row) == 1:
                col_idx = row.index(1)
                # check if col sum function is 1 then add 1 in your count
                count += (col_sum(col_idx) == 1)

        return count

        # ----------------------------------

        # Solution - 2 - Brute Force
        '''
        ans = 0
        m = len(mat)
        n = len(mat[0])
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    continue
                    
                good = True
                for r in range(m):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                
                for c in range(n):
                    if c != col and mat[row][c] == 1:
                        good = False
                        break
                
                if good:
                    ans += 1
        
        return ans
        '''

        # Solution - 2 - Better
        '''
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans += 1

        return ans
        '''

        # -------------------------------------

        # Solution - 3

        '''
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(row[j] for row in mat) == 1:
                    count += 1
        return count


        Complexity :

        ⏱️ Time Complexity: O(n^3), where n is the size of the matrix.
        🚀 Space Complexity: O(1) - no extra space used.
        '''

        # -------------------------------------
        # Solution - 4
        
        '''
        rowSum = [sum(row) for row in mat]
        colSum = [sum(row[j] for row in mat) for j in range(len(mat[0]))]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    count += 1
        return count


        Complexity : 
        ⏱️ Time Complexity: O(n^2), where n is the size of the matrix.
        🚀 Space Complexity: O(n) - for the rowSum and colSum arrays.
        '''

        