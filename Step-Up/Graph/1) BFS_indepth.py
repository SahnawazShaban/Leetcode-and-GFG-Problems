# Question:
'''
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
'''
# Adjacency List
'''
(0, [])
(1, [2, 6])
(2, [1, 3, 4])
(3, [2])
(4, [2, 5])
(5, [4, 7])
(6, [1, 7, 8])
(7, [5, 6])
(8, [6])
'''

# SOLUTION

from collections import deque

def bfs(V, adj):
    visited = [0] * (V + 1)
    bfs_result = []
    queue = deque()

    queue.append(1)
    visited[1] = 1

    while queue:
        node = queue.popleft()
        bfs_result.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)

    return bfs_result


adj = [[], [2, 6], [1, 3, 4], [2], [2, 5], [4, 7], [1, 7, 8], [5, 6], [6]]
V = 8
check = bfs(V, adj)
print(check)

# ----------------------------------

# OUTPUT: [1, 2, 6, 3, 4, 7, 8, 5]

'''
Time Complexity: O(V + E), where V is the number of vertices and E is the number 
of edges in the graph. In the worst case, each vertex and each edge will be visited once.

Space Complexity: O(V), where V is the number of vertices. This is the space required 
for the visited array, bfs_result list, and the queue. In the worst case, all vertices 
are enqueued in the queue, and the visited array stores information for each vertex.
'''
