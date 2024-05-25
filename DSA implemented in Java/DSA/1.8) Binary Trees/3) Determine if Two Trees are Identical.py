"""
Determine if Two Trees are Identical

Easy

Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.

Example 1:
Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: 
Yes
Explanation: 
There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.

Example 2:
Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: 
No
Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.
Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical() that takes two roots as parameters and returns true or false. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 10^5
1 <=Data of a node <= 10^9

"""


# SOLUTION

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # DFS
        Check if both nodes are None (empty trees) or have the same value
        if root1 is None or root2 is None:
            return root1 == root2

        # Check if the current nodes have the same value
        # and recursively check the left and right subtrees
        return (root1.data == root2.data) and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
               
        
        '''
        Time Complexity:
        The time complexity of this algorithm is O(min(N, M)), where N and M are the numbers 
        of nodes in root1 and root2, respectively. The reason for this is that the algorithm 
        compares corresponding nodes and stops early if it finds a mismatch. In the worst case, 
        it needs to compare all nodes in the smaller tree.

        Space Complexity:
        The space complexity is O(min(H1, H2)), where H1 and H2 are the heights of 
        the trees rooted at root1 and root2. This space is used for the recursive 
        call stack. In the worst case, the algorithm may need to recurse to the 
        maximum depth of the smaller tree.
        '''
        
        # BFS
        queue1 = deque([root1]) if root1 else deque()
        queue2 = deque([root2]) if root2 else deque()

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            # Check if the current nodes have the same value
            if not node1 and not node2:
                continue
            elif not node1 or not node2 or node1.data != node2.data:
                return False

            # Enqueue the left and right children for both trees
            queue1.append(node1.left if node1 else None)
            queue1.append(node1.right if node1 else None)
            queue2.append(node2.left if node2 else None)
            queue2.append(node2.right if node2 else None)

        # Check if both queues are empty (all nodes compared)
        return not queue1 and not queue2
        
        
        '''
        Time and Space Complexity:
        The time complexity remains O(min(N, M)), where N and M are the numbers of nodes in 
        root1 and root2, respectively. The space complexity is O(min(N, M)) as well, as the 
        maximum number of nodes in the queue at any given time is determined by the smaller tree.
        '''
