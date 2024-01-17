"""
Left View of Binary Tree

Easy

Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    / \
  4     5   6    7
   \
     8   

Example 1:
Input:
   1
 /  \
3    2
Output: 1 3

Example 2:
Input:
Output: 10 20 40

Your Task:
You just have to complete the function leftView() that returns an array containing the nodes that are in the left view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000

"""


# SOLUTION

# Node Class:
'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    def dfs(root, level, ds):
        if root == None:
            return
        
        if level == len(ds):
            ds.append(root.data)
            
        dfs(root.left, level+1, ds)
        dfs(root.right, level+1, ds)
    
    ds = []
    dfs(root, 0, ds)
    
    return ds