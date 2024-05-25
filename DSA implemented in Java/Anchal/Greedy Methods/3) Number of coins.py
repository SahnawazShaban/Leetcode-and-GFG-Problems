"""
Number of Coins

Medium

Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:
Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin

Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1}
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin

Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 10^6
All array elements are distinct

"""

# SOLUTION

class Solution:
	def minCoins(self, coins, M, V):
	    # DP Approach
	    
		# Initialize a table to store minimum number of coins for each value from 0 to V
        dp = [float('inf')] * (V + 1)
        
        # Base case: minimum coins needed to make change for 0 cents is 0
        dp[0] = 0
        
        # Iterate through each coin and update the minimum number of coins needed for each value
        for coin in coins:
            for value in range(coin, V + 1):
                dp[value] = min(dp[value], dp[value - coin] + 1)
        
        # If dp[V] is still infinity, it means it's not possible to make change for V cents
        return dp[V] if dp[V] != float('inf') else -1
        
        
        # Greedy Algorithm : [2,5,8,9,11,14,17,18]
        '''
        coins.sort(reverse = True)
        count = 0
        
        for coin in coins:
            while V >= coin:
                V -= coin
                count += 1
                
        return count
        '''

'''
Time Complexity:
The time complexity of the provided dynamic programming solution is O(V * M), 
where V is the target value and M is the number of different coin denominations. 
This is because there are two nested loops: one iterating over the coins and the 
other over the possible values from 0 to V.

Space Complexity:
The space complexity is O(V) since the dynamic programming table (dp) has a length of V + 1.
'''