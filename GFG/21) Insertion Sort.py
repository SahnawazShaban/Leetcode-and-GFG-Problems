"""
Insertion Sort

The task is to complete the insert() function which is used to implement Insertion Sort.


Example 1:

Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9


Example 2:

Input:
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output:
1 2 3 4 5 6 7 8 9 10

Your Task: 
You don't have to read input or print anything. Your task is to complete the function insert() and insertionSort() where insert() takes the array, it's size and an index i and insertionSort() uses insert function to sort the array in ascending order using insertion sort algorithm. 

Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 1000
1 <= arr[i] <= 1000

"""

# SOLUTION

## Recursive

class Solution:
    def insert(self, alist, n):
        if n<= 1:
            return
        self.insert(alist,n-1)
        temp = arr[n-1]
        j = n-2
        
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = temp
    
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist,n):
        self.insert(alist,n)



## Normal

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [2, 5, 9, 21, 7, 8, 1]

insertion_sort(arr)

for i in arr:
    print(i, end=" ")