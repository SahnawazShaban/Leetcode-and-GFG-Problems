/*
The Celebrity Problem

Medium

A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.

Follow Up: Can you optimize it to O(N)
 

Example 1:
Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:
Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.


Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)


Constraints:
2 <= N <= 3000
0 <= M[][] <= 1
*/

// SOLUTION

import java.util.Stack;

class Solution {

    // Function to find if there is a celebrity in the party or not.
    public int celebrity(int[][] M, int n) {
        // Solution - 1
        
        // Iterate through each person in the group
        for (int person = 0; person < n; person++) {
            boolean isCelebrity = true;

            // Check if the current person knows anyone or if there is someone they don't know
            for (int otherPerson = 0; otherPerson < n; otherPerson++) {
                if (person != otherPerson && (M[person][otherPerson] == 1 || M[otherPerson][person] == 0)) {
                    isCelebrity = false;
                    break;
                }
            }

            // If the current person is identified as a celebrity, return their index
            if (isCelebrity) {
                return person;
            }
        }

        // If no celebrity is found, return -1
        return -1;
    }

    // -----------------------------------------
    // Solution - 2
    
    public int celebrityStackSolution(int[][] M, int n) {
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            stack.push(i);
        }
        
        while (stack.size() >= 2) {
            int i = stack.pop();
            int j = stack.pop();
            
            if (M[i][j] == 0) {
                // j is not a celebrity
                stack.push(i);
            } else {
                // i is not a celebrity
                stack.push(j);
            }
        }
        
        int celeb = stack.pop();
        
        for (int i = 0; i < n; i++) {
            if (i != celeb) {
                if (M[i][celeb] == 0 || M[celeb][i] == 1) {
                    return -1;
                }
            }
        }
        
        return celeb;
    }
}
