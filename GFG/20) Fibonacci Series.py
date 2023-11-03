"""
Fibonacci Series up to Nth term

You are given integer N, and return the Fibonacci Series till the Nth term.

Example:

Input:
5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to
the 5th term.(0-based indexing)
Your Task:
You don't need to read input or print anything. Your task is to complete the function Series() which takes an Integer N as input and returns a Fibonacci Series up to the Nth term.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraint:
1<=n<100

"""

# SOLUTION

class Solution:
    def series(self, n):
        fibo = [0,1]
        
        while len(fibo) <= N:
            next_term = fibo[-1]+fibo[-2]
            fibo.append(next_term)
            
        return fibo