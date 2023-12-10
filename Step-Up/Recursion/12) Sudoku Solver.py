'''
37. Sudoku Solver
Solved
Hard
Topics
Companies
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
                ]

Output:board = [["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"]
                ]

Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

'''

# SOLUTION

class Solution:
    def isValid(self, board, row, col, char):
        for i in range(9):
            if board[i][col] == char:
                return False
            if board[row][i] == char:
                return False
            if board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] == char:
                return False

        return True


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == ".":
                    for ch in "123456789":
                        if self.isValid(board,i,j,ch):
                            board[i][j] = ch
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True


        '''
        Time Complexity: O(9^(n^2)), in the worst case, for each cell in the n^2 board, we have 9 possible numbers.

        Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.
        '''
                            