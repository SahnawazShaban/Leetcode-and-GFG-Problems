"""
Insert a node in a BST

Easy

Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. If K is already present in the BST, don't modify the BST.

Example 1:
Input:
     2
   /   \   
  1     3
K = 4
Output: 
1 2 3 4
Explanation: 
After inserting the node 4
Inorder traversal will be 1 2 3 4.

Example 2:
Input:
        2
      /   \
     1     3
             \
              6
K = 4
Output: 
1 2 3 4 6
Explanation: 
After inserting the node 4
Inorder traversal of the above tree will be 1 2 3 4 6.
Your Task:
You don't need to read input or print anything. Your task is to complete the function insert() which takes the root of the BST and Key K as input parameters and returns the root of the modified BST after inserting K. 
Note: The generated output contains the inorder traversal of the modified tree.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= Number of nodes initially in BST <= 10^5
1 <= K <= 10^9

"""


# SOLUTION

class Solution:
    #Function to insert a node in a BST.
    def insert(self,root, Key):
        # Recursive
        if root is None:
            return Node(Key)
        
        if root.data < Key:
            root.right = self.insert(root.right, Key)
        elif root.data > Key:
            root.left = self.insert(root.left, Key)
       
        return root
        
        # -------------------------------------
        
        # Iterative
        '''
        if not root:
            return Node(Key)  # If the tree is empty, return a new node with value Key.

        current = root
        while True:
            if Key < current.data:
                if current.left is None:
                    current.left = Node(Key)
                    break
                else:
                    current = current.left
            elif Key > current.data:
                if current.right is None:
                    current.right = Node(Key)
                    break
                else:
                    current = current.right
            else:
                # If K is already present in the BST, do nothing.
                break
    
        return root
        '''
    
    