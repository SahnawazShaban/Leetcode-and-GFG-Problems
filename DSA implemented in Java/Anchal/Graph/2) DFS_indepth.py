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

def dfsGraph(V, adj):
    def dfs(node):
        visited[node] = 1
        dfs_result.append(node)

        for neighbour in adj[node]:
            if not visited[neighbour]:
                dfs(neighbour)

    visited = [0] * (V + 1)
    dfs_result = []

    for i in range(1, V):
        if not visited[i]:
            dfs(i)

    return dfs_result


adj = [[], [2, 6], [1, 3, 4], [2], [2, 5], [4, 7], [1, 7, 8], [5, 6], [6]]
V = 8
check = dfsGraph(V, adj)
print(check)


# OUTPUT: [1, 2, 3, 4, 5, 7, 6, 8]

'''
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
'''
