/*
Get minimum element from stack
Medium

You are given N elements and your task is to Implement a Stack in which you can get a minimum element in O(1) time.

Example 1:
Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 2 1

Explanation: In the first test case for
query 
push(2)  Insert 2 into the stack.
         The stack will be {2}
push(3)  Insert 3 into the stack.
         The stack will be {2 3}
pop()    Remove top element from stack 
         Poped element will be 3 the
         stack will be {2}
getMin() Return the minimum element
         min element will be 2 
push(1)  Insert 1 into the stack.
         The stack will be {2 1}
getMin() Return the minimum element
         min element will be 1

Your Task:
You are required to complete the three methods push() which takes one argument an integer 'x' to be pushed into the stack, pop() which returns an integer popped out from the stack, and getMin() which returns the min element from the stack. (-1 will be returned if for pop() and getMin() the stack is empty.)

Expected Time Complexity: O(1) for all the 3 methods.
Expected Auxiliary Space: O(1) for all the 3 methods.

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
*/

// SOLUTION

import java.util.Stack;

class StackWithMin {
    private Stack<Integer> s;
    private Stack<Integer> temp;
    
    public StackWithMin() {
        s = new Stack<>();
        temp = new Stack<>();
    }

    public void push(int x) {
        // If the temp stack is empty or the current element is less than or equal to the top of the temp stack
        if (temp.isEmpty() || x <= temp.peek()) {
            temp.push(x);
        }
        s.push(x);
    }

    public int pop() {
        if (s.isEmpty()) {
            return -1;  // Indicating stack is empty
        }
        // If the popped element is the minimum element, pop it from temp as well
        if (s.peek().equals(temp.peek())) {
            temp.pop();
        }
        return s.pop();
    }

    public int getMin() {
        if (temp.isEmpty()) {
            return -1;  // Indicating no elements in the stack
        }
        return temp.peek();
    }
}
