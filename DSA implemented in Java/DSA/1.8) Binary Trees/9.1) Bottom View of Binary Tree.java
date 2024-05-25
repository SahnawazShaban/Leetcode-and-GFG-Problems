/*
Bottom View of Binary Tree
Medium
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /  \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.

Note: The Input/Output format and Example given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.
 
Example 1:
Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.

Example 2:
Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30

Your Task:
This is a functional problem, you don't need to care about input, just complete the function bottomView() which takes the root node of the tree as input and returns an array containing the bottom view of the given tree.

Expected Time Complexity: O(N*logN).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 10^5
1 <= Data of a node <= 10^5
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

class Pair {
    int state;
    Node root;

    public Pair(int state, Node root) {
        this.state = state;
        this.root = root;
    }
}

class Solution {
    // Function to return a list containing the bottom view of the given tree.
    public ArrayList<Integer> bottomView(Node root) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        if (root == null) {
            return ans;
        }
        Map<Integer, Integer> map = new HashMap<>();

        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(0, root));

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        while (!q.isEmpty()) {
            Pair temp = q.poll();
            int state = temp.state;
            Node node = temp.root;

            min = Math.min(min, state);
            max = Math.max(max, state);

            map.put(state, node.data);

            // Top view BT. 
            // if (!map.containsKey(state)){
            // map.put(state, node.data);
            // }

            if (node.left != null) {
                q.offer(new Pair(state - 1, node.left));
            }

            if (node.right != null) {
                q.offer(new Pair(state + 1, node.right));
            }
        }

        for (int i = min; i <= max; i++) {
            ans.add(map.get(i));
        }

        return ans;
    }
}
