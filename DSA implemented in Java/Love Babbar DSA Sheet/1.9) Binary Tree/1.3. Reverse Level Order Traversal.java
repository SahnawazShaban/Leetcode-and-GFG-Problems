/*
Reverse Level Order Traversal
Easy
Given a binary tree of size n, find its reverse level order traversal. ie- the traversal must begin from the last level.

Example 1:
Input :
        1
      /   \
     3     2

Output: 
3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1

Example 2:
Input :
       10
      /  \
     20   30
    / \ 
   40  60

Output: 
40 60 20 30 10
Explanation:
Traversing level 2 : 40 60
Traversing level 1 : 20 30
Traversing level 0 : 10

Your Task: 
You don't need to read input or print anything. Complete the function reverseLevelOrder() which takes the root of the tree as input parameter and returns a list containing the reverse level order traversal of the given tree.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 10^4
*/

// SOLUTION

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

class Tree {
    public ArrayList<Integer> reverseLevelOrder(Node node) {
        ArrayList<Integer> ans = new ArrayList<>();

        if (node == null) {
            return ans;
        }

        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);

        while (!queue.isEmpty()) {
            Node temp = queue.poll();
            ans.add(0, temp.data);

            if (temp.right != null) {
                queue.offer(temp.right);
            }
            if (temp.left != null) {
                queue.offer(temp.left);
            }

        }
        return ans;

        // --------------------------------------

        // Solution : using reverse function.
        /*
         * Queue<Node>q=new LinkedList<>();
         * ArrayList<Integer>ans=new ArrayList<>();
         * if(node==null){
         * return ans;
         * }
         * q.add(node);
         * 
         * while(!q.isEmpty()){
         * Node currnode=q.remove();
         * ans.add(currnode.data);
         * if(currnode.right!=null){
         * q.add(currnode.right);
         * }
         * if(currnode.left!=null){
         * q.add(currnode.left);
         * 
         * }
         * 
         * }
         * Collections.reverse(ans);
         * return ans;
         */
    }
}