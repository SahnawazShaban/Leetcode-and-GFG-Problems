/*
Print adjacency list

Easy

Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere.

Example 1:
Input:
V = 5, E = 7
edges = {(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)}

Output: 
{{1,4}, 
 {0,2,3,4}, 
 {1,3},
 {1,2,4},
 {0,1,3}}
Explanation:
Node 0 is connected to 1 and 4.
Node 1 is connected to 0,2,3 and 4.
Node 2 is connected to 1 and 3.
Node 3 is connected to 1,2 and 4.
Node 4 is connected to 0,1 and 3.

Example 2:
Input:
V = 4, E = 3
edges = {(0,3),(0,2),(2,1)}

Output: 
{{2,3} 
 {2}, 
 {0,1} 
 {0}}
Explanation:
Node 0 is connected to 2 and 3.
Node 1 is only connected to 2.
Node 2 is connected to 0 and 1.
Node 3 is only connected to 0.

Your task:
You don't need to read input or print anything. Your task is to complete the function printGraph() which takes the integer 
V denoting the number of vertices and edges as input parameters and returns the list of list denoting the adjacency list.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V + E)

Constraints:
1 ≤ V, E ≤ 10^5
*/

// SOLUTION

class Solution {
    public ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        ArrayList<Integer> bfsResult = new ArrayList<>();
        int[] visited = new int[V];
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0); // Start BFS from node 0
        visited[0] = 1; // Mark node 0 as visited
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            bfsResult.add(node);
            
            // Traverse all adjacent nodes of 'node'
            for (int neighbor : adj.get(node)) {
                if (visited[neighbor] == 0) { // If neighbor is not visited
                    visited[neighbor] = 1; // Mark neighbor as visited
                    queue.add(neighbor); // Add neighbor to the queue
                }
            }
        }
        
        return bfsResult;
    }
}
