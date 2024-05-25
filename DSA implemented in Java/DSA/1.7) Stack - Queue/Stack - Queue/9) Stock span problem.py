"""
Stock span problem

Medium

The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stocks price for all n days. 
The span Si of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Example 1:
Input: 
N = 7, price[] = [100 80 60 70 60 75 85]
Output:
1 1 1 2 1 4 6
Explanation:
Traversing the given input span for 100 
will be 1, 80 is smaller than 100 so the 
span is 1, 60 is smaller than 80 so the 
span is 1, 70 is greater than 60 so the 
span is 2 and so on. Hence the output will 
be 1 1 1 2 1 4 6.

Example 2:
Input: 
N = 6, price[] = [10 4 5 90 120 80]
Output:
1 1 2 4 5 1
Explanation:
Traversing the given input span for 10 
will be 1, 4 is smaller than 10 so the 
span will be 1, 5 is greater than 4 so 
the span will be 2 and so on. Hence, the 
output will be 1 1 2 4 5 1.
User Task:
The task is to complete the function calculateSpan() which takes two parameters, an array price[] denoting the price of stocks, and an integer N denoting the size of the array and number of days. This function finds the span of stock's price for all N days and returns an array of length N denoting the span for the i-th day.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 10^5
1 ≤ C[i] ≤ 10^5

"""

# SOLUTION

class Solution:
    
    #Function to calculate the span of stocks price for all n days.
    def calculateSpan(self,a,n):
        v = []      # List to store the span for each day
        stack = []  # Stack to keep track of previous stock prices and their indices
    
        # Iterate through each stock price
        for i in range(n):
            # If the stack is empty, append -1 to the result list
            if len(stack) == 0:
                v.append(-1)
            # If the current stock price is greater than the price at the top of the stack
            elif stack and stack[-1][0] > a[i]:
                # Append the index of the top element in the stack to the result list
                v.append(stack[-1][1])
            # If the current stock price is less than or equal to the price at the top of the stack
            elif stack and stack[-1][0] <= a[i]:
                # Pop elements from the stack until a greater element is found or the stack is empty
                while stack and stack[-1][0] <= a[i]:
                    stack.pop()
                
                # If the stack is empty after popping, append -1 to the result list
                if len(stack) == 0:
                    v.append(-1)
                else:
                    # Append the index of the top element in the stack to the result list
                    v.append(stack[-1][1])
    
            # Push the current stock price and its index onto the stack
            stack.append((a[i], i))
        
        # Calculate the span for each day by subtracting the stored indices from the current index
        for i in range(len(v)):
            v[i] = i - v[i]
        
        return v  # Return the list of spans
    

        '''
        Time Complexity:

        The for loop iterates through each stock price once, and the operations inside the loop are O(1) on average.
        Therefore, the overall time complexity is O(n), where n is the number of stock prices.


        Space Complexity:

        The space complexity is primarily determined by the stack and v lists.
        In the worst case, the stack could store all n elements, leading to a space complexity of O(n).
        The v list also has a length of n.
        Therefore, the overall space complexity is O(n).
        '''