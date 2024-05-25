"""
BFS of Graph

Easy

You are given a connected undirected graph. Perform a Breadth First Traversal of the graph.


Example 1:
Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
Output: 0 2 3 1 4

"""

# SOLUTION

class Solution:
    
    def bfsOfGraph(self, V, adj):
        visited = [0]*V
        bfs_result = []
        
        queue = deque()
        queue.append(0)
        visited[0] = 1
        
        while queue:
            node = queue.popleft()
            bfs_result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)
                    
        return bfs_result
    
    