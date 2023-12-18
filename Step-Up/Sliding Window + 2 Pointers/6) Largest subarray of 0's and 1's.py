"""
Largest subarray of 0's and 1's

Easy

Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.

Example 1:
Input:
N = 4
A[] = {0,1,0,1}
Output: 4
Explanation: The array from index [0...3]
contains equal number of 0's and 1's.
Thus maximum length of subarray having
equal number of 0's and 1's is 4.

Example 2:
Input:
N = 5
A[] = {0,0,1,0,0}
Output: 2
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxLen() which takes the array arr[] and the size of the array as inputs and returns the length of the largest subarray with equal number of 0s and 1s.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 10^5
0 <= A[] <= 1

"""

# SOLUTION

# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        # Solution - 1
        '''
        max_length = 0

        for i in range(len(nums)):
            count_zeros = 0
            count_ones = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    count_zeros += 1
                else:
                    count_ones += 1
    
                if count_zeros == count_ones:
                    max_length = max(max_length, j - i + 1)
    
        return max_length
        '''
    
    # --------------------------------------
    
        # Solution - 2
        
        d = {0:-1}
        ans = prefix_sum  = 0
        
        for i in range(N):
            if arr[i] == 1:
                prefix_sum  += 1
            else:
                prefix_sum  -= 1
                
            if prefix_sum  in d:
                ans = max(ans, i-d[prefix_sum ])
            
            if prefix_sum  not in d:
                d[prefix_sum ] = i
        
        return ans
    
'''
Time Complexity:
The time complexity of this optimal solution is O(n), where n is the length of the input array nums. 
The loop iterates through the array once, and within each iteration, the operations performed 
(arithmetic operations, dictionary lookups, and comparisons) are constant time. Therefore, the overall time complexity is linear.

Space Complexity:
The space complexity of this solution is also O(n), where n is the length of the input array nums. 
The primary data structure contributing to space complexity is the prefix_sum_indices dictionary. 
In the worst case, all distinct prefix sums encountered during the iteration will be stored in the dictionary. 
Since the array is of length n, the dictionary may have up to n entries. Therefore, the space complexity is linear.
'''
    
