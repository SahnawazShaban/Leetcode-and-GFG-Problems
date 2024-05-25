"""
Detect cycle in an undirected graph - DFS

Medium

Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:
Input:  
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1
Explanation: 
1->2->3->4->1 is a cycle.

Example 2:
Input: 
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation: 
No cycle in the graph.

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.


Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

"""

# SOLUTION

from typing import List

class Solution:
    #Function to detect cycle in an undirected graph.
    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [0]*V
	    
	    for i in range(V):
	        if not visited[i]:
                # If a cycle is detected, return True.
	            if self.dfs(visited, adj, i, -1):
	                return True
	                
        return False
	            

    def dfs(self, visited, adj, node, parent):
        visited[node] = 1
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                # Recursively call DFS on the neighbor.
                if self.dfs(visited, adj, neighbor, node):
                    return True
            # If the neighbor is already visited and is not the parent, a cycle is detected.
            elif neighbor != parent:
                return True
	    
        # If no cycle is detected in the current DFS traversal, return False.
	    return False
    

'''
Time Complexity:
The isCycle function iterates through all the vertices of the graph once, and for each unvisited vertex, it calls the dfs function.
In the worst case, the dfs function may visit all the vertices and edges in the graph.
Therefore, the overall time complexity is O(V + E), where V is the number of vertices, and E is the number of edges in the graph.

Space Complexity:
The space complexity is determined by the additional data structures used, mainly the visited list.
The visited list has a size of V, where V is the number of vertices in the graph.
The recursive depth of the dfs function is determined by the height of the recursion tree, which can be at most V.
Therefore, the overall space complexity is O(V).
'''