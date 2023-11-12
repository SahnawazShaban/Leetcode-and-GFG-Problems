"""
Maximum of all subarrays of size k

Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example 1:

Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
Explanation: 
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6


Example 2:

Input:
N = 10, K = 4
arr[] = 8 5 10 7 9 4 15 12 90 13
Output: 
10 10 10 15 15 90 90
Explanation: 
1st contiguous subarray = {8 5 10 7}, Max = 10
2nd contiguous subarray = {5 10 7 9}, Max = 10
3rd contiguous subarray = {10 7 9 4}, Max = 10
4th contiguous subarray = {7 9 4 15}, Max = 15
5th contiguous subarray = {9 4 15 12}, 
Max = 15
6th contiguous subarray = {4 15 12 90},
Max = 90
7th contiguous subarray = {15 12 90 13}, 
Max = 90
Your Task:  
You dont need to read input or print anything. Complete the function max_of_subarrays() which takes the array, N and K as input parameters and returns a list of integers denoting the maximum of every contiguous subarray of size K.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ N ≤ 105
1 ≤ K ≤ N
0 ≤ arr[i] ≤ 107
"""

# SOLUTION

from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        result = []
        dq = deque()
    
        for i in range(n):
            # Remove elements outside the current window
            if dq and dq[0] == i - k:
                dq.popleft()
    
            # Remove elements smaller than the current element from the back
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
    
            # Add the current element index to the deque
            dq.append(i)
    
            # Add the maximum element for the current window to the result
            if i >= k - 1:
                result.append(arr[dq[0]])
    
        return result
        
        
        
        # ------------------------------
        ## TLE
        '''
        l = []
        for i in range(n-k+1):
            l1 = arr[i:i+k]
            maxi = max(l1)
            l.append(maxi)
            
        return l
        '''
        
        # ------------------------------
        
        ## TLE
        '''
        max_list = []
        
        for i in range(n-k+1):
            maxi = arr[i]
            for j in range(i,k+i):
                if arr[j] > maxi:
                    maxi = arr[j]
            max_list.append(maxi)
            
        return max_list
        '''

        # ---------------------------------------------------

        '''
        why we store index in deque?

        Storing indices in the deque is a crucial aspect of the algorithm for finding the maximum of all subarrays efficiently. The use of indices in the deque helps to track which elements are still within the current window and which elements have been removed due to moving the window.

        Here's a breakdown of why indices are stored in the deque:

        Removing Elements Outside the Current Window:

        python
        code
        if dq and dq[0] == i - k:
            dq.popleft()
        This condition checks whether the index at the front of the deque (dq[0]) is equal to i - k. If it is, it means that the element at the front is outside the current window, so it gets removed. By storing indices, the algorithm keeps track of the valid elements within the current window efficiently.

        Removing Elements Smaller Than the Current Element from the Back:

        python
        code
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        This loop removes elements from the back of the deque while the current element (arr[i]) is greater than the element at the back of the deque (arr[dq[-1]]). This ensures that the deque only contains indices of elements that are larger than the current element, maintaining a decreasing order of elements in the deque.

        Adding the Current Element Index to the Deque:

        python
        Copy code
        dq.append(i)
        After removing invalid elements, the current element's index (i) is added to the deque. This step ensures that the deque always contains indices corresponding to elements within the current window.

        By storing indices, the algorithm avoids repeatedly searching for the maximum element in the current window. Instead, it efficiently maintains a decreasing order of elements in the deque, allowing for constant-time access to the maximum element's index in the current window. This results in a more optimal solution compared to brute force methods that repeatedly search for the maximum in each subarray.




        User
        expain time and spzce complexity
        ChatGPT
        Let's analyze the time and space complexity of the provided algorithm for finding the maximum of all subarrays of size k using a deque.

        Time Complexity:
        The time complexity of the algorithm is O(n), where n is the length of the input array.

        Loop Over the Array:

        python
        code
        for i in range(n):
        The main loop iterates through each element of the input array exactly once.

        Deque Operations:

        Both popleft() and append() operations on the deque take constant time O(1).
        The while loop that removes smaller elements from the back of the deque can potentially iterate through all elements once, but each element is added or removed from the deque at most once.
        Therefore, the overall time complexity is dominated by the main loop, resulting in O(n).

        Space Complexity:
        The space complexity of the algorithm is O(k), where k is the size of the subarray (window size).

        Deque Size:

        At most, the deque stores k indices. During the iteration, it may temporarily store fewer indices if some elements are removed from the front.
        Result List:

        The result list stores the maximum element for each subarray. In the worst case, it contains n/k elements.
        Considering these factors, the overall space complexity is O(k).

        In summary, the algorithm has a linear time complexity of O(n) and a space complexity linearly proportional to the size of the subarray (O(k)). This makes it an efficient solution for finding the maximum of all subarrays with a fixed window size.
        
        '''