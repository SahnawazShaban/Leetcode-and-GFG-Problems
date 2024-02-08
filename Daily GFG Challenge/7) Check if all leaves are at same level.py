"""
Check if all leaves are at same level

Easy

Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. Return true if all leaf nodes are at the same level, and false otherwise.

Example 1:
Input:
Tree:
    1
   / \
  2   3
Output:
true
Explanation:
The binary tree has a height of 2 and the leaves are at the same level.

Example 2:
Input:
Tree:
     10
    /  \
  20   30
 /  \
10  15
Output:
false
Explanation:
The binary tree has a height of 3 and the leaves are not at the same level.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(height of tree)

Your Task:
Implement the function check() that checks whether all the leaf nodes in the given binary tree are at the same level or not. 
The function takes the root node of the tree as an input and should return a boolean value (true/false) based on the condition.

Constraints:
1 ≤ n ≤ 10^5

"""

# Solution 

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        if not root:
            return True
            
        queue = deque([(root,0)])
        leaf_level = None
        
        while queue:
            node, level = queue.popleft()
            
            if not node.left and not node.right:
                if leaf_level is None:
                    leaf_level = level
                elif level != leaf_level:
                    return False
                    
            if node.left:
                queue.append((node.left, level+1))
                
            if node.right:
                queue.append((node.right, level+1))
                
        return True
    

'''
Time Complexity:

In the worst-case scenario, we need to traverse all the nodes of the binary tree to determine if all the leaf nodes are at the same level or not.
Since we're using a breadth-first search (BFS) approach, each node is visited once.
Therefore, the time complexity is O(n), where n is the number of nodes in the binary tree.

Space Complexity:

We use a queue to perform BFS traversal.
At any given time, the queue can hold at most the number of nodes in a level, which is the width of the widest level in the binary tree.
In the worst case, the width of the widest level can be n/2 (in the case of a complete binary tree), where n is the total number of nodes.
Thus, the space complexity is O(n/2), which simplifies to O(n) in terms of big O notation.
Therefore, the time complexity of the check function is O(n), and the space complexity is O(n).
'''
    