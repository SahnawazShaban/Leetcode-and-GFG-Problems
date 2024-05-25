/*
Top View of Binary Tree

Medium

Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    / \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the left ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:
Input:
      1
   /    \
  2      3
Output: 2 1 3

Example 2:
Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 10^5
1 ≤ Node Data ≤ 10^5
*/

// SOLUTION

/*
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}
*/

class Pair{
    int state;
    Node root;
    
    public Pair(int state, Node root){
        this.state = state;
        this.root = root;
    }
}

class Solution
{
    //Function to return a list of nodes visible from the top view 
    //from left to right in Binary Tree.
    static ArrayList<Integer> topView(Node root)
    {
        ArrayList<Integer> ans = new ArrayList<>();
        if (root == null){
            return ans;
        }
        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(0, root));
        Map<Integer, Integer> map = new HashMap<>();
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        while (!q.isEmpty()){
            Pair temp = q.poll();
            Node node = temp.root;
            int state = temp.state;
            
            min = Math.min(min, state);
            max = Math.max(max, state);
            
            if (!map.containsKey(state)){
                map.put(state, node.data);
            }
            
            if (node.left != null){
                q.offer(new Pair(state-1, node.left));
            }
            
            if (node.right != null){
                q.offer(new Pair(state+1, node.right));
            }
        }
        
        for (int i = min; i <= max; i++){
            ans.add(map.get(i));
        }
        return ans;
    }
}

