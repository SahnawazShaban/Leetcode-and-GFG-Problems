"""
Subarray with given sum

Medium

Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements from 2nd position to 4th position is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements from 1st position to 5th position is 15.


Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10^5
0 <= Ai <= 10^9
0<= S <= 10^9


"""

# SOLUTION

class Solution:
    def subArraySum(self, arr, n, s):
        
        # Initialize pointers and variables
        begin = 0        # Start of the current subarray
        end = 0          # End of the current subarray
        cur_sum = 0      # Current sum of elements in the subarray
        res = [-1]       # Default result if no subarray is found
    
        # Iterate through the array elements
        for i in range(n):
            end = i
            cur_sum += arr[i]
    
            # Check if the current sum exceeds the target sum
            # If yes, move the 'begin' pointer to reduce the sum
            while cur_sum > s and begin < i:
                cur_sum -= arr[begin]
                begin += 1
    
            # Check if the current sum equals the target sum
            # If yes, update the result and break out of the loop
            if cur_sum == s:
                res = [begin + 1, end + 1]
                break
    
        return res  # Return the result
    