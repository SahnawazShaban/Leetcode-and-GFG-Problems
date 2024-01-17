"""
Mirror Tree

Easy

Given a Binary Tree, convert it into its mirror.
          

Example 1:
Input:
      1
    /  \
   2    3
Output: 3 1 2
Explanation: The tree is
   1    (mirror)  1
 /  \    =>      /  \
2    3          3    2
The inorder of mirror is 3 1 2


Example 2:
Input:
      10
     /  \
    20   30
   /  \
  40  60
Output: 30 10 60 20 40
Explanation: The tree is
      10               10
    /    \  (mirror) /    \
   20    30    =>   30    20
  /  \                   /   \
 40  60                 60   40
The inroder traversal of mirror is
30 10 60 20 40.

Your Task:
Just complete the function mirror() that takes node as paramter  and convert it into its mirror. The printing is done by the driver code only.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 10^5
1 ≤ Data of a node ≤ 10^5

"""

# SOLUTION

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # DFS
        
        if root == None:
            return
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        root.left, root.right = root.right, root.left
        
        # -------------------------------------
        
        # BFS
        
        if root is None:
            return
        
        queue = deque([root])
    
        while queue:
            current_node = queue.popleft()
    
            # Swap the left and right subtrees at the current node
            current_node.left, current_node.right = current_node.right, current_node.left
    
            # Enqueue the left and right children if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
                
        '''
        Breadth-First Search (BFS):
        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(N), where N is the number of nodes.
        
        Depth-First Search (DFS):
        Time Complexity: O(N), where N is the number of nodes.
        Space Complexity: O(h) for recursive DFS (where h is the height), O(N) 
        '''