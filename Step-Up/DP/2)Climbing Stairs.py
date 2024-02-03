"""
70. Climbing Stairs

Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45

"""

# SOLUTION

class Solution:
    # Recursion : TLE
    '''
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        left = self.climbStairs(n-1)
        right = self.climbStairs(n-2)

        return left + right
    '''

    # Memoization
    def climbStairs(self, n: int) -> int:
        def func(idx, dp):
            if idx == 0 or idx == 1:
                return 1

            if dp[idx] != -1:
                return dp[idx]

            dp[idx] = func(idx-1, dp) + func(idx-2, dp)

            return dp[idx]

        dp = [-1]*(n+1)

        ans = func(n, dp)
        return ans
        

'''
TC = O(n), where "n" is the input parameter. 
     This is because each value in the memoization array is computed only once, 
     and there are a total of "n" values to be computed.
SC = O(n)[auxilairy space] + O(n)[array space]
'''

class Solution:

    # Memoization
    def climbStairs(self, n: int) -> int:
        # Recursive function to calculate the number of ways to climb stairs
        def func(idx, dp):
            # Base case: if the current step is 0 or 1, there is only one way to climb
            if idx == 0 or idx == 1:
                return 1

            # Check if the result for the current step is already calculated (memoization)
            if dp[idx] != -1:
                return dp[idx]

            # Recursive calculation of the number of ways to climb the current step
            dp[idx] = func(idx-1, dp) + func(idx-2, dp)

            # Return the calculated result for the current step
            return dp[idx]

        # Initialize memoization array with -1 for each step
        dp = [-1]*(n+1)

        # Call the recursive function to calculate the total number of ways to climb stairs
        ans = func(n, dp)
        return ans

    # Tabulation
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


    # Space Optimization
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        prev1 = prev2 = 1

        for i in range(2, n+1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur
