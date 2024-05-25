/*
100. Same Tree
Easy
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
*/

// SOLUTION

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null) {
            return false;
        }

        return ((p.val == q.val) && (isSameTree(p.left, q.left)) && (isSameTree(p.right, q.right)));

        // -------------------------------

        // BFS

        // Create queues for both trees.
        Queue<TreeNode> queue1 = new LinkedList<>();
        Queue<TreeNode> queue2 = new LinkedList<>();

        // Start by adding the root nodes of both trees to their respective queues.
        queue1.offer(p);
        queue2.offer(q);

        while (!queue1.isEmpty() && !queue2.isEmpty()) {
            TreeNode node1 = queue1.poll();
            TreeNode node2 = queue2.poll();

            // If the values of the current nodes are not equal, the trees are not
            // identical.
            if (node1 == null && node2 == null) {
                continue;
            }
            if (node1 == null || node2 == null || node1.val != node2.val) {
                return false;
            }

            // Add the left and right children of both nodes to their respective queues.
            queue1.offer(node1.left);
            queue1.offer(node1.right);
            queue2.offer(node2.left);
            queue2.offer(node2.right);
        }

        // If both queues are empty, the trees are identical.
        return queue1.isEmpty() && queue2.isEmpty();
    }

    // ---------------------------

    public boolean isSameTree(TreeNode p, TreeNode q) {
        String hash1 = computeTreeHash(p);
        String hash2 = computeTreeHash(q);
        return hash1.equals(hash2);
    }

    private String computeTreeHash(TreeNode node) {
        if (node == null) {
            return "null";
        }
        String leftHash = computeTreeHash(node.left);
        String rightHash = computeTreeHash(node.right);
        return "(" + node.val + leftHash + rightHash + ")";
    }
}