"""
Print N to 1 without loop

Print numbers from N to 1 (space separated) without the help of loops.

Example 1:

Input:
N = 10
Output: 10 9 8 7 6 5 4 3 2 1
Your Task:
This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraint
1<=n<=1000

"""

# SOLUTION

class Solution:
    def printNos(self, n):
        if n == 0:
            return 
        
        print(n,end=" ")
        self.printNos(n-1)