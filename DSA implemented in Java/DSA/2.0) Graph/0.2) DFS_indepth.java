/*
# Question:
              1
            /   \
           /     \
          2       6
         / \      /\
        /   \    /  \
       3     4   7   8
             \   /
              \ /
               5

# Adjacency List

(0, [])
(1, [2, 6])
(2, [1, 3, 4])
(3, [2])
(4, [2, 5])
(5, [4, 7])
(6, [1, 7, 8])
(7, [5, 6])
(8, [6])

*/

//SOLUTION

import java.util.ArrayList;
import java.util.List;

public class DFSGraph {
    
    // Function to perform DFS
    private static List<Integer> dfsGraph(int V, List<List<Integer>> adj) {
        // Array to track visited nodes
        boolean[] visited = new boolean[V + 1];
        
        // List to store the DFS traversal result
        List<Integer> dfsResult = new ArrayList<>();
        
        // Perform DFS from each node that hasn't been visited yet
        for (int i = 1; i <= V; i++) {
            if (!visited[i]) {
                dfs(i, adj, visited, dfsResult);
            }
        }
        
        return dfsResult;
    }
    
    // Recursive DFS function
    private static void dfs(int node, List<List<Integer>> adj, boolean[] visited, List<Integer> dfsResult) {
        visited[node] = true;
        dfsResult.add(node);
        
        // Traverse all adjacent nodes of the current node
        for (int neighbour : adj.get(node)) {
            if (!visited[neighbour]) {
                dfs(neighbour, adj, visited, dfsResult);
            }
        }
    }
    
    public static void main(String[] args) {
        // Example adjacency list representation of the graph
        int V = 8;
        List<List<Integer>> adj = new ArrayList<>();
        
        adj.add(new ArrayList<>());        // index 0 is unused
        adj.add(List.of(2, 6));            // Node 1
        adj.add(List.of(1, 3, 4));         // Node 2
        adj.add(List.of(2));               // Node 3
        adj.add(List.of(2, 5));            // Node 4
        adj.add(List.of(4, 7));            // Node 5
        adj.add(List.of(1, 7, 8));         // Node 6
        adj.add(List.of(5, 6));            // Node 7
        adj.add(List.of(6));               // Node 8
        
        List<Integer> check = dfsGraph(V, adj);
        System.out.println(check);
    }
}

/*
Time Complexity:
The function visits each vertex once and each edge once (since it checks all neighbors of each vertex). 
Therefore, the time complexity is O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
The space complexity is determined by the auxiliary data structures used. In your implementation, 
you use the visited list to keep track of visited nodes and the dfs_result list to store the order 
of visited nodes.

The visited list has a size of (V + 1) to represent the vertices, and the dfs_result list stores 
the order of visited nodes.

Therefore, the space complexity is O(V) for the visited list and O(V) for the dfs_result list, 
resulting in a total space complexity of O(V).

Please note that if the graph is represented using an adjacency matrix, the space complexity would be 
O(V^2), and if it's represented using an adjacency list (as in your case), it is O(V + E). In the worst 
case (a complete graph), E can be as large as V^2, so the time complexity would be O(V^2). However, in 
most practical cases, the number of edges is much smaller than the number of vertices, making the time 
complexity closer to O(V).
*/
