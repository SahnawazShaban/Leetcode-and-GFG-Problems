"""
2706. Buy Two Chocolates

Easy

You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

 
Example 1:
Input: prices = [1,2,2], money = 3
Output: 0
Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

Example 2:
Input: prices = [3,2,3], money = 3
Output: 3
Explanation: You cannot buy 2 chocolates without going in debt, so we return 3.
 

Constraints:

2 <= prices.length <= 50
1 <= prices[i] <= 100
1 <= money <= 100

"""


# Solution 

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Solution - 1 - Brute Force
        prices.sort()
        res=money-(prices[0]+prices[1])
        return money if res < 0 else res

        # ----------------------------------------
        # Solution - 2 - Optimal

        # Initialize variables to store the first and second minimum values
        first_min_val = float('inf')
        second_min_val = float('inf')

        # Iterate through the prices list
        for i in range(len(prices)):
            # Check if the current price is less than the first minimum value
            if prices[i] < first_min_val:
                # Update the second minimum value and the first minimum value
                second_min_val, first_min_val = first_min_val, prices[i]
            else:
                # Update the second minimum value if the current price is smaller than the second minimum value
                second_min_val = min(second_min_val, prices[i])

        # Calculate the remaining money after purchasing the two minimum-priced items
        leftover = money - (first_min_val + second_min_val)

        # Check if there is non-negative leftover money
        if leftover >= 0:
            # Return the non-negative leftover money
            return leftover

        # If there is a deficit, return the original money amount
        return money
        

        # -------------------------------------------

        # Solution - 3 - Optimal
        
        first = min(prices)
        prices.remove(first)
        second = min(prices)

        leftover = money - (first + second)

        return leftover if leftover >= 0 else money
        
        
        '''
        Time Complexity:

        Finding the first minimum element using min(arr) takes O(n) time, where n is the length of the array.
        Removing the first minimum element using arr.remove(min1) takes O(n) time in the worst case because it may need to shift elements after the removal point.
        Finding the second minimum element using min(arr) again takes O(n) time.
        Removing the second minimum element using arr.remove(min2) also takes O(n) time in the worst case.
        Therefore, the overall time complexity of the remove_two_min function is O(n).

        Space Complexity:

        The space complexity is O(1) because the function does not use any additional data structures that grow with the input size. It only uses a constant amount of space for variables like min1, min2, and the loop variable.
        '''

        