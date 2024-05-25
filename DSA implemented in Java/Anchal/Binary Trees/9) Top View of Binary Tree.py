"""
Top View of Binary Tree

Medium

Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    / \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the left ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:
Input:
      1
   /    \
  2      3
Output: 2 1 3

Example 2:
Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 10^5
1 ≤ Node Data ≤ 10^5


"""

# SOLUTION

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque, defaultdict

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        v = []  # Resultant list for top view values
        mp = defaultdict(int)  # Dictionary to store top view values for each horizontal distance
        q = deque([(root, 0)])  # Queue to perform level order traversal
    
        while q:
            p = q.popleft()  # Dequeue the front element
            hd = p[1]  # Horizontal distance of the current node
            curr = p[0]  # Current node
    
            # If horizontal distance is not in the dictionary, add the current node's value
            if hd not in mp:
                mp[hd] = curr.data
    
            # Enqueue left and right children with updated horizontal distances
            if curr.left:
                q.append((curr.left, hd-1))
            if curr.right:
                q.append((curr.right, hd+1))
    
        # Collecting values in sorted order based on horizontal distance
        for value in sorted(mp.keys()):
            v.append(mp[value])
    
        return v

'''
Time Complexity:
The time complexity is O(N), where N is the number of nodes in the binary tree. 
This is because each node is processed once in the while loop, 
and each operation inside the loop takes constant time.

Space Complexity:
The space complexity is O(N) as well. In the worst case, 
the queue can have at most N/2 nodes at the maximum level of the binary tree,
and the dictionary (defaultdict) can also have at most N entries, 
where N is the number of nodes. Therefore, the overall space complexity is O(N).
'''

