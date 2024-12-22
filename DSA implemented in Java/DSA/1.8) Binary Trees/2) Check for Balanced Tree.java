/*
Check for Balanced Tree

Easy

Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5

Example 1:
Input:
      1
    /
   2
    \
     3 
Output: 0
Explanation: The max difference in height
of left subtree and right subtree is 2,
which is greater than 1. Hence unbalanced

Example 2:
Input:
       10
     /   \
    20   30 
  /   \
 40   60
Output: 1
Explanation: The max difference in height
of left subtree and right subtree is 1.
Hence balanced. 
Your Task:
You dont need to take input. Just complete the function isBalanced() that takes root node as parameter and returns true, if the tree is balanced else returns false.

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^9

Expected time complexity: O(N)
Expected auxiliary space: O(h) , where h = height of tree

*/


// SOLUTION

// DFS

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
    public boolean isBalanced(TreeNode root) {
        return getHeight(root) != -1;
    }

    //DFS
    private int getHeight(TreeNode root){
        if(root == null){
            return 0;
        }

        //Post order traversal
        int leftSubtreeHeight = getHeight(root.left);
        int rightSubtreeHeight = getHeight(root.right);

        if(leftSubtreeHeight == -1 || rightSubtreeHeight == -1){
            return -1;
        }

        if(Math.abs(leftSubtreeHeight - rightSubtreeHeight) > 1){
            return -1;
        }

        return 1 + Math.max(leftSubtreeHeight, rightSubtreeHeight);
    }
}
        
'''
Time Complexity:
The time complexity of the code is O(N), where N is the number of nodes in the binary tree. This is because each node is visited once, and for each node, constant time operations are performed.


Space Complexity:
The space complexity is O(H), where H is the height of the binary tree. In the worst case, the recursion depth would be equal to the height of the tree. Therefore, the space complexity is determined by the maximum depth of the recursion stack.

In the worst case, if the binary tree is unbalanced (skewed), the height becomes N (number of nodes), and the space complexity becomes O(N). In the best case, if the tree is balanced, the height is log(N) for a binary tree with N nodes, resulting in a space complexity of O(log(N)).

So, the overall space complexity is O(H), where H is the height of the binary tree.
'''


// BFS
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true; // An empty tree is considered balanced
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();

            int leftDepth = getDepth(node.left);
            int rightDepth = getDepth(node.right);

            if (Math.abs(leftDepth - rightDepth) > 1) {
                return false;
            }

            if (node.left != null) {
                queue.offer(node.left);
            }

            if (node.right != null) {
                queue.offer(node.right);
            }
        }

        return true;
    }

    private int getDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(getDepth(node.left), getDepth(node.right));
    }
}

// Example usage
class Main {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        Solution solution = new Solution();
        System.out.println(solution.isBalanced(root)); // Output: true or false based on tree structure
    }
}