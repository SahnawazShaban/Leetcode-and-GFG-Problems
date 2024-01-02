"""
Merge k Sorted Arrays

Medium

Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.

Example 1:
Input:
K = 3
arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation:Above test case has 3 sorted
arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],[4, 5, 6], 
[7, 8, 9]]
The merged list will be 
[1, 2, 3, 4, 5, 6, 7, 8, 9].

Example 2:
Input:
K = 4
arr[][]={{1,2,3,4},{2,2,3,4},
         {5,5,6,6},{7,8,9,9}}
Output:
1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
Explanation: Above test case has 4 sorted
arrays of size 4, 4, 4, 4
arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4],
[5, 5, 6, 6], [7, 8, 9, 9 ]]
The merged list will be 
[1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 
6, 6, 7, 8, 9, 9].
Your Task:
You do not need to read input or print anything. Your task is to complete mergeKArrays() function which takes 2 arguments, an arr[K][K] 2D Matrix containing K sorted arrays and an integer K denoting the number of sorted arrays, as input and returns the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python)

Expected Time Complexity: O(K^2*Log(K))
Expected Auxiliary Space: O(K^2)

Constraints:
1 <= K <= 100

"""

# SOLUTION

import heapq

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # Initialize an empty heap and result list
        heap = []
        result = []

        # Push the first element from each array into the heap
        for i in range(len(arr)):
            # Check if the array is not empty
            if arr[i]:
                # Push a tuple (value, array index, element index) into the heap
                heapq.heappush(heap, (arr[i][0], i, 0))

        # Process elements from the heap until it is empty
        while heap:
            # Pop the smallest element from the heap
            val, i, j = heapq.heappop(heap)
            
            # Append the smallest element to the result list
            result.append(val)

            # Move to the next element in the same array if available
            if j + 1 < len(arr[i]):
                # Push the next element from the same array into the heap
                heapq.heappush(heap, (arr[i][j + 1], i, j + 1))

        # Return the merged and sorted result list
        return result
    
    