"""
Check for Balanced Tree

Easy

Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5

Example 1:
Input:
      1
    /
   2
    \
     3 
Output: 0
Explanation: The max difference in height
of left subtree and right subtree is 2,
which is greater than 1. Hence unbalanced

Example 2:
Input:
       10
     /   \
    20   30 
  /   \
 40   60
Output: 1
Explanation: The max difference in height
of left subtree and right subtree is 1.
Hence balanced. 
Your Task:
You don't need to take input. Just complete the function isBalanced() that takes root node as parameter and returns true, if the tree is balanced else returns false.

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^9

Expected time complexity: O(N)
Expected auxiliary space: O(h) , where h = height of tree

"""


# SOLUTION

#DFS

'''
class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self, root):
        # Check if the height difference is not -1 (indicating imbalance)
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        # Base case: leaf node (height is 0)
        if root is None:
            return 0

        # Recursive calls to find the heights of left and right subtrees
        lh = self.dfsHeight(root.left)
        rh = self.dfsHeight(root.right)

        # If either subtree is unbalanced, propagate the unbalanced status
        if lh == -1 or rh == -1:
            return -1

        # Check if the current subtree is balanced
        if abs(rh - lh) > 1:
            return -1

        # Return the height of the current subtree
        return 1 + max(lh, rh)
        
'''
Time Complexity:
The time complexity of the code is O(N), where N is the number of nodes in the binary tree. This is because each node is visited once, and for each node, constant time operations are performed.


Space Complexity:
The space complexity is O(H), where H is the height of the binary tree. In the worst case, the recursion depth would be equal to the height of the tree. Therefore, the space complexity is determined by the maximum depth of the recursion stack.

In the worst case, if the binary tree is unbalanced (skewed), the height becomes N (number of nodes), and the space complexity becomes O(N). In the best case, if the tree is balanced, the height is log(N) for a binary tree with N nodes, resulting in a space complexity of O(log(N)).

So, the overall space complexity is O(H), where H is the height of the binary tree.
'''


# BFS

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if not root:
            return True  # An empty tree is considered balanced

        queue = deque([(root, 1)])  # Each element in the queue is a tuple (node, depth)

        while queue:
            node, depth = queue.popleft()

            left_depth = self.get_depth(node.left)
            right_depth = self.get_depth(node.right)

            if abs(left_depth - right_depth) > 1:
                return False

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

        return True

    def get_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.get_depth(node.left), self.get_depth(node.right))