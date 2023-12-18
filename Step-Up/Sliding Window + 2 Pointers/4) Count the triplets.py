"""
Count the triplets

Easy

Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1:
Input: 
N = 4 
arr[] = {1, 5, 3, 2}
Output: 2 
Explanation: There are 2 triplets:
 1 + 2 = 3 and 3 +2 = 5

Example 2:
Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10^3
1 ≤ arr[i] ≤ 10^5

"""

# SOLUTION

class Solution:
	def countTriplet(self, arr, n):
        # Solution - 1
        # TLE
        '''
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                temp = arr[i] + arr[j]
                if temp in arr:
                    count += 1
                    
        return count
        '''
		
# 		---------------------------------------

        # Solution - 2
        
        count = 0
        arr.sort()
        
        for i in range(n-1,1,-1):
            l = 0
            r = i-1
            
            while l < r:
                if (arr[l] + arr[r]) == arr[i]:
                    count += 1
                    l += 1
                    r -= 1
                elif (arr[l]+arr[r]) < arr[i]:
                    l += 1
                else:
                    r -= 1
                    
        return count

'''
Time Complexity:

Sorting the array has a time complexity of O(n log n).
The nested loops iterate through all pairs of elements in the array, which is O(n^2).
The overall time complexity is dominated by the sorting, so it is O(n log n).

Space Complexity:

The space complexity is O(1) because the algorithm uses only a constant amount of additional space (for variables like count, l, r, etc.), regardless of the input size.
'''

