"""
576. Out of Boundary Paths

Medium

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.


Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

"""


# SOLUTION

class Solution:
    def __init__(self):
        self.memo = None
        self.mod = 10**9 + 7

    def findPaths(self, m, n, maxMove, startRow, startColumn):
        self.memo = [[[-1 for k in range(maxMove + 1)] for j in range(n)] for i in range(m)]
        return self.findPathsHelper(m, n, maxMove, startRow, startColumn) % self.mod

    def findPathsHelper(self, m, n, maxMove, i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1  # Reached a boundary
        if maxMove == 0:
            return 0  # No more moves allowed

        if self.memo[i][j][maxMove] != -1:
            return self.memo[i][j][maxMove]

        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            res += self.findPathsHelper(m, n, maxMove - 1, ni, nj)

        self.memo[i][j][maxMove] = res % self.mod
        return self.memo[i][j][maxMove]
    
'''
Time Complexity: O(m * n * maxMove)
Space Complexity: O(m * n * maxMove)

where:
m is the number of rows in the grid,
n is the number of columns in the grid, and
maxMove is the maximum number of moves allowed.
'''