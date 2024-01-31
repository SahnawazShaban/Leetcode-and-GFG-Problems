"""
1074. Number of Submatrices That Sum to Target

Hard

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 
Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

"""


# SOLUTION

# Approach-1 (Brute Force)
# T.C : O(m^3 * n^3)
# S.C : O(1)

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        
        result = 0
        
        # Trying all possible start points (x, y)
        for start_row in range(m):
            for start_col in range(n):
                
                # Trying all possible ending points (x', y')
                for end_row in range(start_row, m):
                    for end_col in range(start_col, n):

                        # Now iterating the start points and end points
                        cumSum = 0
                        for i in range(start_row, end_row + 1):
                            for j in range(start_col, end_col + 1):
                                cumSum += matrix[i][j]
                        
                        if cumSum == target:
                            result += 1
                        
        return result

# Example Usage:
# matrix = [[0,1,0],[1,1,1],[0,1,0]]
# target = 0
# solution = Solution()
# result = solution.numSubmatrixSumTarget(matrix, target)
# print(result)

# ----------------------------

# Approach-2 (Using prefix sum)
# T.C : O(n^2 * m)
# S.C : O(m)

from typing import List
# Optimal Approach

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # First take the cumulative sum row-wise
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c-1]

        # Now, you need to find the "No. of subarrays with sum k" in downward direction
        result = 0
        for startCol in range(cols):
            for currCol in range(startCol, cols):
                # We need to find all sub matrices sum

                # Now comes the concept of "No. of subarrays with sum k"
                mp = {0: 1}
                cumSum = 0
                # Go downwards row wise
                for r in range(rows):
                    cumSum += matrix[r][currCol] - (matrix[r][startCol-1] if startCol > 0 else 0)

                    if cumSum - target in mp:
                        result += mp[cumSum - target]

                    mp[cumSum] = mp.get(cumSum, 0) + 1

        return result
    

# Example usage:
# solution = Solution()
# matrix = [[0,1,0],[1,1,1],[0,1,0]]
# target = 0
# result = solution.numSubmatrixSumTarget(matrix, target)
# print(result)
