"""
98. Validate Binary Search Tree

Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

"""


# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# - Refer Book no.: 5
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.validBST(root, float('-inf'), float('inf'))

    def validBST(self, root, minVal, maxVal):
        if root == None:
            return True

        if root.val >= maxVal or root.val <= minVal:
            return False

        return self.validBST(root.left, minVal, root.val) and self.validBST(root.right, root.val, maxVal)

'''
The provided code checks whether a binary tree is a valid binary search tree (BST). It does so by recursively checking the validity of the left and right subtrees while maintaining the range of valid values (minVal and maxVal) for each node.

Time Complexity
The time complexity of this algorithm is O(N), where N is the number of nodes in the tree. In the worst case, the algorithm needs to visit all nodes once.

Space Complexity
The space complexity is O(H), where H is the height of the tree. In the worst case, the algorithm would have H recursive calls on the call stack. For a balanced BST, the height is log(N), leading to O(log N) space complexity. However, in the worst case (skewed tree), the height becomes N, resulting in O(N) space complexity.

In summary:
Time complexity: O(N)
Space complexity: O(H), where H is the height of the tree (O(log N) for a balanced tree, O(N) for a skewed tree).
'''
