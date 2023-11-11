"""
Count the subarrays having product less than k

Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.

Example 1:

Input : 
n = 4, k = 10
a[] = {1, 2, 3, 4}
Output : 
7
Explanation:
The contiguous subarrays are {1}, {2}, {3}, {4} 
{1, 2}, {1, 2, 3} and {2, 3}, in all these subarrays
product of elements is less than 10, count of
such subarray is 7.
{2,3,4} will not be a valid subarray, because 
2*3*4=24 which is greater than 10.


Example 2:

Input:
n = 7 , k = 100
a[] = {1, 9, 2, 8, 6, 4, 3}
Output:
16
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSubArrayProductLessThanK() which takes the array a[], its size n and an integer k as inputs and returns the count of required subarrays.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<=n<=106
1<=k<=1015
1<=a[i]<=105

"""

# SOLUTION

class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        if k <= 1:
            return 0  # Since all products will be greater than or equal to 1

        product = 1
        count = 0
        left = 0
    
        for right in range(n):
            product *= arr[right]
    
            while product >= k:
                product /= arr[left]
                left += 1
    
            count += right - left + 1
    
        return count
        
        # -------------------------------
        
        ## TLE
        '''
        count = 0

        for left in range(n):
            product = 1
            for right in range(left, n):
                product *= arr[right]
                if product < k:
                    count += 1
                else:
                    break
    
        return count
        '''