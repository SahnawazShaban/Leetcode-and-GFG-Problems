"""
124. Binary Tree Maximum Path Sum

Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000

"""

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Method - 1
        
        
        # Helper function to calculate the maximum path sum
        def maxPath(root):
            # Using nonlocal to access and modify the variable in the outer function
            nonlocal maxi
            
            # Base case: if the current node is None, return 0
            if root == None:
                return 0

            # Recursively calculate the maximum path sum for the left and right subtrees
            lh = maxPath(root.left)
            rh = maxPath(root.right)

            # If lh or rh is negative, set it to 0 (don't include negative values in the path)
            lh = 0 if lh < 0 else lh
            rh = 0 if rh < 0 else rh

            # Update the maximum path sum considering the current root node
            maxi[0] = max(maxi[0], lh + rh + root.val)

            # Return the maximum path sum considering the current root node
            return root.val + max(lh, rh)

        # Initialize maxi with the value of the root node
        maxi = [root.val]

        # Call the helper function to calculate the maximum path sum
        maxPath(root)

        # Return the final maximum path sum
        return maxi[0]


        # Method - 2
        '''
        def maxPathSumHelper(node):
            nonlocal max_sum

            # Base case: If the node is None, return 0
            if not node:
                return 0

            # Recursive calls to find the maximum path sum including and excluding the current node
            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))

            # Update the maximum path sum by considering the current node
            max_sum = max(max_sum, left_sum + right_sum + node.val)

            # Return the maximum path sum including the current node (to be used by the parent node)
            return max(left_sum, right_sum) + node.val

        # Initialize max_sum with a very small value
        max_sum = float('-inf')

        # Call the helper function to start the recursive process
        maxPathSumHelper(root)

        # Return the final maximum path sum
        return max_sum

        '''

# Mathode - 1: Analysis
'''
Time Complexity:
The time complexity of the maxPathSum function is O(N), where N is the number of nodes in the binary tree.
The reason is that each node is visited once in the recursive function maxPath.


Space Complexity:
The space complexity is O(H), where H is the height of the binary tree.
The space complexity is determined by the recursion stack. In the worst case, the recursion stack can go as deep as the height of the tree.
In the average case, the space complexity is O(log N) for a balanced binary tree.
In the worst case (skewed tree), the space complexity is O(N) when the tree is essentially a linked list.
So, in summary:

Time Complexity: O(N)
Space Complexity: O(H) or O(log N) on average, O(N) in the worst case
'''
