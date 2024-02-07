"""
Min distance between two given nodes of a Binary Tree
MediumAccuracy: 39.13%Submissions: 99K+Points: 4
Three 90 Challenge Extended On Popular Demand! Don't Miss Out Now 

banner
Given a binary tree with n nodes and two node values, a and b, your task is to find the minimum distance between them. The given two nodes are guaranteed to be in the binary tree and all node values are unique.

Example 1:
Input:
        1
      /  \
     2    3

a = 2, b = 3
Output: 
2
Explanation: 
We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2. 

Example 2:
Input:
        11
      /   \
     22  33
    /  \  /  \
  44 55 66   77

a = 77, b = 22
Output: 
3

Explanation: 
We need the distance between 77 and 22. Being at node 77, we need to take three steps ahead in order to reach node 22. The path followed will be: 77 -> 33 -> 11 -> 22. Hence, the result is 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findDist() which takes the root node of the tree and the two node values a and b as input parameters and returns the minimum distance between the nodes represented by the two given node values.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
2 <= n <= 10^5
0 <= Data of a node <= 10^9

"""

# Solution 

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self, root, a, b):
        def LCA(node, a, b):
            if node is None or node.data == a or node.data == b:
                return node
            
            left = LCA(node.left, a, b)
            right = LCA(node.right, a, b)
            
            if left and right:
                return node
            
            return left if left else right
        
        
        def distance(node, key, level):
            if not node:
                return -1
                
            if node.data == key:
                return level
                
            left = distance(node.left, key, level + 1)
            if left != -1:
                return left
                
            return distance(node.right, key, level + 1)

        lca = LCA(root, a, b)
        dist_a = distance(lca, a, 0)
        dist_b = distance(lca, b, 0)
        
        return dist_a + dist_b


'''
Time Complexity: O(n), where n is the number of nodes in the binary tree.
Space Complexity: O(n), where n is the height of the binary tree.
'''
    