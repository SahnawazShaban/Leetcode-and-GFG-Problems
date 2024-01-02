"""
Convert Min Heap to Max Heap

Medium

You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.

A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. 

Example 1:
Input:
N = 4
arr = [1, 2, 3, 4]
Output:
[4, 2, 3, 1]
Explanation:

The given min Heap:

          1
        /   \
      2       3
     /
   4

Max Heap after conversion:

         4
       /   \
      2     3
    /
   1

Example 2:
Input:
N = 5
arr = [3, 4, 8, 11, 13]
Output:
[13, 11, 8, 3, 4]
Explanation:

The given min Heap:

          3
        /   \
      4      8
    /   \ 
  11     13

Max Heap after conversion:

          13
        /    \
      11      8
    /   \ 
   3     4
 

Your Task:
Complete the function int convertMinToMaxHeap(), which takes integer N and array represented minheap as input and converts it to the array representing maxheap. You don't need to return or print anything, modify the original array itself.

Note: Only an unique solution is possible under the expected time complexity.

Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(N)


Constraints:

1 <= N <= 10^5
1 <= arr[i] <= 10^9

"""

# SOLUTION

import heapq

class Solution:
    # Solution - 1
    '''
    def convertMinToMaxHeap(self, N, arr):
        maxh = []
        minh = []
        
        # Negate the values before pushing into min-heap
        for i in range(N):
            heapq.heappush(minh, -arr[i])
            
        while len(minh) > 0:
            temp = -heapq.heappop(minh)
            maxh.append(temp)
            
        return maxh
    '''
        
    # -----------------------------------
    
    # Solution - 2
    
    def heapify(self, arr, n, ind):
        """
        Heapify the subtree rooted at index 'ind' in the array 'arr'.

        Parameters:
        - arr: The array representing the heap.
        - n: The size of the heap.
        - ind: The index of the current subtree to heapify.
        """
        target = ind
        left = 2 * ind + 1
        right = 2 * ind + 2

        # Check if left child exists and is greater than the current target
        if left < n and arr[target] < arr[left]:
            target = left

        # Check if right child exists and is greater than the current target
        if right < n and arr[target] < arr[right]:
            target = right

        # If the target has changed, swap the values and continue heapifying
        if target != ind:
            arr[ind], arr[target] = arr[target], arr[ind]
            self.heapify(arr, n, target)
            

    def convertMinToMaxHeap(self, N, arr):
        # Start heapifying from the last non-leaf node up to the root
        for i in range(N // 2 - 1, -1, -1):
            self.heapify(arr, N, i)
        return arr

'''
Time Complexity:
The primary operation in the convertMinToMaxHeap method is the heapify operation, which is called for each non-leaf node in the heap. The heapify operation has a time complexity of O(log N) where N is the number of elements in the heap.
Since we call heapify for each non-leaf node, the overall time complexity is O(N log N), where N is the size of the array.

Space Complexity:
The space complexity is determined by the additional space used by the algorithm. In this case, the algorithm uses a constant amount of extra space for variables like target, left, right, and the loop variable i. Therefore, the space complexity is O(1), which means it is constant and does not depend on the size of the input array.

In summary:
Time Complexity: O(N log N)
Space Complexity: O(1)
'''