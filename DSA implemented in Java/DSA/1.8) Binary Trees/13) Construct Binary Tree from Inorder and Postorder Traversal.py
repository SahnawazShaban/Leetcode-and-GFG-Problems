"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Medium

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

"""

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Brute Force
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build_tree_in_post(inorder, postorder):
            # Base case: If the inorder list is empty, return None
            if not inorder:
                return None
            
            # The last element in postorder is the root of the current subtree
            root_value = postorder.pop()
            root = TreeNode(root_value)
            
            # Find the index of the root value in the inorder traversal
            inorder_root_index = inorder.index(root_value)
            
            # Recursively build the right and left subtrees
            root.right = build_tree_in_post(inorder[inorder_root_index + 1:], postorder)
            root.left = build_tree_in_post(inorder[:inorder_root_index], postorder)
            
            # Return the root of the current subtree
            return root

        # Call the helper function to build the tree and return the root
        return build_tree_in_post(inorder, postorder)

'''
Time Complexity:
The time complexity is O(N^2), where N is the number of nodes in the binary tree.
The inorder.index(root_value) operation, performed for each node, has a worst-case time complexity of O(N) in each recursive call.

Space Complexity:
The space complexity is O(N) due to the recursion stack.
In the worst case, the recursion stack can go as deep as the height of the tree, which is O(N) for an unbalanced tree.

Important Note:
The current implementation with inorder.index for finding the index of the root value contributes to the quadratic time complexity. Using a hashmap to store the indices of values in the inorder list would improve the time complexity to O(N).
'''

    # ---------------------------------------------

    # Optimize
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap to store the indices of values in the inorder list
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build_tree_in_post(left, right):
            nonlocal postorder  # Allow access to the outer function's postorder list

            # Base case: If there are no elements in the subtree, return None
            if left > right:
                return None
            
            # The last element in postorder is the root of the current subtree
            root_value = postorder.pop()
            root = TreeNode(root_value)
            
            # Find the index of the root value in the inorder traversal
            inorder_root_index = inorder_map[root_value]
            
            # Recursively build the right and left subtrees
            root.right = build_tree_in_post(inorder_root_index + 1, right)
            root.left = build_tree_in_post(left, inorder_root_index - 1)
            
            # Return the root of the current subtree
            return root

        # Call the helper function to build the tree and return the root
        return build_tree_in_post(0, len(inorder) - 1)

'''
Time Complexity:
The time complexity is O(N), where N is the number of nodes in the binary tree.
The inorder_map allows finding the index of a value in O(1) time, resulting in an overall linear time complexity.

Space Complexity:
The space complexity is O(N) due to the recursion stack.
In the worst case, the recursion stack can go as deep as the height of the tree, which is O(N) for an unbalanced tree.
'''
