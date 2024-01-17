"""
987. Vertical Order Traversal of a Binary Tree

Hard

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

"""

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Output
        # [[0],[1],[3,2],[4]]
        # Expected
        # [[0],[1],[3,2,2],[4]]
        # defaultdict to store values at each vertical position
        nodes = defaultdict(lambda: defaultdict(list))
        # Initialize deque with root and its coordinates (x, y)
        todo = deque([(root, [0, 0])])

        # Perform level-order traversal
        while todo:
            node, (x, y) = todo.popleft()
            # Append node value to the corresponding position in the defaultdict
            nodes[x][y].append(node.val)

            # Enqueue left child with updated coordinates
            if node.left:
                todo.append((node.left, (x - 1, y + 1)))
            # Enqueue right child with updated coordinates
            if node.right:
                todo.append((node.right, (x + 1, y + 1)))

        # Construct the final result by sorting and organizing the values
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)

        return ans

'''
Time Complexity:
The time complexity is determined by the number of nodes in the binary tree, denoted as N. In the worst case, every node is visited once.

Traversal (While Loop): Each node is processed once, and each edge is traversed once. Hence, the traversal part is O(N).

Sorting: The sorting operation is done for each column and is performed after the traversal. The sorting step involves the values in each column and is done separately for each column. In the worst case, the total number of values across all columns is N. Sorting N values takes O(N log N) time.

Therefore, the overall time complexity is O(N + N log N), but in the context of big-O notation, the dominating factor is the sorting operation. So, the simplified time complexity is O(N log N).


Space Complexity:
The space complexity is determined by the additional data structures used during the traversal.

Deque (todo): The deque stores tuples for each node with its coordinates. In the worst case, the deque may hold all nodes in the tree, resulting in O(N) space.

Nested Defaultdict (nodes): The defaultdict is used to organize nodes based on their vertical and horizontal positions. In the worst case, it may hold all nodes in the tree. The space complexity for nodes is O(N).

Result (ans): The final result is a 2D list containing sorted values. In the worst case, it may also hold all nodes in the tree. The space complexity for the result is O(N).

Therefore, the overall space complexity is O(N).
'''