"""
662. Maximum Width of Binary Tree

Medium

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 0
        q = deque([(root, 0)])

        while q:
            size = len(q)
            min_num = q[0][1]  # Starting index for current level

            first, last = 0, 0
            for i in range(size):
                cur_id = q[0][1] - min_num  # Corrected indentation
                node = q.popleft()[0]  # Corrected indentation

                if i == 0:
                    first = cur_id
                if i == size - 1:
                    last = cur_id

                if node.left:
                    q.append((node.left, cur_id * 2))
                if node.right:
                    q.append((node.right, cur_id * 2 + 1))

            ans = max(ans, last - first + 1)

        return ans

'''
Time Complexity:
The time complexity of the widthOfBinaryTree function is O(N), where N is the number of nodes in the binary tree.

Explanation:
The function uses a breadth-first search (BFS) traversal, which visits each node once.
The while loop iterates through all the nodes in the tree, and within the loop, each node is processed exactly once.
Therefore, the time complexity is linear with respect to the number of nodes in the binary tree.
Space Complexity:
The space complexity of the widthOfBinaryTree function is O(W), where W is the maximum width of the binary tree.


Explanation:
The space complexity is primarily determined by the maximum number of nodes that can be present at any level during the BFS traversal.
The q deque is used to store nodes along with their corrected indices. In the worst case, this deque can contain all the nodes at the widest level.
The maximum width of the tree (W) corresponds to the maximum number of nodes that can be present at any level.
Therefore, the space complexity is O(W).

Auxiliary Space Analysis:

The auxiliary space used by the algorithm is not proportional to the total number of nodes in the tree but rather to the maximum number of nodes at any single level.
In the worst case, the space required would be proportional to the maximum width (W) of the binary tree.

Note:

The space complexity can be further optimized by using a single integer to represent the indices, as the corrected index is derived from the previous level's minimum index. This would reduce the space complexity to O(1) for the deque.
'''
