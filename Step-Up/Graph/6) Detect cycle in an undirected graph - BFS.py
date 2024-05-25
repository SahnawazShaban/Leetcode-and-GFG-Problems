"""
Detect cycle in an undirected graph - BFS

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
from collections import deque

class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False]*V
        
        for i in range(V):
            if not visited[i]:
                if self.bfs(i, visited , adj):
                    return True
                    
        return False
        
        
    def bfs(self, start, visited , adj):
        queue = deque()
        queue.append((start, -1))
        visited[start] = True
        
        while queue:
            node, parent = queue.popleft()
            
            # Explore neighbors of the current node
            for neighbor in adj[node]:
                # If the neighbor is not visited, mark it as visited and enqueue it with the current node as the parent
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                    
                # If the neighbor is already visited and not the parent, a cycle is detected
                elif parent != neighbor:
                    return True
                    
        # No cycle found in the current connected component
        return False
     

'''
Time Complexity:
The outer loop in isCycle iterates through each vertex once, so it takes O(V) time.
The BFS function is called for each vertex exactly once, and inside the BFS, each edge is processed once. 
Therefore, the overall time complexity is O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
The visited array has a space complexity of O(V) as it stores whether each vertex has been visited or not.
The queue in BFS can have a maximum of O(V) vertices at any time.
The adjacency list adj also contributes to the space complexity, which is O(V + E), 
where V is the number of vertices and E is the number of edges.
'''
    