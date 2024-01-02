"""
k largest elements

Medium

Given an array Arr of N positive integers and an integer K, find K largest elements from the array.  The output elements should be printed in decreasing order.

Example 1:
Input:
N = 5, K = 2
Arr[] = {12, 5, 787, 1, 23}
Output: 787 23
Explanation: 1st largest element in the
array is 787 and second largest is 23.

Example 2:
Input:
N = 7, K = 3
Arr[] = {1, 23, 12, 9, 30, 2, 50}
Output: 50 30 23
Explanation: 3 Largest element in the
array are 50, 30 and 23.
Your Task:
You don't need to read input or print anything. Your task is to complete the function kLargest() which takes the array of integers arr, n and k as parameters and returns an array of integers denoting the answer. The array should be in decreasing order.

Expected Time Complexity: O(K+(N-K)*logK)
Expected Auxiliary Space: O(K+(N-K)*logK)

Constraints:
1 ≤ K ≤ N ≤ 10^5
1 ≤ Arr[i] ≤ 10^6


"""

# SOLUTION

import queue
import heapq
class Solution:

	def kLargest(self,arr, n, k):
	    # SOlution - 1 - TLE
	    '''
		minh = queue.PriorityQueue()
		
		for i in range(n):
		    minh.put(arr[i])
		    
		    if minh.qsize() > k:
		        minh.get()
		
		ans = []
	    while minh.qsize() > 0:
	        ans.append(minh.get())
        
        return ans[::-1]
        '''
        
        # SOlution - 2
        
        minh = []
        
        for i in range(n):
            heapq.heappush(minh, arr[i])
            
            if len(minh) > k:
                heapq.heappop(minh)
                
        ans = []
        while len(minh) > 0:
            ans.append(heapq.heappop(minh))
            
        return ans[::-1]

        
'''
Time Complexity:
The loop that iterates over the elements of the array and pushes them onto the heap (heapq.heappush) runs in O(n * log(k)) time. In each iteration, the heappush operation takes log(k) time because the heap has a maximum size of k.
The loop that iterates over the elements in the heap and pops them (heapq.heappop) also runs in O(k * log(k)) time. In each iteration, the heappop operation takes log(k) time.
The dominating term is the O(n * log(k)) term. So, the overall time complexity is O(n * log(k)).

Space Complexity:
The space complexity is O(k) because the heap has a maximum size of k, storing the k largest elements.
So, in terms of time complexity, the code is efficient, especially when k is much smaller than n. The space complexity is also reasonable, as it depends on the value of k.
'''

