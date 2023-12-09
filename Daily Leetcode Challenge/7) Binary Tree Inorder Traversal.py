"""
94. Binary Tree Inorder Traversal

Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?

"""


# Solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Solution - 1
        
        '''
        if root == None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''

        # Solution - 2
        
        # Time Complexity : O(n)
        # Height of tree if tree is Skewed Binary Trees
        # Space Complexity : O(n) ≈ O(H)

        if root == None:
            return []
        
        stack = []
        res = []
        node = root
        
        while True:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0: # (if not stack) = (len(stack == 0))
                    break
                else:
                    node = stack.pop()
                    res.append(node.val)
                    node = node.right
        
        return res


