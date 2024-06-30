/*
BFS of Graph

Easy

You are given a connected undirected graph. Perform a Breadth First Traversal of the graph.


Example 1:
Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
Output: 0 2 3 1 4

*/

// SOLUTION

import java.util.*;

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

    
    