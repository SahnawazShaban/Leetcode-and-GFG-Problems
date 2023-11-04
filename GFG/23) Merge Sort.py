"""
Merge Sort

Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9


Example 2:

Input:
N = 10
arr[] = {10 9 8 7 6 5 4 3 2 1}
Output:
1 2 3 4 5 6 7 8 9 10

Your Task:
You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

Expected Time Complexity: O(nlogn) 
Expected Auxiliary Space: O(n)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 105

"""

# SOLUTION

class Solution:
    def merge(self,arr, l, m, r): 
        mergeList = [0]*(r-l+1)
        
        idx1 = l
        idx2 = m+1
        
        x = 0
        
        while(idx1 <= m and idx2 <= r):
            if arr[idx1] <= arr[idx2]:
                mergeList[x] = arr[idx1]
                x += 1
                idx1 += 1
            else:
                mergeList[x] = arr[idx2]
                x += 1
                idx2 += 1
                
        while(idx1 <= m):
            mergeList[x] = arr[idx1]
            x += 1
            idx1 += 1
            
        while(idx2 <= r):
            mergeList[x] = arr[idx2]
            x += 1
            idx2 += 1
            
        for i in range(len(mergeList)):
            arr[i+l] = mergeList[i]
        
        return arr
        
        
    def mergeSort(self,arr, l, r):
        if l >= r:
            return
        
        mid = l+(r-l)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        self.merge(arr, l, mid, r)