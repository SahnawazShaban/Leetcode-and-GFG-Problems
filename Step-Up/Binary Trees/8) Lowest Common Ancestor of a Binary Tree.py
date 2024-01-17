"""
236. Lowest Common Ancestor of a Binary Tree

Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.

"""

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Optimal
        # Base case: if the root is None or either p or q, return the root
        if root == None or root == p or root == q:
            return root

        # Recursive calls to find the LCA in the left and right subtrees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If one of the subtrees returned None, return the other one
        if l == None:
            return r
        elif r == None:
            return l
        else:  # If both l and r are not None, the current root is the LCA
            return root


'''
The time complexity of this algorithm is O(N), where N is the number of nodes in the binary tree, as each node is visited once. 

The space complexity is O(H), where H is the height of the binary tree, representing the maximum depth of the call stack during recursion. 

In a balanced tree, H is log(N), and in the worst case (skewed tree), H can be equal to N.
'''

# Brute Force
'''
def find_path(root, target, path):
    # Helper function to find the path from the root to the target node
    if not root:
        return False

    path.append(root)

    if root == target:
        return True

    if (root.left and find_path(root.left, target, path)) or (root.right and find_path(root.right, target, path)):
        return True

    path.pop()
    return False


def lowestCommonAncestor(root, p, q):
    # Brute force approach to find the lowest common ancestor

    # Find paths from root to p and q
    path_p = []
    path_q = []

    find_path(root, p, path_p)
    find_path(root, q, path_q)

    # Compare paths to find the lowest common ancestor
    lca = None
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        lca = path_p[i]
        i += 1

    return lca
'''

'''
This brute force solution has a time complexity of O(N^2) in the worst case, where N is the number of nodes in the tree. 
This is because, for each node, the algorithm may traverse the path from the root to that node twice. 
The space complexity is O(N) due to the storage of paths.
'''