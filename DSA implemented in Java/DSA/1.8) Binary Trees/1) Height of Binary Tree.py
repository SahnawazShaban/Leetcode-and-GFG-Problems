"""
Height of Binary Tree

Easy

Given a binary tree, find its height.

Example 1:
Input:
     1
    /  \
   2    3
Output: 2

Example 2:
Input:
  2
   \
    1
   /
 3
Output: 3   
Your Task:
You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^9

"""


# SOLUTION

from collections import deque
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # Recursion : 
        '''
        if root == None:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        return 1 + max(l,r)
        '''
        
        '''
        Time Complexity:
        -----------------
        O(n) in the worst case, where n is the number of nodes in the tree. 
        This is because the function visits each node once in a balanced tree. 
        However, in the worst-case scenario of a skewed tree (e.g., a linear chain), 
        it might visit all nodes.
        
        Space Complexity:
        -----------------
        O(h) due to recursion stack space, where h is the height of the tree. 
        This is because the function calls itself recursively, 
        and each recursive call adds a new frame to the call stack. 
        The maximum depth of the recursion is equal to the height of the tree.
        '''
        
        # ______________________________________________________________
        
        # Using Level Order / BFS
        
        if root == None:
            return 0
           
        wrap_list = deque([root])
        next_level = 1
        level = 0
         
        while wrap_list:
            node = wrap_list.popleft()
            
            if node.left:
                wrap_list.append(root.left)
            
            if node.right:
                wrap_list.append(root.right)
             
            next_level -= 1
            
            if next_level == 0:
                level += 1
                 
                next_level = len(wrap_list)
             
        return level

        
        '''
        Time Complexity:
        O(n) in the worst case, where n is the number of nodes in the tree. 
        This is because the function visits each node exactly once during the level-order traversal.
        
        Space Complexity:
        O(w) in the worst case, where w is the maximum width of the tree 
        (the maximum number of nodes at any level). This is because the queue can hold up 
        to w nodes at any given time, representing a complete level of the tree.
        '''
