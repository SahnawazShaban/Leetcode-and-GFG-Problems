"""
279. Perfect Squares

Medium

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of 
some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:
1 <= n <= 10^4

"""


# SOLUTION
class Solution:
    def numSquares(self, n: int) -> int:
        # Recursion: TLE
        # Recursion convert into memo
        
        def solve(n, dp):
            if n == 0:                                                     # part 1
                return 0
                
            if n < 0:                                                      # part 2
                return float("inf")
            
            if dp[n] != -1:
                return dp[n]
                
            mini = n                                                       # part 3 
            
            num = 1
            while num*num <= n:                                            # part 4
                mini = min(mini, solve(n-(num*num), dp))
                num+=1
                
            dp[n] = mini+1
            return dp[n]                                                   # part 5
        
        dp = [-1]*(n+1)
        return solve(n, dp)
        

        # Tabulation - Bottom Up Approach
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]


'''
This step is included to handle cases where the recursive algorithm attempts to go below zero. 
In the context of the problem, negative values are not valid solutions since we're trying to 
represent n as the sum of perfect squares, which are all non-negative integers.

By returning float("inf") (infinity) when n becomes negative, the algorithm effectively 
discards these paths, ensuring that only valid paths leading to the target sum n are 
considered. This is a way of signaling to the algorithm that going down this path will 
not yield a valid solution.

Time Complexity: Exponential, as each recursive call branches out into multiple subproblems. 
However, due to memoization (storing and reusing intermediate results), the effective time 
complexity is reduced to O(n√n), as explained earlier.

Space Complexity: O(n), due to the recursion depth, as each recursive call consumes stack space.

IN Tabulation method reduce Auxiliary space.
'''
