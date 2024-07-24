/*
94. Binary Tree Inorder Traversal

Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?

*/


// Solution 
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        helper(root, ans);
        return ans;
    }

    private void helper(TreeNode root, List<Integer> ans){
        if(root == null){
            return;
        }

        helper(root.left, ans);
        ans.add(root.val);
        helper(root.right, ans);
    }
}
// Time - O(n)
// Space - O(logn), for skewed is O(n)


// Solution - 2
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // Time Complexity : O(n)
        // Height of tree if tree is Skewed Binary Trees
        // Space Complexity : O(n) ≈ O(H)

        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;

        while (true) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                if (stack.isEmpty()) {
                    break;
                } else {
                    node = stack.pop();
                    res.add(node.val);
                    node = node.right;
                }
            }
        }
        return res;
    }
}
