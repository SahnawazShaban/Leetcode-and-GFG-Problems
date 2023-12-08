"""
606. Construct String from Binary Tree

Easy

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 
Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-1000 <= Node.val <= 1000

"""


# Solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            if not root:
                return

            res.append("(")  
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")

            preorder(root.left)
            preorder(root.right)

            res.append(")")

        preorder(root)
        return "".join(res)[1:-1] #Since I don't include the string's initial and end index, I add [1,-1] after the join function.


        # ____________________________________________________________________

    # Solution - 2
    '''
    
    # Step 1: Base case - if the root is None, return an empty string
    if root is None:
        return ""

    # Step 2: Start with the value of the current node as the result string
    result = str(root.val)

    # Step 3: Recursively process the left and right subtrees
    left_subtree = self.tree2str(root.left)
    right_subtree = self.tree2str(root.right)

    # Step 4: Check conditions to determine the final result
    if not left_subtree and not right_subtree:
        # Both left and right subtrees are empty, return the current result
        return result
    if not left_subtree:
        # Left subtree is empty, include empty parentheses for it and the right subtree
        return result + "()" + "(" + right_subtree + ")"
    if not right_subtree:
        # Right subtree is empty, include the left subtree
        return result + "(" + left_subtree + ")"

    # Both left and right subtrees are non-empty, include both in the result
    return result + "(" + left_subtree + ")" + "(" + right_subtree + ")"

    '''