"""
Buy and Sell a Share at most twice

Medium

In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices. 

Given an array price of size n, find out the maximum profit that a share trader could have made.

Example 1:
Input:
n = 6
prices[] = {10,22,5,75,65,80}
Output:
87
Explanation:
Trader earns 87 as sum of 12, 75 Buy at 10, sell at 22, Buy at 5 and sell at 80.

Example 2:
Input:
n = 7
prices[] = {2,30,15,10,8,25,80}
Output:
100
Explanation:
Trader earns 100 as sum of 28 and 72 Buy at price 2, sell at 30, Buy at 8 and sell at 80,
Your Task:

Complete the function maxProfit() which takes an integer array price as the only argument and returns an integer, representing the maximum profit, if only two transactions are allowed.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:

1 <= n <= 10^5
1 <= price[i] <= 10^5
"""

# Solution

from typing import List

class Solution:
    def maxProfit(self, n : int, prices : List[int]) -> int:
        # Initialize an array to store the maximum profit achievable by
        # making a single transaction from the left side of the array.
        left = [0] * n

        # Initialize the minimum price encountered so far.
        mn = prices[0]

        # Loop through the prices to calculate the maximum profit
        # achievable from the left side of the array.
        for i in range(1, n):
            cur = prices[i]
            mn = min(mn, cur)
            left[i] = max(left[i - 1], cur - mn)
        
        # Initialize variables to keep track of the maximum price encountered
        # so far from the right side of the array and the maximum profit.
        mx = prices[-1]
        result = max(left)

        # Iterate through the prices from right to left to calculate the
        # maximum profit achievable by making two transactions.
        for i in range(n - 2, 0, -1):
            cur = prices[i]
            mx = max(mx, cur)
            # Update the result by considering the maximum profit achievable
            # by making two transactions at this point.
            result = max(result, left[i - 1] + mx - cur)
        
        return result
    