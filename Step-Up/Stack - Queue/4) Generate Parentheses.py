"""
Generate Parentheses

Medium

Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.


Example 1:
Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()

Example 2:
Input:
N = 1
Output:
()

Your Task:  
You don't need to read input or print anything. Complete the function AllParenthesis() which takes N as input parameter and returns the list of balanced parenthesis.

Expected Time Complexity: O(2^N * N).
Expected Auxiliary Space: O(2*N*X), X = Number of valid Parenthesis.

Constraints:
1 ≤ N ≤ 12

"""

# SOLUTION

class Solution:
    def AllParenthesis(self,n):
        # Solution - 1
        def solve(Open,close,op,ans):
            if Open == 0 and close == 0:
                ans.append(op)
                return 
            
            if Open != 0:
                op1 = op
                
                op1 += '('
                
                solve(Open-1,close,op1,ans)
                
            if close > Open:
                op2 = op
                
                op2 += ')'
                
                solve(Open,close-1,op2,ans)
        
        ans = []
        solve(n,n,"",ans)
        return ans
        
        # Time and Space Complexity
        
        # Time Complexity: O(2^n)
        # Space Complexity: O(2n + 2^n)
        
# ----------------------------------------------
        # Solution - 2
        '''
        res = []
        def dfs(s,open,close):
            if len(s) == n*2:
                res.append(s)
                return
            if open <n:
                dfs(s+'(',open+1,close)
            if close<open:
                dfs(s+')',open,close+1)
        dfs('',0,0)
        return res
        '''

'''
Time Complexity : The time complexity is determined by the number of recursive calls made by the `solve` function. In each recursive call, either an open parenthesis or a close parenthesis is added to the partial solution (`op`). The base case is reached when both the open and close counts are zero. In each recursive call, we either decrement the open count or the close count. Therefore, the total number of recursive calls is 2^n, where nnn is the input value.
As a result, the time complexity is O(2^n).

Space Complexity : The space complexity is determined by the depth of the recursive call stack and the space required to store the intermediate solutions. In each recursive call, a new string `op1` or `op2` is created to represent the partial solution. The maximum depth of the recursive call stack is 2n, as we decrement either the open count or the close count in each call.
Additionally, the space required to store the result (valid combinations) is proportional to the number of valid combinations, which is O(2^n).
Therefore, the overall space complexity is O(2n + 2^n).

In summary:

*   Time Complexity: O(2^n)
*   Space Complexity: O(2n + 2^n)
'''
        