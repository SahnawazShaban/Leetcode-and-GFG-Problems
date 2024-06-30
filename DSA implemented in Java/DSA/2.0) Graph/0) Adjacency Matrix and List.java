import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GraphRepresentation {
    // Method to create adjacency matrix
    public static int[][] adjacencyMatrix(int[][] edges, int n) {
        int[][] mg = new int[n][n];
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            mg[u][v] = 1;
            mg[v][u] = 1;
        }
        return mg;
    }

    // Method to create adjacency list
    public static Map<Integer, List<Integer>> adjacencyList(int[][] edges, int n) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        return graph;
    }

    public static void main(String[] args) {
        int[][] edges = {
                { 0, 1 }, { 0, 2 }, { 0, 3 }, { 0, 4 },
                { 1, 3 }, { 2, 3 }, { 2, 4 }, { 2, 5 }, { 3, 5 }
        };
        int n = 6;

        // Adjacency Matrix
        System.out.println("Adjacency Matrix");
        int[][] mg = adjacencyMatrix(edges, n);
        for (int i = 0; i < mg.length; i++) {
            for (int j = 0; j < mg[i].length; j++) {
                System.out.print(mg[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("--------------------------------------");

        // Adjacency List
        System.out.println("Adjacency List");
        Map<Integer, List<Integer>> graph = adjacencyList(edges, n);
        for (Map.Entry<Integer, List<Integer>> entry : graph.entrySet()) {
            System.out.print(entry.getKey() + ": ");
            for (Integer neighbor : entry.getValue()) {
                System.out.print(neighbor + " ");
            }
            System.out.println();
        }
    }
}

/*
int[][] edges = {
    {0, 1}, {0, 2}, {0, 3}, {0, 4},
    {1, 3}, {2, 3}, {2, 4}, {2, 5}, {3, 5}
};
int n = 6;

Output
Adjacency Matrix
0 1 1 1 1 0 
1 0 0 1 0 0 
1 0 0 1 1 1 
1 1 1 0 0 1 
1 0 1 0 0 0 
0 0 1 1 0 0 

--------------------------------------
Adjacency List
0: 1 2 3 4 
1: 0 3 
2: 0 3 4 5 
3: 0 1 2 5 
4: 0 2 
5: 2 3 
*/
