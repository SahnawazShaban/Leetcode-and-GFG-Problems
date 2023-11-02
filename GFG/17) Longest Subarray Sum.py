"""
Longest Sub-Array with Sum K

Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

 

Example 1:
 
Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.


Example 2:

Input : 
A[] = {-1, 2, 3}
K = 6
Output : 0
Explanation: 
There is no such sub-array with sum 6.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function lenOfLongSubarr() that takes an array (A), sizeOfArray (n),  sum (K)and returns the required length of the longest Sub-Array. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).


Constraints:
1<=N<=105
-105<=A[i], K<=105

"""

# SOLUTION

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        preSum = 0
        maxLen = 0
        temp_dict = {}
        
        for i in range(n):
            # add the current element to the sum
            preSum += arr[i]
            
            # if the current sum is equal to k if yes then add the maxlength
            if preSum == k:
                maxLen = max(maxLen, i+1)
            
            # here diff is important because we store the cummulative sum in hashmap. By the time we find the diff in hashmap we can guarantee that its length is greater than the previous one
            diff = preSum - k
            
            if diff in temp_dict:
                maxLen = max(maxLen, i - temp_dict[diff])
                
            # below condition is very important because there might some edge cases of 0
            if preSum not in temp_dict:
                temp_dict[preSum] = i
                
        # We are adding cumulative sum to the hashmap along with its index
        return maxLen
