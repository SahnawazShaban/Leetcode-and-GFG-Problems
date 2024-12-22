/*
Determine if Two Trees are Identical

Easy

Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.

Example 1:
Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: 
true
Explanation: 
There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.

Example 2:
Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: 
false
Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.
Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical() that takes two roots as parameters and returns true or false. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 10^5
1 <=Data of a node <= 10^9

*/


// SOLUTION

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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //DFS
        if(p == null && q == null){
            return true;
        }

        if(p == null || q == null){
            return false;
        }

        return (p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right));

        // ------------------

        //BFS
        Stack<TreeNode[]> st = new Stack<>();
        st.push(new TreeNode[]{p, q});

        while(!st.isEmpty()){
            TreeNode[] node = st.pop();
            TreeNode first = node[0];
            TreeNode second = node[1];

            if(first == null && second == null){
                continue;
            }
            if(first == null || second == null){
                return false;
            }

            if(first.val != second.val){
                return false;
            }

            // Push left and right children for comparison
            st.push(new TreeNode[]{first.left, second.left});
            st.push(new TreeNode[]{first.right, second.right});
        }
        return true;
    }
}