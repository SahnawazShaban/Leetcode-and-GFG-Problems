/*
104. Maximum Depth of Binary Tree

Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

*/

// SOLUTION

//DFS

class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        int leftH = maxDepth(root.left);
        int rightH = maxDepth(root.right);

        return 1 + Math.max(leftH, rightH);
    }
}


//BFS
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        Deque<TreeNode> dq = new ArrayDeque<>();
        dq.push(root);
        int level_node_count = dq.size();
        int level = 0;

        while(!dq.isEmpty()){
            TreeNode temp = dq.pollFirst();

            if(temp.left != null){
                dq.offer(temp.left);
            }

            if(temp.right != null){
                dq.offer(temp.right);
            }

            level_node_count -= 1;

            if(level_node_count == 0){
                level += 1;
                level_node_count = dq.size();
            }
        }

        return level;
    }
}
