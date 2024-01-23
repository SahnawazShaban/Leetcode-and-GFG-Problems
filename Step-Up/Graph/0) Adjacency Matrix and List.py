def adjacencyMatrix(ipt, n, mg):
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        mg.append(temp)

    for (u, v) in ipt:
        mg[u][v] = 1
        mg[v][u] = 1

    return mg


def adjacencyList(ipt, n, graph):
    for i in range(n):
        graph[i] = []

    for (u, v) in ipt:
        graph[u].append(v)
        graph[v].append(u)


ipt = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]

print("Adjacency Matrix")
# Adjacency Matrix
mg = []
n = 6
adjacencyMatrix(ipt, n, mg)

for row in mg:
    print(row)

print("--------------------------------------")
print("Adjacency List")
# Adjacency List
graph = {}
n = 6
adjacencyList(ipt, n, graph)

for row in graph.items():
    print(row)
