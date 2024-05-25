"""
103. Binary Tree Zigzag Level Order Traversal

Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

"""

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level = []  # Use a list for direct appending
            for _ in range(level_size):
                node = queue.popleft()

                # Append to the correct end based on left_to_right
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)  # Insert at the beginning

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Toggle left_to_right for next level
            left_to_right = not left_to_right
            result.append(level)  # No need to convert to list

        return result

'''
Time Complexity:
The time complexity is O(N), where N is the number of nodes in the binary tree.
Each node is processed once during the traversal, and the inner loop runs in O(N) overall.

Space Complexity:
The space complexity is O(W), where W is the maximum width of the binary tree (the maximum number of nodes at any level).
The space required is dominated by the queue (deque) and the level list, both of which can have a maximum of W elements in the worst case.


Outer While Loop:
This loop runs until the queue is empty, and each node is processed once.
The number of iterations of this loop is proportional to the number of nodes in the binary tree.
Therefore, the time complexity of the outer loop is O(N), where N is the number of nodes in the binary tree.

Inner For Loop:
This loop iterates over the nodes at the current level (level size).
For each node, a constant amount of work is done (popping from the queue, inserting into the level list, and enqueuing left and right children).
The number of iterations of this loop across all levels is also proportional to the number of nodes in the binary tree.

Therefore, the time complexity of the inner loop is also O(N).
Since the inner loop is nested within the outer loop, the overall time complexity is still O(N). The presence of two loops doesn't change the asymptotic complexity; it's still dominated by the number of nodes in the binary tree.
'''
