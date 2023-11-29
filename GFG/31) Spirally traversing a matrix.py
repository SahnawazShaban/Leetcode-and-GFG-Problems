"""
Spirally traversing a matrix

Medium

Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:
Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Example 2:
Input:
r = 3, c = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.

Your Task:
You dont need to read input or print anything. Complete the function spirallyTraverse() that takes matrix, r and c as input parameters and returns a list of integers denoting the spiral traversal of matrix. 

Expected Time Complexity: O(r*c)
Expected Auxiliary Space: O(r*c), for returning the answer only.

Constraints:
1 <= r, c <= 100
0 <= matrixi <= 100

"""

# SOLUTION

class Solution:
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        top, bottom = 0, r-1
        left, right = 0, c-1
        # dir = 0
        temp = []
        
        # only for 4x4 matrix
        '''
        while top <= bottom and left <= right:
            if dir == 0:
                for i in range(left,right+1):
                    temp.append(matrix[top][i])
                top += 1
                dir += 1
            elif dir == 1:
                for i in range(top,bottom+1):
                    temp.append(matrix[i][right])
                right -= 1
                dir += 1
            elif dir == 2:
                for i in range(right,left-1,-1):
                    temp.append(matrix[bottom][i])
                bottom -= 1
                dir += 1
            elif dir == 3:
                for i in range(bottom,top-1,-1):
                    temp.append(matrix[i][left])
                left += 1
                dir = 4
                
            dir = dir%4
        '''
        
        # for all matrix
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                temp.append(matrix[top][i])
            top += 1
            
            for i in range(top,bottom+1):
                temp.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right,left-1,-1):
                    temp.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom,top-1,-1):
                    temp.append(matrix[i][left])
                left += 1
                
        return temp