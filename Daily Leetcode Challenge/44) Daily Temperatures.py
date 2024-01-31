"""
739. Daily Temperatures

Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

"""


# SOLUTION

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Initialize a result array with zeros
        res = [0]*n
        
        # Stack to store indices and corresponding values
        stack = []
        
        # Loop through each temperature and its index
        for idx, val in enumerate(temperatures):
            # Check if the stack is not empty and the current temperature is greater than the one at the top of the stack
            while stack and stack[-1][1] < val:
                # Pop the element from the stack
                index, value = stack.pop()

                # Update the result for the popped index with the time difference
                res[index] = idx - index

            # Push the current index and temperature onto the stack
            stack.append([idx, val])

        # Return the resulting array
        return res
    

'''
Time Complexity:
The time complexity is O(N), where N is the number of temperatures in the input array. 
In the worst case, each temperature is pushed and popped from the stack once, and each operation takes constant time.

Space Complexity:
The space complexity is also O(N), where N is the number of temperatures in the input array. 
In the worst case, the stack may have to store all temperatures if they are in non-decreasing order. 
Therefore, the space required for the stack is proportional to the number of temperatures.

In summary:
Time Complexity: O(N)
Space Complexity: O(N)
'''
    