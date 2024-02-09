"""
Check for Children Sum Property in a Binary Tree

Medium

Given a binary tree having n nodes. Check whether all of its nodes have the value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it return 0.

For every node, data value must be equal to the sum of data values in left and right children. Consider data value as 0 for NULL child.  Also, leaves are considered to follow the property.

Example 1:
Input:
Binary tree
        35
      /    \
     20     15
    /  \    / \
   15   5  10  5
Output: 
1
Explanation: 
Here, every node is sum of its left and right child.

Example 2:
Input:
Binary tree
       1
     /   \
    4     3
   /  
  5    
Output: 
0
Explanation: 
Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isSumProperty() that takes the root Node of the binary tree as input and returns 1 if all the nodes in the tree satisfy the following properties, else it returns 0.

Expected Time Complexiy: O(n).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= n <= 10^5
1 <= Data on nodes <= 10^5

"""

# Solution 

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # Solution - 1
        
        if root is None:
            return 1
            
        if root.left is None and root.right is None:
            return 1
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            child_sum = 0
            
            if node.left is None and node.right is None:
                continue
            
            if node.left:
                queue.append(node.left)
                child_sum += node.left.data
                
            if node.right:
                queue.append(node.right)
                child_sum += node.right.data
                
            if child_sum != node.data:
                return 0
                    
        return 1
        
        # --------------------------------------------------------
        
        # Solution - 2
        '''
        if not root or (not root.left and not root.right):
            return 1
       
        l, r, sum1 = 1, 1, 0
       
        if root.left:
            l = self.isSumProperty(root.left)
            sum1 += root.left.data
        if root.right:
            r = self.isSumProperty(root.right)
            sum1 += root.right.data
       
        return int(root.data == sum1) and l and r
        '''

'''
Time Complexity:
The algorithm traverses each node in the binary tree exactly once.
Inside the while loop, each node is processed once, and its children (if any) are enqueued for future processing.
Therefore, the time complexity of the algorithm is directly proportional to the number of nodes in the binary tree.
In the worst-case scenario, the algorithm will visit every node once, resulting in a time complexity of O(n), 
where n is the number of nodes in the binary tree.

Space Complexity:
The space complexity is determined by the space used by the data structures involved in the algorithm.
The main data structure used is the queue, which stores the nodes to be processed.
At any given time, the queue contains at most one level of the binary tree.
In the worst-case scenario, the queue might contain all nodes of the last level of the binary tree.
For a perfectly balanced binary tree, the number of nodes in the last level is approximately half of the total number of nodes in the tree.
Therefore, the space complexity of the algorithm is O(n), where n is the number of nodes in the binary tree.
'''