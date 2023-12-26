"""
1155. Number of Dice Rolls With Target Sum

Medium

You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
 

Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
 

Constraints:

1 <= n, k <= 30
1 <= target <= 1000

"""


# Solution 

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Initialize a 2D array to store the subproblem solutions
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: There is one way to achieve a target sum of 0 with 0 rolls
        dp[0][0] = 1

        # Loop through each roll (i) and each possible target sum (j)
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Loop through each face of the die (from 1 to k)
                for face in range(1, k + 1):
                    # Check if subtracting the face value is within the bounds of the target
                    if j - face >= 0:
                        # Update the number of ways to achieve the target sum using the current roll and face
                        dp[i][j] += dp[i - 1][j - face]
                        # Take the result modulo (10^9 + 7) to avoid overflow
                        dp[i][j] %= 10**9 + 7

        # The final result is the number of ways to achieve the target sum with n rolls
        return dp[n][target]

        '''
        Time Complexity:
        The triple nested loop iterates over each roll (i), each possible target sum (j), and each face of the die (face).
        The number of iterations for each loop is proportional to the input parameters (n, k, target), resulting in a time complexity of O(n * k * target).
        
        Space Complexity:
        The space complexity is determined by the size of the 2D array dp, which has dimensions (n + 1) x (target + 1).
        Therefore, the space complexity is O(n * target) since k is a constant factor and doesn't contribute to the overall space complexity.

        In summary:
        Time Complexity: O(n * k * target)
        Space Complexity: O(n * target)

        It's important to note that the modulo operation (dp[i][j] %= 10**9 + 7) within the innermost loop ensures that the values in the dp array remain within a manageable range, preventing integer overflow. This is especially relevant when dealing with large values and a large number of iterations.
        '''

# ---------------------------------
'''
# Recursion with Memorization
def numRollsToTarget_recursion(n, k, target):
    # Dictionary to store already computed results for a given state
    memo = {}

    # Helper function that performs the recursive calculation with memorization
    def helper(n, target):
        # Base case: If there are no more rolls and the target is achieved, return 1
        if n == 0 and target == 0:
            return 1
        # Base cases: If there are no more rolls or the target becomes negative, return 0
        if n == 0 or target < 0:
            return 0
        # Check if the result for the current state (n, target) is already computed
        if (n, target) in memo:
            return memo[(n, target)]

        # Variable to store the number of ways to achieve the target
        ways = 0

        # Iterate over each face of the die (from 1 to k)
        for face in range(1, k + 1):
            # Recursively call the helper function for the next roll, reducing the number of rolls and updating the target
            ways += helper(n - 1, target - face)

        # Memoize the result for the current state
        memo[(n, target)] = ways
        return ways

    # Start the recursion with the given number of rolls (n) and target sum
    return helper(n, target)


# Tabulation
def numRollsToTarget_tabulation(n, k, target):
    # Initialize a 2D array to store the subproblem solutions
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: There is one way to achieve a target sum of 0 with 0 rolls
    dp[0][0] = 1

    # Loop through each roll (i) and each possible target sum (j)
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Loop through each face of the die (from 1 to k)
            for face in range(1, k + 1):
                # Check if subtracting the face value is within the bounds of the target
                if j - face >= 0:
                    # Update the number of ways to achieve the target sum using the current roll and face
                    dp[i][j] += dp[i - 1][j - face]
                    # Take the result modulo (10^9 + 7) to avoid overflow
                    dp[i][j] %= 10**9 + 7

    # The final result is the number of ways to achieve the target sum with n rolls
    return dp[n][target]


# Space-Optimized Tabulation
def numRollsToTarget_space_optimized(n, k, target):
    # Initialize a 1D array to store the solutions to subproblems
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: There is one way to achieve a target sum of 0 with 0 rolls

    # Loop through each roll (i)
    for i in range(1, n + 1):
        # Create a temporary array to store the updated subproblem solutions
        temp = [0] * (target + 1)

        # Loop through each possible target sum (j)
        for j in range(1, target + 1):
            # Loop through each face of the die (from 1 to k)
            for face in range(1, k + 1):
                # Check if subtracting the face value is within the bounds of the target
                if j - face >= 0:
                    # Update the number of ways to achieve the target sum using the current roll and face
                    temp[j] += dp[j - face]
                    # Take the result modulo (10^9 + 7) to avoid overflow
                    temp[j] %= 10**9 + 7

        # Update the dp array with the values from the temporary array
        dp = temp

    # The final result is the number of ways to achieve the target sum with n rolls
    return dp[target]

'''
