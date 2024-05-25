"""
543. Diameter of Binary Tree

Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100

"""

# SOLUTION

# Brute Force
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if node is None:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))

        if root is None:
            return 0

        left_subtree_depth = maxDepth(root.left)
        right_subtree_depth = maxDepth(root.right)

        # Calculate the diameter for the current node
        current_diameter = left_subtree_depth + right_subtree_depth

        # Recursively calculate diameters for left and right subtrees
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        # Return the maximum diameter among the current node and its subtrees
        return max(current_diameter, left_diameter, right_diameter)
    


'''
This brute-force solution has a higher time complexity compared to the optimized solution you provided earlier. 
The time complexity is exponential, O(2^N), where N is the number of nodes in the binary tree. This is because, 
for each node, we are recursively exploring both left and right subtrees.

The optimized solution you provided earlier, using a depth-first search, is more efficient with a time complexity 
of O(N) because it traverses each node only once.
'''

# Optimal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root == None:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)

            self.maxi = max(self.maxi, lh + rh)
            
            return 1 + max(lh, rh)

        
        self.maxi = 0
        dfs(root)

        return self.maxi
    

'''
Time Complexity: The time complexity is O(N), where N is the number of nodes in the binary tree. 
This is because each node is visited once during the depth-first search.

Space Complexity: The space complexity is O(H), where H is the height of the binary tree. 
This is the maximum depth of the call stack during the recursive depth-first search. In the worst case, 
H can be equal to N (the number of nodes), but for a balanced binary tree, H would be log(N).
'''