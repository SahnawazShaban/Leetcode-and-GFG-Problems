"""
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

"""

# SOLUTION

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def insertSort(self, s, temp):
        if len(s) == 0 or s[len(s)-1] <= temp:
            s.append(temp)
            return
        
        val = s[len(s)-1]
        s.pop()
        self.insertSort(s, temp)
        s.append(val)
        
        
    def Sorted(self, s):
        # Brute Force
        '''
        n = len(s)
        
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i] > s[j]:
                    s[i], s[j] = s[j], s[i]
                    
        return s
        '''
        
        # Better
        
        n = len(s)
        if len(s) == 0:
            return 
        
        temp = s[n-1]
        s.pop()
        self.Sorted(s)
        self.insertSort(s,temp)
        