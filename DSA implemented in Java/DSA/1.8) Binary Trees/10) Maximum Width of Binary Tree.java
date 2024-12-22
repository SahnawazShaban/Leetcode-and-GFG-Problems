/*
662. Maximum Width of Binary Tree

Medium

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

*/

// Solution

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
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> qInt = new LinkedList<>();
        
        q.offer(root);
        qInt.offer(1);

        int maxi = 0;

        while(!q.isEmpty()){
            int n = q.size();
            int R = 0;
            int L = 0;

            for (int i = 0; i < n; i++){
                TreeNode temp = q.poll();
                int idx = qInt.poll();

                if(i == 0){
                    L = idx;
                }

                if(i == n-1){
                    R = idx;
                }

                if(temp.left != null){
                    q.offer(temp.left);
                    qInt.offer(idx*2);
                }

                if(temp.right != null){
                    q.offer(temp.right);
                    qInt.offer(idx*2+1);
                }
            }
            maxi = Math.max(maxi, R-L+1);
        }
        return maxi;
    }
}


/*
Time Complexity:
The time complexity of the widthOfBinaryTree function is O(N), where N is the number of nodes in the binary tree.

Explanation:
The function uses a breadth-first search (BFS) traversal, which visits each node once.
The while loop iterates through all the nodes in the tree, and within the loop, each node is processed exactly once.
Therefore, the time complexity is linear with respect to the number of nodes in the binary tree.
Space Complexity:
The space complexity of the widthOfBinaryTree function is O(W), where W is the maximum width of the binary tree.


Explanation:
The space complexity is primarily determined by the maximum number of nodes that can be present at any level during the BFS traversal.
The q deque is used to store nodes along with their corrected indices. In the worst case, this deque can contain all the nodes at the widest level.
The maximum width of the tree (W) corresponds to the maximum number of nodes that can be present at any level.
Therefore, the space complexity is O(W).

Auxiliary Space Analysis:

The auxiliary space used by the algorithm is not proportional to the total number of nodes in the tree but rather to the maximum number of nodes at any single level.
In the worst case, the space required would be proportional to the maximum width (W) of the binary tree.

Note:

The space complexity can be further optimized by using a single integer to represent the indices, as the corrected index is derived from the previous level's minimum index. This would reduce the space complexity to O(1) for the deque.
*/
