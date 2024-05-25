/*
Height of Binary Tree

Easy

Given a binary tree, find its height.

Example 1:
Input:
     1
    /  \
   2    3
Output: 2

Example 2:
Input:
  2
   \
    1
   /
 3
Output: 3   
Your Task:
You don't need to read input or print anything. Your task is to complete the function height() which takes root node of the tree as input parameter and returns an integer denoting the height of the tree. If the tree is empty, return 0. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^9
*/


// SOLUTION

//User function Template for Java

/* 
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
 */

 class Solution {
    //Function to find the height of a binary tree.
    int height(Node node) 
    {
        //DFS
        /*
        if (node == null){
            return 0;
        }
        
        int lh = height(node.left);
        int lr = height(node.right);
        
        return 1 + Math.max(lh,lr);
        */
        
        //BFS
        if (node == null){
            return 0;
        }
        Queue<Node> q = new LinkedList<>();
        q.offer(node);
        int height = 0;
        
        while (!q.isEmpty()){
            int n = q.size();
            height++;
            
            while (n-- > 0){
                Node temp = q.poll();
                
                if (temp.left != null){
                    q.offer(temp.left);
                }
                
                if (temp.right != null){
                    q.offer(temp.right);
                }
            }
        }
        return height;
        
    }
}

        
/* 
Time Complexity:
O(n) in the worst case, where n is the number of nodes in the tree. 
This is because the function visits each node exactly once during the level-order traversal.

Space Complexity:
O(w) in the worst case, where w is the maximum width of the tree 
(the maximum number of nodes at any level). This is because the queue can hold up 
to w nodes at any given time, representing a complete level of the tree.
*/
