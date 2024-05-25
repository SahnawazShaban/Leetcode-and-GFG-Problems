"""
Check whether BST contains Dead End

Medium

Given a Binary Search Tree that contains unique positive integer values greater than 0. The task is to complete the function isDeadEnd which returns true if the BST contains a dead end else returns false. Here Dead End means a leaf node, at which no other node can be inserted.


Example 1:
Input :   
               8
             /   \ 
           5      9
         /  \     
        2    7 
       /
      1     
Output : 
Yes
Explanation : 
Node 1 is a Dead End in the given BST.

Example 2:
Input :     
              8
            /   \ 
           7     10
         /      /   \
        2      9     13

Output : 
Yes
Explanation : 
Node 9 is a Dead End in the given BST.
Your Task: You don't have to input or print anything. Complete the function isDeadEnd() which takes BST as input and returns a boolean value.

Expected Time Complexity: O(N), where N is the number of nodes in the BST.
Expected Space Complexity: O(N)

Constraints:
1 <= N <= 1001
1 <= Value of Nodes <= 10001

"""


# SOLUTION

class Solution:
    def solve(self, root, mini, maxi):
        if root == None:
            return False
            
        if mini == maxi:
            return True
            
        left_side = self.solve(root.left, mini, root.data-1)
        right_side = self.solve(root.right, root.data+1, maxi)
            
        return left_side or right_side
        
    def isDeadEnd(self, root):
        
        return self.solve(root, 1, float('inf'))
        
# REFER : https://discuss.geeksforgeeks.org/comment/21f01238-90b0-4e44-bf16-4241a12b745e/practice
    
# ------------------------

class Solution:
    def isDeadEnd(self, root):
        # Initialize a queue for BFS traversal
        queue = deque()
        queue.append(root)
       
        # Sets to store visited nodes and leaf nodes
        visited_nodes, leaf_nodes = set(), set()
       
        # Perform BFS traversal
        while queue:
            current_node = queue.popleft()
           
            # Add current node to the visited set
            visited_nodes.add(current_node.data)
           
            # Enqueue left child if present
            if current_node.left:
                queue.append(current_node.left)
               
            # Enqueue right child if present
            if current_node.right:
                queue.append(current_node.right)
               
            # Add current node to the leaf set if it is a leaf node
            if not current_node.left and not current_node.right:
                leaf_nodes.add(current_node.data)
       
        # Check for dead ends in the leaf nodes
        for leaf in leaf_nodes:
            # If the leaf node is 1 and its next node is 2, or if the leaf node's neighbors are present, return 1
            if (leaf == 1 and 2 in visited_nodes) or (leaf - 1 in visited_nodes and leaf + 1 in visited_nodes):
                return 1
       
        # No dead end found
        return 0
    
