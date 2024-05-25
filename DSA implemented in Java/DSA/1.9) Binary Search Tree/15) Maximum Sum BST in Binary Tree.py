"""
1373. Maximum Sum BST in Binary Tree

Hard

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.

Constraints:
The number of nodes in the tree is in the range [1, 4 * 10^4].
-4 * 10^4 <= Node.val <= 4 * 10^4

"""


# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        def traverse(root):
            '''return status_of_bst, size_of_bst, left_bound, right_bound'''
            nonlocal res
            if not root: return 1, 0, None, None # this subtree is empty
            
            ls, l, ll, lr = traverse(root.left)
            rs, r, rl, rr = traverse(root.right)
            
            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1):
		        # this subtree is a BST
                size = root.val + l + r
                res = max(res, size)
                return 2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val)
            return 0, None, None, None # this subtree is not a BST
        
        traverse(root)
        return res


'''
Time Complexity:
The time complexity of the maxSumBST function is O(N), where N is the number of nodes in the binary tree. This is because the function visits each node exactly once during the depth-first traversal.

Space Complexity:
The space complexity is O(H), where H is the height of the binary tree. This is because the recursive calls in the traverse function form a call stack, and the maximum height of the call stack is proportional to the height of the tree. In the worst case, when the tree is skewed, the height could be O(N), leading to O(N) space complexity. In balanced cases, the space complexity would be O(log N).

In summary, the time complexity is O(N), and the space complexity is O(H) where H is the height of the binary tree.
'''
