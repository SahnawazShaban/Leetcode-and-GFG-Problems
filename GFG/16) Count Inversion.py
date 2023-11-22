"""
Count Inversions

Medium

banner
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).

Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Example 3:
Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.


Your Task:

You don't need to read input or print anything.
Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*10^5
1 ≤ arr[i] ≤ 10^18

"""

# SOLUTION

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        ## Brute Force
        '''
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > arr[j]:
                    count += 1
        return count
        '''
        
        ## Optimal Approach - Using Merge Sort
        
        count = 0
        if (len(arr) > 1):
            mid = len(arr)//2
            l = arr[:mid]
            r = arr[mid:]
            
            count += self.inversionCount(l,len(l))
            count += self.inversionCount(r,len(r))
            
            i,j,k = 0,0,0
            
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                    count += len(l)-i
                k += 1
            
            while i < len(l):
                arr[k] = l[i]
                k += 1
                i += 1
            
            while j < len(r):
                arr[k] = r[j]
                k += 1
                j += 1
                
        return count
