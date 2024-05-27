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
You don't need to take input. Just complete the function isBalanced() that takes root node as parameter and returns true, if the tree is balanced else returns false.

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^9

Expected time complexity: O(N)
Expected auxiliary space: O(h) , where h = height of tree

*/


// SOLUTION
/* 
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

// Depth-First Search (DFS)

class Solution {
    public boolean isBalanced(TreeNode root) {
        return dfsHeight(root) != -1;
    }

    private int dfsHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int lh = dfsHeight(root.left);
        if (lh == -1) {
            return -1;
        }

        int rh = dfsHeight(root.right);
        if (rh == -1) {
            return -1;
        }

        if (Math.abs(lh - rh) > 1) {
            return -1;
        }

        return 1 + Math.max(lh, rh);
    }
}
*/

// Breadth-First Search (BFS)

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;  // An empty tree is considered balanced
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            int leftDepth = getDepth(node.left);
            int rightDepth = getDepth(node.right);

            if (Math.abs(leftDepth - rightDepth) > 1) {
                return false;
            }

            if (node.left != null) {
                queue.add(node.left);
            }

            if (node.right != null) {
                queue.add(node.right);
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


// The TreeNode class in Java represents a node in the binary tree, similar to the TreeNode class in Python.

// DFS Approach:

// The Solution class contains the isBalanced method and the dfsHeight helper method.
// isBalanced checks if the height difference is not -1, indicating an imbalance.
// dfsHeight recursively calculates the height of the left and right subtrees. If an imbalance is detected, it returns -1.

// BFS Approach:

// The Solution class also provides a BFS approach with the isBalanced and getDepth methods.
// isBalanced uses a queue to traverse the tree level by level.
// getDepth is a helper method that computes the depth of a given node.