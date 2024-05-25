"""
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

"""

# SOLUTION

class stack:
    def __init__(self):
        self.s=[]
        self.temp=[]
        self.minEle=None

    def push(self,x):
        # temp work is that to store min value on top of the stack
        if len(self.temp) == 0 or x <= self.temp[-1]:
            self.temp.append(x)
        self.s.append(x)

    def pop(self):
        if not self.s:
            return -1
        if self.s[-1] == self.temp[-1]:
            self.temp.pop(-1)
            
        return self.s.pop()
        
    def getMin(self):
        if not self.temp:
            return -1
        return self.temp[-1]
    