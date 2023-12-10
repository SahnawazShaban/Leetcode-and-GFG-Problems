"""
867. Transpose Matrix

Easy

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


Example 1:
Input: matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
Output: [
        [1,4,7],
        [2,5,8],
        [3,6,9]
        ]

Example 2:
Input: matrix = [
                [1,2,3],
                [4,5,6]
                ]
Output: [
        [1,4],
        [2,5],
        [3,6]
        ]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

"""


# Solution 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Solution - 1
        
        n = len(matrix)
        m = len(matrix[0])

        result = [[0]*n for i in range(m)]

        for i in range(n):
            for j in range(m):
                result[j][i] = matrix[i][j]

        return result
        

        # --------------------------------------

        # Solution - 2
        '''
        arr = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            arr.append(row)
        return arr
        '''

        # Time Complexity : O(m * n)
        # Space Complexity : O(m * n)

        # ----------------------------------------

        # Solution - 3
        # For square matrix, we can solve without using any extra space
        '''
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix
        '''
        