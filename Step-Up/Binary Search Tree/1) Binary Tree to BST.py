"""
Binary Tree to BST

Easy

Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
 
Example 1:
Input:
      1
    /   \
   2     3
Output: 
1 2 3
Explanation:
The converted BST will be 
      2
    /   \
   1     3

Example 2:
Input:
          1
       /    \
     2       3
   /        
 4       
Output: 
1 2 3 4
Explanation:
The converted BST will be

        3
      /   \
    2     4
  /
 1
Your Task:
You don't need to read input or print anything. Your task is to complete the function binaryTreeToBST() which takes the root of the Binary tree as input and returns the root of the BST. The driver code will print inorder traversal of the converted BST.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 10^5

"""


# SOLUTION

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    
    def binaryTreeToBST(self, root):
        node_list = []
        self.get_nodes(root, node_list)
        node_list.sort()
        self.inorder(root, node_list)
        return root
        
    def get_nodes(self, root, node_list):
        if root is None:
            return
        
        node_list.append(root.data)
        self.get_nodes(root.left, node_list)
        self.get_nodes(root.right, node_list)
    
    def inorder(self, root, node_list):
        if root is None:
            return
        
        self.inorder(root.left, node_list)
        root.data = node_list.pop(0)
        self.inorder(root.right, node_list)
        

'''
Time Complexity:
Getting Nodes (get_nodes): The get_nodes function traverses the entire binary tree once, visiting each node exactly once. Therefore, its time complexity is O(n), where n is the number of nodes in the binary tree.

Sorting Nodes (node_list.sort()): Sorting the node_list takes O(n log n) time in the worst case, where n is the number of nodes.

Inorder Traversal (inorder): The inorder function again traverses the entire binary tree once, visiting each node exactly once. This operation also has a time complexity of O(n), where n is the number of nodes.

The dominating factor is the sorting operation (O(n log n)), so the overall time complexity of your binaryTreeToBST method is O(n log n).


Space Complexity:
Node List (node_list): The node_list stores the data of all nodes in the binary tree, so its space complexity is O(n), where n is the number of nodes.

Recursion Stack: The space complexity of the recursion stack during the traversal is O(h), where h is the height of the binary tree.

The dominating factor is the space used by the node_list, so the overall space complexity of your binaryTreeToBST method is O(n).
'''
