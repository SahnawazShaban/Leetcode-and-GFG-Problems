"""
297. Serialize and Deserialize Binary Tree

Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000

"""


# SOLUTION

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []

        def dfs(node):
            if not node:
                ans.append('#')
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ' '.join(ans)

    def deserialize(self, data):
        data = collections.deque(data.split())

        def dfs():
            if not data:
                return None

            rootVal = data.popleft()

            if rootVal is '#':
                return None
            root = TreeNode(rootVal)
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



'''
Serialize Method:
Time Complexity: O(N), where N is the number of nodes in the binary tree. This is because the function visits each node exactly once during the depth-first traversal.
Space Complexity: O(N), as the serialized string will contain information about each node in the binary tree.

Deserialize Method:
Time Complexity: O(N), where N is the number of nodes in the binary tree. Similar to the serialize method, the function processes each node exactly once during the depth-first traversal.
Space Complexity: O(N), as the function uses a deque to store the split components of the input string. The maximum space required is proportional to the height of the binary tree, and in the worst case, it could be O(N) for a skewed tree.

Overall, both methods have a time complexity of O(N) and a space complexity of O(N).
'''
