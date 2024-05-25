"""
104. Maximum Depth of Binary Tree

Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

# SOLUTION

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        '''
        if root == None:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh, rh)
        '''

        # Level Order
        if root == None:
            return 0

        wrap_list = deque([root])
        level = 0
        nodes_level = 1
        
        while wrap_list:
            node = wrap_list.popleft()

            if node.left:
                wrap_list.append(node.left)

            if node.right:
                wrap_list.append(node.right)

            nodes_level -= 1
            if nodes_level == 0:
                level += 1

                nodes_level = len(wrap_list)

        return level
    