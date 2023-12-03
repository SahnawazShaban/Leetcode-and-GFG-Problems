"""
Quick Sort

Medium

Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.

Example 1:
Input: 
N = 5 
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9

Example 2:
Input: 
N = 9
arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
Output:
1 1 2 3 4 6 7 9 10

Your Task: 
You don't need to read input or print anything. Your task is to complete the functions partition()  and quickSort() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(logN)

Constraints:
1 <= N <= 10^3
1 <= arr[i] <= 10^4

"""

# SOLUTION

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pidx = self.partition(arr,low,high)
            
            self.quickSort(arr,low,pidx-1)
            self.quickSort(arr,pidx+1,high)
        return arr
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        
        x = low-1
        
        for i in range(low,high):
            if arr[i] < pivot:
                x += 1
                
                arr[x], arr[i] = arr[i], arr[x]
        
        x += 1
        # add (pivot+1) elements
        arr[x], arr[high] = arr[high], arr[x]
        
        return x