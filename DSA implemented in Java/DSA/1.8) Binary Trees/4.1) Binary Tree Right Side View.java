/*
199. Binary Tree Right Side View
Medium
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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
    public List<Integer> rightSideView(TreeNode root) {
        Stack<Integer> st = new Stack<>();
        dfs(root, 0, st);
        return st;
    }

    public void dfs(TreeNode root, int level, Stack<Integer> st){
        if (root == null){
            return;
        }

        if (st.size() == level){
            st.push(root.val);
        }

        if (root.right != null){
            dfs(root.right, level+1, st);
        }
        if (root.left != null){
            dfs(root.left, level+1, st);
        }
    }

    // ------------------------------------
    //BFS
    /*
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null)
            return new ArrayList();
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root);
        List<Integer> res = new ArrayList();
        
        while(!queue.isEmpty()){
            int size = queue.size();
            
            while (size -- > 0){
                TreeNode cur = queue.poll();
                if (size == 0)
                    res.add(cur.val);
                
                if (cur.left != null)
                    queue.offer(cur.left);
                if (cur.right != null)
                    queue.offer(cur.right);
            }
        }
        
        return res;
    }
    */
}