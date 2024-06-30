/*
Question:

        1
      /   \
     /     \
    2       6
   / \      /\
  /   \    /  \
 3     4   7   8
        \  /
         \/ 
          5

Adjacency List

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

# SOLUTION

import java.util.*;

public class BFSExample {

    // Method to perform BFS traversal on a graph
    public static List<Integer> bfs(int V, List<List<Integer>> adj) {
        List<Integer> bfsResult = new ArrayList<>(); // List to store BFS traversal result
        boolean[] visited = new boolean[V + 1]; // Array to keep track of visited nodes
        Queue<Integer> queue = new LinkedList<>(); // Queue for BFS

        queue.offer(1);  // Start BFS from node 1
        visited[1] = true; // Mark node 1 as visited

        while (!queue.isEmpty()) {
            int node = queue.poll(); // Get the front of the queue
            bfsResult.add(node); // Add the node to the result list

            // Visit all neighbors of the current node
            for (int neighbor : adj.get(node)) {
                if (!visited[neighbor]) { // If neighbor is not visited
                    visited[neighbor] = true; // Mark it as visited
                    queue.offer(neighbor); // Add it to the queue for further processing
                }
            }
        }

        return bfsResult; // Return the BFS traversal result
    }

    public static void main(String[] args) {
        int V = 8;  // Number of vertices in the graph
        List<List<Integer>> adj = new ArrayList<>(V + 1); // Adjacency list representation of the graph

        // Initialize adjacency list
        for (int i = 0; i <= V; i++) {
            adj.add(new ArrayList<>()); // Each node has an empty list of neighbors initially
        }

        // Adding edges to the graph
        adj.get(1).add(2);
        adj.get(1).add(6);
        adj.get(2).add(1);
        adj.get(2).add(3);
        adj.get(2).add(4);
        adj.get(3).add(2);
        adj.get(4).add(2);
        adj.get(4).add(5);
        adj.get(5).add(4);
        adj.get(5).add(7);
        adj.get(6).add(1);
        adj.get(6).add(7);
        adj.get(6).add(8);
        adj.get(7).add(5);
        adj.get(7).add(6);
        adj.get(8).add(6);

        List<Integer> result = bfs(V, adj); // Perform BFS traversal starting from node 1
        System.out.println(result);  // Output: [1, 2, 6, 3, 4, 7, 8, 5]
    }
}


/*
Time Complexity: O(V + E), where V is the number of vertices and E is the number 
of edges in the graph. In the worst case, each vertex and each edge will be visited once.

Space Complexity: O(V), where V is the number of vertices. This is the space required 
for the visited array, bfs_result list, and the queue. In the worst case, all vertices 
are enqueued in the queue, and the visited array stores information for each vertex.
*/

