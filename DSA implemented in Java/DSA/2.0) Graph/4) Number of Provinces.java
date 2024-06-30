/*
  547. Number of Provinces
  Medium
  There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
  
  A province is a group of directly or indirectly connected cities and no other cities outside of the group.
  
  You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
  
  Return the total number of provinces.
  

  Example 1:
  Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
  Output: 2

  Example 2:
  Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
  Output: 3
   
  Constraints:
  1 <= n <= 200
  n == isConnected.length
  n == isConnected[i].length
  isConnected[i][j] is 1 or 0.
  isConnected[i][i] == 1
  isConnected[i][j] == isConnected[j][i]
*/


// SOLUTION

//DFS
/*
class Solution {
  public int findCircleNum(int[][] isConnected) {
      int V = isConnected.length;
      int[] vis = new int[V];
      int count = 0;
      
      for(int i = 0; i < V; i++){
          if (vis[i] == 0){
              count++;
              dfs(isConnected, i, vis);
          }
      }
      return count;
  }

  public void dfs(int[][] isConnected, int node, int[] vis) {
      vis[node] = 1;

      for(int i = 0; i<isConnected.length; i++){
          if (isConnected[node][i] == 1 && vis[i] == 0){
              dfs(isConnected, i, vis);
          }
      }
  }
}

*/

//BFS

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int V = isConnected.length;
        int[] vis = new int[V];
        int count = 0;

        for(int i = 0; i < V; i++){
            if (vis[i] == 0){
                count++;
                bfs(isConnected, i, vis);
            }
        }
        return count;
    }

    public void bfs(int[][] isConnected, int node, int[] vis) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(node);
        vis[node] = 1;

        while (!queue.isEmpty()) {
            int current = queue.poll();

            for (int i = 0; i < isConnected.length; i++) {
                if (isConnected[current][i] == 1 && vis[i] == 0) {
                    queue.offer(i);
                    vis[i] = 1;
                }
            }
        }
    }
}
