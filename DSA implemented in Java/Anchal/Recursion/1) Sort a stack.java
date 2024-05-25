/* 
Sort a stack

Medium

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:
Input:
Stack: 3 2 1
Output: 3 2 1

Example 2:
Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2

Your Task: 
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.

Constraints:
1<=N<=100

*/

// SOLUTION
/* 
private void insertSort(Stack<Integer> s, int temp) {
    if (s.isEmpty() || s.peek() <= temp) {
        s.push(temp);
        return;
    }

    int val = s.pop();
    insertSort(s, temp);
    s.push(val);
}

// Brute force approach (iterative sorting)
public Stack<Integer> bruteForceSort(Stack<Integer> s) {
    int n = s.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (s.get(i) > s.get(j)) {
                int temp = s.get(i);
                s.set(i, s.get(j));
                s.set(j, temp);
            }
        }
    }
    return s;
}
*/

import java.util.Stack;

class Solution {

    // Function to insert an element into a sorted stack
    private void insertSort(Stack<Integer> s, int temp) {
        if (s.isEmpty() || s.peek() <= temp) {
            s.push(temp);
            return;
        }

        int val = s.pop();
        insertSort(s, temp);
        s.push(val);
    }

    // Function to sort the stack such that the top element is max
    public void Sorted(Stack<Integer> s) {
        if (s.isEmpty()) {
            return;
        }

        int temp = s.pop();
        Sorted(s);
        insertSort(s, temp);
    }
}
