"""
Row with max 1s

Medium

banner
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:  
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.
 

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, M ≤ 10^3
0 ≤ Arr[i][j] ≤ 1 

"""

# SOLUTION

class Solution:
	def rowWithMax1s(self,arr, n, m):
	    # TLE
	    '''
	    maxi = 0
	    idx = -1
		for i in range(n):
		    count = 0
		    for j in range(m):
		        if arr[i][j] == 1:
		            count += 1
		    # possibility of maximum number of count is equal to m (column)
		    if count == m:
		        return i
	        elif count > maxi:
	            idx = i
	            maxi = count
		        
        return idx
        '''
        
        # ------------------------------
        
        # Optimal Solution
        
        # max_ones = 0
        # max_row = -1
    
        # for i in range(n):
        #     count_ones = arr[i].count(1)
            
        #     if count_ones > max_ones:
        #         max_ones = count_ones
        #         max_row = i
                
        # return max_row
		        
		        
	    # Now it's working properly; before I solved it, it gave TLE
	  
		target = -1
		max_count = 0
        for i in range(n):
            count = 0
            for j in range(m):
                if arr[i][j] == 1:
                    count += 1
            if count > max_count:
                max_count = count
                target = i
            
        return target